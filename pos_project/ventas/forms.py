from django import forms
from .models import Venta, DetalleVenta
from productos.models import Producto

class DetalleVentaForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label="Producto")
    cantidad = forms.IntegerField(min_value=1, label="Cantidad")
