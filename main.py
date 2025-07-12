from openai_config import configure_openai
from openai import OpenAI
from resume_parser import ResumeParser
from jd_processor import JDProcessor
from openai_skill_extractor import OpenAISkillExtractor
from resume_shortlister import ResumeShortlister
import re


def extract_known_skills_from_resume_text(resume_text: str) -> list:
    # Match TECHNICAL SKILLS, PROJECTS, SOFT SKILLS, and EXPERIENCE sections
    patterns = [
        r"(?<=Objective)(.*?)(?=(TECHNICAL SKILLS|PROJECTS|EXPERIENCE|SOFT SKILLS|$))",
        r"(?<=TECHINICAL SKILLS)(.*?)(?=(EXPERIENCE|PROJECTS|SOFT SKILLS|$))",
        r"(?<=PROJECTS)(.*?)(?=(EXPERIENCE|SOFT SKILLS|$))",
        r"(?<=Soft Skills:)(.*?)(?=(Languages:|Hobbies:|$))",
        r"(?<=EXPERIENCE)(.*?)(?=(EDUCATION|CERTIFICATIONS|$))",
        r"(?<=Operating System:)(.*?)(?=(\n|$))"
    ]

    extracted_text = ""
    for pattern in patterns:
        match = re.search(pattern, resume_text, re.DOTALL | re.IGNORECASE)
        if match:
            extracted_text += match.group() + "\n"

    # Explicit splitting of comma-separated and bullet-separated lines
    inline_skills = re.split(r"[•,\n]", extracted_text)

    # Common skill and domain keywords — expanded and corrected
    keywords = re.findall(
        r"\b(?:TensorFlow|Deep Learning|Machine Learning|Predictive Models|Python|Mask RCNN|Greenhouse Gas|GHG|Raspberry Pi|AWS|MongoDB|Linux|Windows|Mac|MacOS|Communication|Team Work|Object Detection|Detectron|Scikit-Learn|Numpy|Pandas|Matplotlib|C\+\+|Java|SQL|R|Problem Solving)\b",
        extracted_text,
        re.IGNORECASE
    )

    # Normalize for matching, keep casing for readability
    skills = [k.strip().lower().replace("macos", "mac") for k in keywords]
    return list(set(skills))


# 🔧 Load .env and OpenAI client
configure_openai()
client = OpenAI()

# 🔧 Initialize all components
resume_parser = ResumeParser()
jd_processor = JDProcessor()
skill_extractor = OpenAISkillExtractor(client=client)
shortlister = ResumeShortlister()

# 📄 File and JD Text
resume_file = "/Users/nevilston/Downloads/Deoston-Resume.pdf"
jd_text = """
🎯 Job Title: AI Intern – Python, TensorFlow, Projects

We are looking for a recent graduate or final-year student with a strong academic background in Artificial Intelligence. The ideal candidate should have hands-on experience with Python programming and machine learning tools, and have completed academic or internship projects involving model development.

🔧 Responsibilities:
- Build predictive models using Scikit-Learn and TensorFlow
- Analyze datasets using Pandas, NumPy, and Matplotlib
- Apply machine learning in areas like greenhouse gas (GHG) emissions or plant disease detection
- Collaborate with mentors in developing model pipelines
- Work in Linux-based environments with basic AWS and MongoDB knowledge

✅ Required Skills:
- Programming: Python, R, Java, C++
- Machine Learning: TensorFlow, Scikit-Learn
- Data Tools: Numpy, Pandas, Matplotlib
- Databases: SQL, basic MongoDB
- Cloud: Basic AWS
- OS: Linux, Windows, Mac
- Soft Skills: Problem Solving, Team Work, Communication
- Internship or project experience in AI-based GHG 
"""

# 🔍 Parse resume and JD
resume_text = resume_parser.parse(resume_file)
jd_clean = jd_processor.clean(jd_text)

# 🔍 Extract skills from both resume and JD
structured_resume_skills = extract_known_skills_from_resume_text(resume_text)
gpt_resume_skills = skill_extractor.extract_skills(resume_text)
resume_skills = list(set(structured_resume_skills + gpt_resume_skills))

jd_skills = skill_extractor.extract_skills(jd_clean)

# 🧠 Evaluate match
result = shortlister.evaluate(resume_text, jd_clean, resume_skills, jd_skills)

# 📤 Output
print("\n✅ Shortlist Result:\n")
print(result)
