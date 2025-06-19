from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.lista_clientes, name='lista'),
    path('nuevo/', views.nuevo_cliente, name='nuevo'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar'),
]
