from src.extract import extract_medication_dose


def test_dose_twice_daily():
    assert extract_medication_dose("500mg twice daily") == "500mg twice daily"


def test_dose_once_daily():
    assert extract_medication_dose("take 250 mg once daily") == "250mg once daily"


def test_dose_missing():
    assert extract_medication_dose("patient reports fatigue") is None
