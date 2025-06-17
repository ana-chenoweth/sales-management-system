from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, DetalleVenta
from .forms import DetalleVentaForm
from productos.models import Producto
from clientes.models import Cliente

def nueva_venta(request):
    if request.method == 'POST':
        forms_data = []
        total = 0

        for i in range(0, int(request.POST.get('form-TOTAL_FORMS'))):
            producto_id = request.POST.get(f'form-{i}-producto')
            cantidad = int(request.POST.get(f'form-{i}-cantidad'))

            producto = Producto.objects.get(id=producto_id)
            subtotal = producto.precio * cantidad
            total += subtotal
            forms_data.append((producto, cantidad, producto.precio))

        venta = Venta.objects.create(total=total)
        for producto, cantidad, precio in forms_data:
            DetalleVenta.objects.create(venta=venta, producto=producto, cantidad=cantidad, precio_unitario=precio)
            producto.stock -= cantidad
            producto.save()

        return redirect('ventas:detalle', venta.id)

    else:
        form = DetalleVentaForm()
        return render(request, 'ventas/nueva.html', {'form': form})

def detalle_venta(request, id):
    venta = Venta.objects.get(id=id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'ventas/detalle.html', {
        'venta': venta,
        'detalles': detalles
    })