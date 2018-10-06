FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
