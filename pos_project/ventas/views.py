from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, DetalleVenta
from .forms import DetalleVentaForm
from productos.models import Producto
from clientes.models import Cliente
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import tempfile
import csv
from django.http import HttpResponse
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def detalle_venta(request, id):
    venta = Venta.objects.get(id=id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'ventas/detalle.html', {
        'venta': venta,
        'detalles': detalles
    })

def venta_pdf(request, id):
    venta = Venta.objects.get(id=id)
    detalles = DetalleVenta.objects.filter(venta=venta)

    html_string = render_to_string('ventas/pdf_venta.html', {
        'venta': venta,
        'detalles': detalles,
    })

    html = HTML(string=html_string)
    result = tempfile.NamedTemporaryFile(delete=True)
    html.write_pdf(target=result.name)

    with open(result.name, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=venta_{venta.id}.pdf'
    return response

@login_required
def venta_csv(request, id):
    venta = Venta.objects.get(id=id)
    detalles = DetalleVenta.objects.filter(venta=venta)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="venta_{venta.id}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Producto', 'Cantidad', 'Precio Unitario', 'Subtotal'])

    for item in detalles:
        subtotal = item.cantidad * item.precio_unitario
        writer.writerow([item.producto.nombre, item.cantidad, item.precio_unitario, subtotal])

    return response

@login_required
def historial_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha')

    # Filtro por fecha (opcional)
    fecha_inicio = request.GET.get('inicio')
    fecha_fin = request.GET.get('fin')
    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha__range=[fecha_inicio, fecha_fin])

    # Filtro por cliente (opcional si manejas clientes)
    busqueda = request.GET.get('q')
    if busqueda:
        ventas = ventas.filter(Q(id__icontains=busqueda))

    return render(request, 'ventas/historial.html', {
        'ventas': ventas,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'busqueda': busqueda,
    })