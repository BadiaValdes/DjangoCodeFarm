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
from .views2 import tpop, operacion, salario, deudas

app_name = "economia"

urlpatterns = [
    path('', views.index, name='index'),

    # tpop
    path('tpop/', tpop.CreateTPOP.as_view(), name='create_tpop'),

    # operacion
    path('operacion/add', operacion.CreateOperacion.as_view(), name='create_op'),
    path('operacion/', operacion.OperacionList.as_view(), name='list_op'),

    # salario
    path('salario/add/', salario.CreateSalario.as_view(), name='create_salario'),
    path('salario/', salario.SalarioList.as_view(), name='list_salario'),
    re_path('salario/(?P<pk>[0-9a-f]{32})', salario.SalarioDetailView.as_view(), name='salario_details'),
    path('salario/elim/', salario.SalarioEliminar, name='del'),

    # deudas
    path('deuda/add', deudas.CreateDeuda.as_view(), name='create_deuda'),
    path('deuda/', deudas.DeudasList.as_view(), name='list_deudas')
]
