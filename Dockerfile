FROM python:3.6-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY service.py .

COPY app /app

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
