#!/bin/sh
if [ "$DEBUG" = "True" ]; then
    LOG_LEVEL=debug
else
    LOG_LEVEL=info
fi

echo "Waiting for postgres..."

while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn -b 0.0.0.0:8000 config.wsgi:application --log-level=$LOG_LEVEL
