from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Almacen, Marca, ProductoTipo, Posicion, Reportes
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ProductForm, MarcaForm, ProductTipoForm, PosicionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from .print import MyFirstPrint
from io import BytesIO
from django.core.files import File
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from django.utils.timezone import now


#from celery.schedules import crontab
#from celery.task import periodic_task
#from celery import task

import os


# Create your views here.


# Otros
@login_required
def index(request):
    # notify.send(request.user, recipient=request.user, verb='The items  have been deleted by {}'.format(request.user.username), level='info')
    if request.user is not None:
        if request.POST:
            producto = searchTipeSelector(request.POST['search_type'], request.user, request.POST['search'])
            search = True
            search_type = request.POST['search_type']
            search_text = request.POST['search']
        else:
            producto = Almacen.objects.filter(user__id=request.user.id)
            search = False
            search_type = False
            search_text = False
        context = {'producto': producto, 'search': search, 'user': request.user, 'search_type': search_type,
                   'search_text': search_text}
        return render(request, '../templates/almacen/index.html', context)
    else:
        return HttpResponse('Not user found')

#@task()
def pdf_gen():
    marca = Marca.objects.all()
    html_string = render_to_string('pdf_template/marca.html', {'marca': marca})
    html = HTML(string=html_string)
    filename = 'marca_reporte_' + date.today().strftime("%d-%m-%Y")
    # change to an absolute uri for local change
    # keep it in temp for only download option
    name = '{0}.pdf'.format(filename)
    #uri = 'media/pdf_repo/' + name
    try:
        os.mkdir( os.path.join(settings.MEDIA_ROOT, 'pdf_repo', '{0}'.format(now().year)))
    except:
        pass
    uri = 'media/pdf_repo/{0}/{1}'.format(now().year, name)
    html.write_pdf(target=uri, stylesheets=[CSS('static/css/w3.css')]);
    # f = open(j)
    # myFile = File(f)
    Reportes.objects.create(nombre=filename, fecha_creacion=date.today().strftime("%Y-%m-%d"), file_path=uri)
    # Reportes.objects.create('marca_reporte' , date.today(), 'marca_reporte_17-12-2020.pdf')
    # html.HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(target='/tmp/mypdf.pdf')
    # html.HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(target='/tmp/mypdf.pdf')
    # fs = FileSystemStorage('./media/pdf_repo/')
    # with fs.open('mypdf.pdf') as pdf:
    #    response = HttpResponse(pdf, content_type='application/pdf')
    #   response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    #  return response
    return True




def searchTipeSelector(search_type, user, search):
    if search_type == 'all':
        return Almacen.objects.filter(user__id=user.id)
    elif search_type == 'marca':
        marca = Marca.objects.filter(nombre__contains=search).first()
        if marca is not None:
            return Almacen.objects.filter(marca=marca.id, user__id=user.id)
        else:
            return None
    elif search_type == 'tipo':
        pt = ProductoTipo.objects.filter(nombre__contains=search).first()
        if pt is not None:
            return Almacen.objects.filter(tipo=pt.id, user__id=user.id)
        else:
            return None
    elif search_type == 'ubicacion':
        ps = Posicion.objects.filter(nombre__contains=search).first()
        if ps is not None:
            return Almacen.objects.filter(ubicacion=ps.id, user__id=user.id)
        else:
            return None
