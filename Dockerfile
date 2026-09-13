FROM python:3.11-alpine

WORKDIR /

RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /publication_system

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]