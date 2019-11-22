#!/bin/sh
set -e

if [ "$DEBUG" = "True" ]; then
    FLAGS="--log-level=debug --reload"
else
    FLAGS="--log-level=info"
fi

echo "Waiting for postgres..."

while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --no-input

gunicorn -b 0.0.0.0:8000 config.wsgi:application $FLAGS
