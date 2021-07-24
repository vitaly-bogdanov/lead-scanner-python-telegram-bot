FROM python:3.8.6

WORKDIR /src
COPY Requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src