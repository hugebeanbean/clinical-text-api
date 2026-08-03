import re


def extract_age(text: str) -> int | None:
    """Find an age like '45-year-old' in clinical text. Return the age, or None."""
    match = re.search(r"(\d{1,3})[- ]year[- ]old", text)
    if match:
        age = int(match.group(1))
        if age <= 120:  # reject impossible ages
            return age
    return None


def extract_medication_dose(text: str) -> str | None:
    """Find a medication dose like '500mg twice daily'. Return it normalized, or None."""
    match = re.search(r"(\d+)\s*mg (twice daily|once daily)", text)
    if match:
        number = match.group(1)
        frequency = match.group(2)
        return f"{number}mg {frequency}"
    return None
