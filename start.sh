#!/bin/sh

# Run FastAPI
uv run uvicorn src.app:app --host 0.0.0.0 --port 80 --reload &

# Run Streamlit
uv run streamlit run src/main.py
