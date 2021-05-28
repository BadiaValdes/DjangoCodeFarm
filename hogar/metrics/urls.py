from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from . import views



urlpatterns = [
path('', views.index, name='hola')
]
