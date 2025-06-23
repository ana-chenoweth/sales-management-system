from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('cajero', 'Cajero'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='cajero')
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.rol = 'admin'
        super().save(*args, **kwargs)