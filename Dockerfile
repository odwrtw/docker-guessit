FROM python:3.11.3-alpine3.17

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "python", "./app.py" ]
