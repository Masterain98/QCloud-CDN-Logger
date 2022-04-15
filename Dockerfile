FROM python:3.9.12-slim-buster

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

