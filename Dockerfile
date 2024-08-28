FROM python:3.12.5-alpine3.20

COPY requirements.txt ./
RUN apk add curl && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .
HEALTHCHECK CMD curl http://127.0.0.1:5000/guess/healthcheck

EXPOSE 5000
CMD [ "python", "./app.py" ]
