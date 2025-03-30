FROM python:3.12.9-alpine3.21

RUN apk update && apk add --no-cache git postgresql gcc musl-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app/app/server.py

EXPOSE 8080

CMD ["sh", "-c", "pwd && echo '========' && ls -l && echo '==========' && ls -l ./app && python ./app/server.py"]