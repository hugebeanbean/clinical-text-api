from src.extract import extract_age


def test_extract_age_simple():
    assert extract_age("Patient is a 45-year-old male") == 45


def test_extract_age_none():
    assert extract_age("No age mentioned") is None


def test_extract_age_missing():
    assert extract_age("No age mentioned here") is None


def test_extract_age_with_space():
    assert extract_age("a 60 year old female") == 60


def test_extract_age_empty():
    assert extract_age("") is None


def test_extract_age_at_start():
    assert extract_age("72-year-old with epilepsy") == 72


def test_extract_age_impossible():
    assert extract_age("250 year old male") == None