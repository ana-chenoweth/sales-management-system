from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('gerente/', views.dashboard_gerente, name='dashboard_gerente'),
    path('cajero/', views.dashboard_cajero, name='dashboard_cajero'),
]
