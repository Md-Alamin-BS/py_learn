import re


def normalize_text(text: str):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)  # replace repeating whitespaces with 1 space
    text = re.sub(r"\.+", ".", text)  # replace repeated dots with 1 dot
    return text
