from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import RegistroUsuarioForm
from .forms import UsuarioEditForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PerfilForm
from django.contrib.auth import update_session_auth_hash


def es_admin(user):
    return user.is_authenticated and user.rol == 'admin'

@user_passes_test(es_admin)
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

@login_required(login_url='/login/')
@user_passes_test(es_admin, login_url='/login/')
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'formulario.html', {'form': form, 'editar': True})

@login_required(login_url='/login/')
@user_passes_test(es_admin, login_url='/login/')
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista')
    return render(request, 'usuarios/confirmar_eliminar.html', {'usuario': usuario})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = CambiarPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('inicio')
    else:
        form = CambiarPasswordForm(user=request.user)
    return render(request, 'usuarios/cambiar_contrasena.html', {'form': form})