from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
