# Clinical Text API
A service that extracts structured information from clinical text.
(Work in progress — built as part of my MLE transition plan.)

## Dev setup: run .\venv\Scripts\Activate before working

## Development
- Create venv: python -m venv venv
- Install: pip install -r requirements.txt
- Run tests: pytest
- Check style: ruff check .

## TDD Test-Driven Development
Write the test first, for a function that doesn't exist yet. then build the function to make the test pass. So Test -> Red -> Green

## Run the server
uvicorn src.main:app --reload
http://127.0.0.1:8000 #Here check server status
http://127.0.0.1:8000/docs #FastAPI auto-generated interactive documentation for your API. Click around. This page is my best friend for the next 5 weeks.
