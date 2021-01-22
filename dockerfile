FROM python:3.8

COPY ./src /usr/src/myapp
WORKDIR /usr/src/myapp


RUN pip install django

ENTRYPOINT ["python"]
CMD ["manage.py runserver 0.0.0.0:8000"]


