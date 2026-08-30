from fastapi import FastAPI
from pydantic import BaseModel

from src.extract import extract_age, extract_medication_dose

app = FastAPI(title="Clinical Text API")


class ExtractRequest(BaseModel):
    text: str

class ExtractResponse(BaseModel):
    age: int | None
    medication_dose: str | None

@app.get("/")
def read_root() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/extract", response_model=ExtractResponse)
def extract(request: ExtractRequest) -> ExtractResponse:
    """Extract structured fields from clinical text."""
    return ExtractResponse(
        age=extract_age(request.text),
        medication_dose=extract_medication_dose(request.text),
    )