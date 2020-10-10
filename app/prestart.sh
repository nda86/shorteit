#! /usr/bin/env bash
# shellcheck disable=SC2164
cd /app
python manage.py makemigrations
sleep 2
python manage.py migrate --no-input
sleep 2
python manage.py collectstatic --no-input
sleep 2
