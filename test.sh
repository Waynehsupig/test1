#!/bin/bash

docker run -itd \
--name python3_venv \
-v $PWD/src:/usr/src/myapp \
-w /usr/src/myapp \
-p 8000:8000 \
python:3


docker exec -it python3_venv pip install django
docker exec -it python3_venv python manage.py runserver 0.0.0.0:8000


exit 0
