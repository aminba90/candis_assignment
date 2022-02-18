# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster



# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /candis_webapi

COPY ./requirements.txt /candis_webapi/requirements.txt


RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

 CMD [ "python3", "app.py"]