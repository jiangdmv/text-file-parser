#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --scoket :8000 --master --enable-threads --module ROKTdjangoProject.wsgi




