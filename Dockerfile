FROM python:3.8.5
MAINTAINER Artem Yurchak (nemnovus@gmail.com)
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/myhome24
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .