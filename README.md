# 🧠 AI Resume Shortlister 🚀

A powerful Python-based AI tool to automatically evaluate and shortlist resumes based on job descriptions using semantic similarity, fuzzy skill matching, and synonym support via WordNet. 

---

## 📌 Features

✅ **Semantic Matching**  
Compare resume and job description context using Sentence-BERT embeddings.

✅ **Skill Extraction & Matching**  
- Uses GPT & regex-based parsing  
- Normalizes skill names and aliases  
- Supports fuzzy and synonym-based matching

✅ **Shortlisting Logic**  
Combines semantic score and skill match percentage to compute a final score with thresholds for:
- High
- Medium
- Low
- Very Low

✅ **Synonym Support (via WordNet)**  
Matches skills with similar meaning (e.g., “teamwork” ≈ “team work”).

---

## 📂 Project Structure

```
.
├── main.py                      # 🔁 Entry point
├── resume_parser.py            # 📄 PDF/Text resume extractor
├── jd_processor.py             # 🧾 Cleans and formats JD text
├── resume_shortlister.py       # 🧠 Core logic: scoring + shortlisting
├── openai_skill_extractor.py   # 🤖 GPT-based skill extraction
├── openai_config.py            # 🔐 OpenAI API key loading
├── .env                        # 🔐 Contains OPENAI_API_KEY
├── requirements.txt            # 📦 Dependencies
└── README.md                   # 📘 This file
```

---

## ⚙️ How It Works

1. **Parse Resume & JD**  
   Extracts plain text and structured skills from both.

2. **Skill Extraction**  
   Uses GPT + rule-based keywords to find relevant technical and soft skills.

3. **Matching & Scoring**
   - Semantic similarity via `SentenceTransformer`
   - Fuzzy skill match (`RapidFuzz`)
   - Synonym match via WordNet

4. **Shortlisting Decision**
   ```python
   final_score = 0.6 * semantic_score + 0.4 * skill_match_pct
   ```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/ai-resume-shortlister.git
cd ai-resume-shortlister
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup your OpenAI API Key
Create a `.env` file with the following:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxx
```

### 4️⃣ Run the app
```bash
python3 main.py
```

---

## 📊 Sample Output

```
✅ Shortlist Result:

{
  'final_score': 58.91,
  'shortlisted': True,
  'match_level': 'low',
  'semantic_score': 40.4,
  'skill_match_pct': 86.67,
  'matched_skills': [...],
  'missing_skills': [...]
}
```

---

## 🧠 Tech Stack

- Python 3.8+
- [SentenceTransformers](https://www.sbert.net/)
- [OpenAI GPT](https://platform.openai.com/)
- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz)
- [NLTK WordNet](https://www.nltk.org/howto/wordnet.html)
- PyMuPDF (PDF parsing)

---

## 🙌 Contributing

Feel free to fork and open PRs to add:
- Streamlit Web UI
- JD parsing with LLMs
---

