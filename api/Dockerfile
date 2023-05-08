FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install -U pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main

COPY . .

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
