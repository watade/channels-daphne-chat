FROM python:3.12-slim-bullseye as builder
WORKDIR /usr/src/app
ENV PIPENV_VENV_IN_PROJECT=1
COPY Pipfile ./
RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv sync --dev --system

FROM python:3.12-slim-bullseye
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /usr/src/app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages/
