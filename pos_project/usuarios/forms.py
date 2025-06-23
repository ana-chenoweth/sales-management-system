from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuario

class RegistroUsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol']
