from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Almacen, Marca, ProductoTipo, Posicion, Reportes
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from ..print import MyFirstPrint
from io import BytesIO
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.utils.timezone import now
from django.conf import settings

import os


# Report
class ReportListView(LoginRequiredMixin, ListView):
    model = Reportes
    template_name = 'almacen/report_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def ReporteEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Reportes.objects.filter(id=dat).delete()
    return redirect('/almacen/reporte/')


@login_required
def ReporteResponse(request, slug):
    file = Reportes.objects.filter(slug_url=slug).first()
    context = {'file': file, }
    return render(request, '../templates/almacen/report_view.html', context)


@login_required
def ReporteDescarga(request, slug):
    file = Reportes.objects.filter(slug_url=slug).first()
    # context = {'file': file, }
    fs = FileSystemStorage(file.file_path)
    with fs.open('{0}.pdf'.format(file.nombre)) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}.pdf"'.format(file.nombre)
    return response
    # return render(request, '../templates/almacen/report_view.html', context)


@login_required
def marca_datos(request):
    response = HttpResponse(content_type='application/pdf')
    filename = 'marca_reporte_' + date.today().strftime("%d-%m-%Y")
    response['Content-Disposition'] = 'attachment; filename={0}.pdf'.format(filename)

    buffer = BytesIO()

    report = MyFirstPrint(buffer, 'Letter')
    pdf = report.print()

    response.write(pdf)
    return response


@login_required
def html_to_pdf_view(request):
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

    return redirect('/almacen/reporte/')
