# 🧠 AI Resume Shortlister 🚀

A Python-based AI tool to automatically evaluate and shortlist resumes based on job descriptions using semantic similarity and skill matching.

---

## 📌 Features

✅ **Semantic Matching**  
- Compares resume and JD using Sentence-BERT embeddings

✅ **Skill Extraction & Matching**  
- Extracts skills using GPT + regex rules  
- Matches technical and soft skills

✅ **Shortlisting Logic**  
Scores candidates based on:
- Semantic similarity
- Skill match percentage

```
final_score = 0.6 * semantic_score + 0.4 * skill_match_pct
```

✅ **Synonym Matching**  
Uses WordNet to recognize skill aliases (e.g., “team work” ≈ “teamwork”).

---

## 📂 Project Structure

```
.
├── api.py                      # 🔗 Flask API endpoint
├── main.py                     # 🔁 Processing logic (resume + JD)
├── resume_parser.py            # 📄 Resume parsing (PDF/DOCX)
├── jd_processor.py             # 🧾 JD cleaner
├── resume_shortlister.py       # 🧠 Matching + Scoring
├── openai_skill_extractor.py   # 🤖 GPT-based skill extraction
├── openai_config.py            # 🔐 API key loader
├── requirements.txt            # 📦 Python dependencies
└── .env                        # 🔐 Your OpenAI key
```

---

## ⚙️ How It Works

1. **Resume & JD Parsing**  
   Extract plain text from uploaded resume and JD input.

2. **Skill Extraction**  
   Identify relevant skills using GPT and regex patterns.

3. **Matching & Scoring**
   - Semantic similarity (via Sentence-BERT)
   - Skill match percentage
   - Synonym-aware comparison

4. **Shortlist Decision**
   Final JSON includes:
   - final score
   - matched/missing skills
   - semantic score
   - match level

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/ai-resume-shortlister.git
cd ai-resume-shortlister
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up OpenAI Key

Create a `.env` file with your OpenAI key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

---

## 🔗 Using the Flask API

### ▶️ Start the API

```bash
python3 api.py
```

By default, it runs at: `http://localhost:5000`

---

### 📬 Endpoint: `/api/shortlist`

**Method**: `POST`  
**Content Type**: `multipart/form-data`  
**Params**:

| Key     | Type  | Required | Description             |
|---------|-------|----------|-------------------------|
| `resume`| File  | ✅       | Resume PDF or DOCX      |
| `jd`    | Text  | ✅       | Job description content |

---

### 🔧 Example (Postman)

- Method: `POST`
- URL: `http://localhost:5000/api/shortlist`
- Body → `form-data`:
  - `resume`: Upload file (PDF or DOCX)
  - `jd`: Paste job description text

---

### 🧪 Sample JSON Response

```json
{
  "final_score": 58.91,
  "shortlisted": true,
  "match_level": "low",
  "semantic_score": 40.4,
  "skill_match_pct": 86.67,
  "matched_skills": ["python", "scikit-learn", "tensorflow"],
  "missing_skills": ["aws", "mongodb"]
}
```

---

## 🧠 Tech Stack

- Python 3.8+
- Flask (API framework)
- OpenAI (skill extraction)
- SentenceTransformers (semantic similarity)
- pdfplumber / python-docx (resume parsing)
- RapidFuzz (fuzzy skill matching)
- WordNet (synonyms)

---

## 🙌 Contributing

PRs are welcome for:
- UI frontend (e.g., Streamlit)
- Enhanced JD parsing
- Bulk resume ranking
