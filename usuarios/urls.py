from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('lista/', views.lista_usuarios, name='lista'),
    path('registro/', views.registro, name='registro'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
]
