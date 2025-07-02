#!/usr/bin/env bash

# Exit on error
set -o errexit

# Instala dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Aplica migraciones
python manage.py migrate --noinput

# Recolecta archivos estáticos
python manage.py collectstatic --noinput
