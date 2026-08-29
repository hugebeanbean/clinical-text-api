from fastapi import FastAPI
from pydantic import BaseModel

from src.extract import extract_age, extract_medication_dose

app = FastAPI(title="Clinical Text API")


class ExtractRequest(BaseModel):
    text: str


@app.get("/")
def read_root() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/extract")
def extract(request: ExtractRequest) -> dict:
    """Extract structured fields from clinical text."""
    return {
        "age": extract_age(request.text),
        "medication_dose": extract_medication_dose(request.text),
    }