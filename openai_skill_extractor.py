from openai import OpenAI
import json

class OpenAISkillExtractor:
    def __init__(self, client: OpenAI, model="gpt-3.5-turbo"):
        self.client = client
        self.model = model

    def extract_skills(self, text: str) -> list:
        prompt = f"""
You are an expert resume parser. Extract a list of unique, relevant skills from the following text.
Return only the skill names as a JSON array. Do not include explanation or formatting.

Text:
\"\"\"{text}\"\"\"
"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=500
            )

            content = response.choices[0].message.content.strip()

            try:
                return json.loads(content)
            except json.JSONDecodeError:
                lines = content.splitlines()
                return [
                    line.strip("-•0123456789. ").strip()
                    for line in lines if line.strip()
                ]

        except Exception as e:
            print("Error extracting skills:", e)
            return []
