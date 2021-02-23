import os
from hogar.almacen.models import Marca, Reportes
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from django.utils.timezone import now
from datetime import date

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