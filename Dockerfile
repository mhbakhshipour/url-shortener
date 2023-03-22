FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /url_shortener
WORKDIR /url_shortener
COPY requirements.txt /url_shortener/
RUN pip install -r requirements.txt
COPY . /url_shortener/
