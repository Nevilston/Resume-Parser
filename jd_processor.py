class JDProcessor:
    def clean(self, jd_text: str) -> str:
        return jd_text.strip().replace("\n", " ").lower()
