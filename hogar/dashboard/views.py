from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from hogar.economia.models import Operaciones, Deudas, Salario
from economia.models import Operaciones, Deudas, Salario
# from .models import Almacen, Marca, ProductoTipo, Posicion, Reportes
from django.http import HttpResponse, HttpResponseRedirect
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your views here.

@login_required
def index(request):
    if request.user is not None:
        salida = Operaciones.objects.filter(tipo_op__tipo='Salida').count()
        entrada = Operaciones.objects.filter(tipo_op__tipo='Entrada').count()
        deudas = Deudas.objects.filter(tipo__exact='DEUDAS').count()
        prestamos = Deudas.objects.filter(tipo__exact='PRESTAMOS').count()
        deudas_liquidadas = Deudas.objects.filter(estado__iexact='Liquidada').count()
        deudas_pendientes = Deudas.objects.filter(estado__iexact='Pendiente').count()
        salario = Salario.objects.all()

        context = {
            'salida': salida,
            'entrada': entrada,
            'deudas': deudas,
            'prestamos': prestamos,
            'deudas_liquidadas': deudas_liquidadas,
            'deudas_pendientes': deudas_pendientes,
            'salario': salario,
        }

        #channel_layer = get_channel_layer()
        #async_to_sync(channel_layer.group_send)("dashboard", {"type": "chat_message", "value": "0"})

        return render(request, '../templates/dashboard/index.html', context)

    else:
        return HttpResponse('Not user found')
