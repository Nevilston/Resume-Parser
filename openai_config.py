from dotenv import load_dotenv
import os

def configure_openai() -> str:
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
