"""hogar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from . import views
from .views2 import marca
from .views2 import producto_tipo
from .views2 import ubicacion
from .views2 import reporte
from .views2 import producto
from django.conf import settings
from django.conf.urls.static import static

app_name = 'almacen'

urlpatterns = [
                  path('', views.index, name='index'),

                  # Producto
                  re_path('eliminar/(?P<pk>[0-9a-f]{32})', producto.DeleteProductoView.as_view(), name='delete'),
                  re_path('modificar/(?P<pk>[0-9a-f]{32})', producto.UpdateProductoView.as_view(), name='update'),
                  path('elim/', producto.eliminar, name='del'),
                  path('adicionar/', producto.CreateProductoView.as_view(), name='add'),

                  # Marcar
                  path('marca/', marca.MarcaListView.as_view(), name='marca_list'),
                  path('marca/delete/', marca.MarcaEliminar, name='marca_del'),
                  path('marca/add/', marca.CreateMarcaView.as_view(), name='marca_add'),
                  re_path('marca/del/(?P<pk>[0-9a-f]{32})', marca.DeleteMarcaView.as_view(), name='marca_delete'),
                  re_path('marca/update/(?P<pk>[0-9a-f]{32})', marca.UpdateMarcaView.as_view(), name='marca_update'),

                  # Producto_Tipo
                  re_path('producto_tipo/del/(?P<pk>[0-9a-f]{32})', producto_tipo.DeleteProductoTipoView.as_view(),
                          name='producto_tipo_delete'),
                  re_path('producto_tipo/update/(?P<pk>[0-9a-f]{32})', producto_tipo.UpdateProductoTipoView.as_view(),
                          name='producto_tipo_update'),
                  path('producto_tipo/', producto_tipo.ProductoTipoListView.as_view(), name='producto_tipo_list'),
                  path('producto_tipo/del/', producto_tipo.eliminar, name='producto_tipo_del'),
                  path('producto_tipo/add/', producto_tipo.CreateProductoTipoView.as_view(), name='producto_tipo_add'),

                  # Ubicacion
                  re_path('ubicacion/del/(?P<pk>[0-9a-f]{32})', ubicacion.DeleteUbicacionView.as_view(),
                          name='ubicacion_delete'),
                  re_path('ubicacion/update/(?P<pk>[0-9a-f]{32})', ubicacion.UpdateUbicacionView.as_view(),
                          name='ubicacion_update'),
                  path('ubicacion/', ubicacion.UbicacionListView.as_view(), name='ubicacion_list'),
                  path('ubicacion/del/', ubicacion.UbicacionEliminar, name='ubicacion_del'),
                  path('ubicacion/add/', ubicacion.CreateUbicacionView.as_view(), name='ubicacion_add'),
                  re_path('ubicacionAutoComplete/', ubicacion.UbicacionAutoComplete.as_view(create_field='nombre'), name="ac_ubicacion"),

                  # Reporte
                  path('reporte/marca/', reporte.marca_datos, name='report_marca'),
                  path('reporte/', reporte.ReportListView.as_view(), name='reporte_list'),
                  path('reporte/<slug:slug>', reporte.ReporteResponse,
                       name='reporte_response'),
                  path('reporte/descargar/<slug:slug>', reporte.ReporteDescarga,
                       name='reporte_download'),
                  path('reporte/marca2/', reporte.html_to_pdf_view, name='report_marca2'),
                  path('reporte/del/', reporte.ReporteEliminar, name='reporte_del'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
