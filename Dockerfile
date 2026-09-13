FROM python:3.11-alpine

WORKDIR /

RUN apk add --no-cache gcc musl-dev libffi-dev
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /publication_system
ENTRYPOINT ["/publication_system/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]