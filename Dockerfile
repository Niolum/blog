FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /blog

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /blog/
RUN pip install -r requirements.txt

COPY . /blog/
EXPOSE 8000