FROM python:3.11-slim

# Configure the working directory
WORKDIR /app
RUN mkdir /app/src

# Copy the necessary files
COPY src/app.py /app/src/app.py
COPY src/config.py /app/src/config.py
COPY src/routers.py /app/src/routers.py
COPY src/schemas.py /app/src/schemas.py
COPY src/utils.py /app/src/utils.py

# Configure poetry-related files and install the dependencies 
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.in-project true
RUN poetry install --with fastapi

# Expose port 80
EXPOSE 80

# Launch the api server at port 80
CMD ["poetry", "run",  "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]