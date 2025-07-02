from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from usuarios.models import Usuario
from productos.models import Producto
from ventas.models import Venta, DetalleVenta
from datetime import timedelta
from django.utils import timezone


def es_admin(user):
    return user.is_authenticated and user.rol == 'admin'

def es_gerente(user):
    return user.is_authenticated and user.rol == 'gerente'

def es_cajero(user):
    return user.is_authenticated and user.rol == 'cajero'


@user_passes_test(es_admin)
def dashboard_admin(request):
    total_usuarios = Usuario.objects.count()
    total_ventas = Venta.objects.count()
    productos_bajos = list(Producto.objects.filter(stock__lt=5).values('nombre', 'stock'))
    return JsonResponse({
        'total_usuarios': total_usuarios,
        'total_ventas': total_ventas,
        'productos_bajos': productos_bajos
    })


@user_passes_test(es_gerente)
def dashboard_gerente(request):
    hoy = timezone.now().date()
    fechas = [str(hoy - timedelta(days=i)) for i in range(6, -1, -1)]
    ventas_por_dia = []
    for f in fechas:
        count = Venta.objects.filter(fecha__date=f).count()
        ventas_por_dia.append(count)

    productos_data = (DetalleVenta.objects
                      .values('producto__nombre')
                      .annotate(total=Sum('cantidad'))
                      .order_by('-total')[:5])
    productos = [p['producto__nombre'] for p in productos_data]
    cantidades = [p['total'] for p in productos_data]

    return JsonResponse({
        'fechas': fechas,
        'ventas': ventas_por_dia,
        'productos': productos,
        'cantidades': cantidades
    })


@user_passes_test(es_cajero)
def dashboard_cajero(request):
    productos = list(Producto.objects.all().values('nombre', 'stock'))
    return JsonResponse({
        'productos': productos
    })
