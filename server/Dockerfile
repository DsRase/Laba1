FROM python:3.12.9-alpine3.21

RUN apk update && apk add --no-cache git

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 6080

CMD ["python", "server.py"]