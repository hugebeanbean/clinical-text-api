from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

from src.extract import extract_age, extract_medication_dose


ner_pipeline = pipeline(
    "token-classification",
    model="d4data/biomedical-ner-all",
    aggregation_strategy="simple",
)

app = FastAPI(title="Clinical Text API")

class NERResponse(BaseModel):
    entities: list[dict]

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

@app.post("/ner", response_model=NERResponse)
def ner(request: ExtractRequest) -> NERResponse:
    """Run biomedical named entity recognition on text."""
    results = ner_pipeline(request.text)
    entities = [
        {"text": r["word"], "label": r["entity_group"], "score": float(r["score"])}
        for r in results
    ]
    return NERResponse(entities=entities)