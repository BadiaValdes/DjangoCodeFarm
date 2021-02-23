from django.db import models
import uuid
import requests
from django.conf import settings
from datetime import date
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.apps import apps

# Create your models here.

def generate_uuid():
    return uuid.uuid4().hex

def get_RandomString():
    return get_random_string(40,'0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')


class Posicion(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    #user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class ProductoTipo(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    #user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    #user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Almacen(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    nombre = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField()
    ubicacion = models.ForeignKey(Posicion, on_delete=models.CASCADE, null=False)
    tipo = models.ForeignKey(ProductoTipo, on_delete=models.CASCADE, null=False)
    photo = models.ImageField(upload_to='almacen')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Reportes(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    nombre = models.CharField(max_length=50, default='hola')
    fecha_creacion = models.DateField(default=timezone.now)
    url_change = models.CharField(default=generate_uuid, editable=False, unique=True, max_length=40)
    slug_url = models.SlugField(max_length=40, default=get_RandomString, unique=True, blank=True)
    #file = models.FileField(upload_to='media/pdf_repo', null=True)
    file_path = models.FilePathField(path='media/pdf_repo', null=True)

    def __str__(self):
        return self.nombre
