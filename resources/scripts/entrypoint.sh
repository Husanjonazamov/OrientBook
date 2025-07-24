#!/bin/bash

echo "📦 Collectstatic"
python3 manage.py collectstatic --noinput

echo "🧱 Migrate"
python3 manage.py migrate --noinput

# python3 bot.py

echo "🚀 Uvicorn"
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload --reload-dir core --reload-dir config

wait
