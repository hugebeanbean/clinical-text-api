from fastapi import FastAPI

app = FastAPI(title="Clinical Text API")


@app.get("/")
def read_root() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}
