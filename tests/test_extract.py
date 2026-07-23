from src.extract import extract_age


def test_extract_age_simple():
    assert extract_age("Patient is a 45-year-old male") == 45


def test_extract_age_none():
    assert extract_age("No age mentioned") is None