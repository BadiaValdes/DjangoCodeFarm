import os
import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string


def generate_uuid():
    return uuid.uuid4().hex


def get_RandomString():
    return get_random_string(40, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')

class Size(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    size = models.IntegerField(blank=False, null=False, default=333, verbose_name="Tamaño mm")
    slug = models.SlugField(max_length=20, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.size + "mm"

class LED(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre

class Connector(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre

class Controller(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre
