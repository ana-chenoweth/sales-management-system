from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('nueva/', views.nueva_venta, name='nueva'),
    path('detalle/<int:id>/', views.detalle_venta, name='detalle'),
    path('pdf/<int:id>/', views.venta_pdf, name='pdf'),
    path('csv/<int:id>/', views.venta_csv, name='csv'),
    path('', views.historial_ventas, name='historial'),
]
