from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('nueva/', views.nueva_venta, name='nueva'),
    path('detalle/<int:id>/', views.detalle_venta, name='detalle'),

]
