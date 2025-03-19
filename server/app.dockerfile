FROM python:3.12.9-alpine3.21

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir requirements.txt

COPY server.py .

EXPOSE 6080

CMD ["python", "server.py"]