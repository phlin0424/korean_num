#!/bin/sh

# Run FastAPI
poetry run uvicorn src.app:app --host 0.0.0.0 --port 80 --reload &

# Run Streamlit
poetry run streamlit run src/main.py
