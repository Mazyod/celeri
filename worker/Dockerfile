FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install -U pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main

COPY . .

# entrypoint and cmd to run celery worker
ENTRYPOINT [ "celery" ]
CMD [ "--app", "app.celery_app", "worker", "--queues", "type_a,type_b", "-l", "info" ]
