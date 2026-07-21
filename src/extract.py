import re

def extract_age(text: str) -> int | None:
    """Find an age like '45 years old' in clinical text. Return the age, or None."""
    match = re.search(r"(\d{1,3})[- ]year[- ]old", text)
    if match:
        return int(match.group(1))
    return None