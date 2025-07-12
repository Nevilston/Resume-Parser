from sentence_transformers import SentenceTransformer, util
from rapidfuzz import fuzz
from nltk.corpus import wordnet
import nltk

# Download WordNet if not already
nltk.download('wordnet')

# ✅ Skill normalization map
def normalize_skill(skill: str) -> str:
    aliases = {
        "amazon web services": "aws",
        "amazon web service": "aws",
        "aws cloud": "aws",
        "m-rcnn": "mask rcnn",
        "scikit learn": "scikit-learn",
        "tensor flow": "tensorflow",
        "team work": "teamwork",
        "communication skills": "communication",
        "opencv library": "opencv",
        "greenhouse gas": "ghg emissions",
        "mac os": "mac",
        "macos": "mac",
        "windows os": "windows",
        "win": "windows",
        "linux os": "linux"
    }
    skill = skill.strip().lower()
    return aliases.get(skill, skill)

# ✅ WordNet-based synonym fetcher
def get_synonyms(skill: str):
    synonyms = set()
    for syn in wordnet.synsets(skill):
        for lemma in syn.lemmas():
            name = lemma.name().lower().replace('_', ' ')
            if len(name) > 2:
                synonyms.add(name)
    return synonyms

class ResumeShortlister:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def compute_semantic_score(self, resume_text: str, jd_text: str) -> float:
        embeddings = self.model.encode([resume_text, jd_text], convert_to_tensor=True)
        similarity = util.cos_sim(embeddings[0], embeddings[1])
        return float(similarity.item() * 100)

    def fuzzy_match(self, jd_skills: list, resume_skills: list, threshold: int = 80):
        matched = []
        unmatched = []

        normalized_resume_skills = {normalize_skill(s): s for s in resume_skills}
        normalized_resume_set = set(normalized_resume_skills.keys())

        for jd_skill in jd_skills:
            jd_skill_norm = normalize_skill(jd_skill)
            found = False

            # Direct fuzzy match
            for resume_skill_norm in normalized_resume_set:
                if fuzz.token_set_ratio(jd_skill_norm, resume_skill_norm) >= threshold:
                    matched.append(jd_skill)
                    found = True
                    break

            # WordNet synonym match
            if not found:
                for synonym in get_synonyms(jd_skill_norm):
                    for resume_skill_norm in normalized_resume_set:
                        if fuzz.token_set_ratio(synonym, resume_skill_norm) >= threshold:
                            matched.append(jd_skill)
                            found = True
                            break
                    if found:
                        break

            if not found:
                unmatched.append(jd_skill)

        return matched, unmatched

    def classify_match_level(self, score: float) -> str:
        if score >= 80:
            return "high"
        elif score >= 60:
            return "medium"
        elif score >= 50:
            return "low"
        else:
            return "very low"

    def evaluate(self, resume_text: str, jd_text: str, resume_skills: list, jd_skills: list):
        semantic_score = self.compute_semantic_score(resume_text, jd_text)
        matched, missing = self.fuzzy_match(jd_skills, resume_skills)

        skill_match_pct = (len(matched) / len(jd_skills)) * 100 if jd_skills else 0
        final_score = round(semantic_score * 0.6 + skill_match_pct * 0.4, 2)
        match_level = self.classify_match_level(final_score)

        return {
            "final_score": final_score,
            "shortlisted": final_score >= 50,
            "match_level": match_level,
            "semantic_score": round(semantic_score, 2),
            "skill_match_pct": round(skill_match_pct, 2),
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing)
        }
