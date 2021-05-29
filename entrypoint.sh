#! /bin/bash
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
python3 manage.py runserver 0.0.0.0:8000
#exec gunicorn myhome24.wsgi:application --bind 0.0.0.0:8000