#!/bin/bash

ptyhon manage.py makemigrations api --noinput
python manage.py migrate api --noinput
python manage.py collectstatic --noinput
python manage.py create_superuser 
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 xcaret.wsgi:application
