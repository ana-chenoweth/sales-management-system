from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'rol', 'foto')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'foto']

class CambiarPasswordForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']

class UsuarioEditForm(UserChangeForm):
    password = None  # ocultar campo password (opcional)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'foto']