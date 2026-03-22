import re
import string

def clean_text(text: str) -> str:
    """
    Basic NLP preprocessing:
    - Lowercase
    - Remove punctuation
    - Strip extra whitespace
    """
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
