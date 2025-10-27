FROM python:3.12-slim


RUN apt-get update && apt-get install -y build-essential libpq-dev


RUN pip install poetry


WORKDIR /app
COPY pyproject.toml poetry.lock* ./


RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi


COPY . .


ENV PYTHONUNBUFFERED=1


CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]