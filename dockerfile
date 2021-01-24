FROM python:3.9

COPY ./src /usr/src/myapp
WORKDIR /usr/src/myapp

EXPOSE 8000
RUN pip install django


ENTRYPOINT ["python"]
CMD ["manage.py","runserver","0.0.0.0:8000"]
