#pull offical base image
FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update

RUN apt-get install python3-dev build-essential -y

#pip requirements

RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv venv

ENV PATH="/venv/bin:$PATH"

RUN pip install django


COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


COPY . /srv/app
WORKDIR /srv/app

