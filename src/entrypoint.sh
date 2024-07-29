#!/usr/bin/env sh

set -e

pdm install

pdm run python manage.py migrate

pdm run python manage.py runserver 0.0.0.0:8000
