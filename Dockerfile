FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]  # Or whatever your entrypoint is
