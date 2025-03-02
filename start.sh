#!/bin/sh

# Run FastAPI
uv run uvicorn src.korean_num.app:app --host 0.0.0.0 --port 80 --reload &

# Run Streamlit
uv run streamlit run src/korean_num/main.py