from django.urls import path
from . import views 

app_name = 'productos'

urlpatterns = [
    path('', views.producto_listar, name='listar'),
    path('crear/', views.producto_crear, name='crear'),
    path('editar/<int:id>/', views.producto_editar, name='editar'),
    path('eliminar/<int:id>/', views.producto_eliminar, name='eliminar'),
]
