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

# Crea superusuario 
python - << 'EOF'
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
django.setup()
from django.db import connection
from django.contrib.auth import get_user_model

# Asegúrate de que la tabla exista
if 'workmates_workmateuser' in connection.introspection.table_names():
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    if username and not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email or '', password)
        print("Superusuario creado:", username)
else:
    print("Tabla workmates_workmateuser no existe aún. No se creó superusuario.")
EOF