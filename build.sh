#!/usr/bin/env bash
set -o errexit

# Instala dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Aplica migraciones
python manage.py migrate --noinput

# Recolecta archivos estáticos
python manage.py collectstatic --noinput

# Crear superusuario si no existe
python << EOF
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pos_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()
if 'usuarios_usuario' in connection.introspection.table_names():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if username and not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email or '', password=password)
        print(f"✅ Superusuario '{username}' creado.")
    else:
        print("⚠️ Superusuario ya existe o faltan variables.")
else:
    print("⏳ La tabla 'usuarios_usuario' no existe todavía.")
EOF
