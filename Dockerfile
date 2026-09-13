FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache gcc g++ musl-dev libffi-dev tzdata musl-locales \
    git curl zip unzip tar build-base


ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/publication_system

ENTRYPOINT ["sh", "/app/publication_system/entrypoint.sh"]