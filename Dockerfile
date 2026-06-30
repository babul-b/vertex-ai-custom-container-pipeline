FROM python:3.10-slim

WORKDIR /app

COPY src/deploy.py deploy.py

ENTRYPOINT ["python"]
