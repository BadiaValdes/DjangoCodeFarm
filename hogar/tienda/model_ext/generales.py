import os
import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string


def generate_uuid():
    return uuid.uuid4().hex[:10]


def get_RandomString():
    return get_random_string(20, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')

class SLI (models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre

class TypeMemory (models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre

class Chipset(models.Model):
    class TypeChoice(models.TextChoices):
        MotherBoard = "Motherboard"
        GPU = "GPU"

    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)
    type = models.CharField(max_length=20, choices=TypeChoice.choices, default=TypeChoice.GPU)


    def __str__(self):
        return self.nombre


class Color(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=25, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre


class Socket(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre


class TypeProduct(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre


class FormFactor(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)
    type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, null=True, verbose_name="Compañía")

    def __str__(self):
        return self.nombre


class Manufacturer(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(max_length=23, default=get_RandomString, unique=True, blank=True)
    type = models.ManyToManyField(TypeProduct)

    def __str__(self):
        return self.nombre
