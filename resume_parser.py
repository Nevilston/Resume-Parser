import pdfplumber
from docx import Document
import os

class ResumeParser:
    def parse(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".pdf":
            return self._parse_pdf(file_path)
        elif ext == ".docx":
            return self._parse_docx(file_path)
        else:
            raise ValueError("Unsupported file format")

    def _parse_pdf(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])

    def _parse_docx(self, file_path):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
