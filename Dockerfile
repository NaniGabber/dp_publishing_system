FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache gcc g++ musl-dev libffi-dev tzdata musl-locales \
    git curl zip unzip tar build-base


ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY . .

WORKDIR /app/publishing_system

ENTRYPOINT ["sh", "/app/publishing_system/entrypoint.sh"]