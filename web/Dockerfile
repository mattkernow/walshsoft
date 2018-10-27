FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE walshsoft.settings

RUN mkdir /code
WORKDIR /code/

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD . /code/

EXPOSE 8000

CMD ['gunicorn', 'walshsoft.wsgi:application', '--bind', ':8000']
