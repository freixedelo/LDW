#!/bin/bash
set -e

if [ -f "package.json" ] && [ ! -d "node_modules" ]; then
npm install
fi

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
