from django.db import models

from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.conf import settings

import uuid
import os


# for year will be "{1}".format(now.Year())
def get_upload_path(instance, filename):
    return os.path.join("{0}".format(instance.user.id), filename)


def generate_uuid():
    return uuid.uuid4().hex


def generate_uuid_valid():
    uui = generate_uuid()
    if Item.objects.filter(id__contains=uui):
        return generate_uuid()

    return uuid


def get_random_string_fun(num=-1):
        return get_random_string(11, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM-')


def get_random_string_name():
    return get_random_string(5, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM-')


# Create your models here.

class Tipo(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=generate_uuid, editable=False, max_length=40)
    nb = models.CharField(max_length=30)

    def __str__(self):
        return self.nb

class State(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=generate_uuid, editable=False, max_length=40)
    nb = models.CharField(max_length=30)
    tipo = models.ManyToManyField(Tipo)
    icon = models.CharField(max_length=20, null=True, blank=True)


    class Meta:
        ordering = ['nb']

    def __str__(self):
        return self.nb


class Lista(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=generate_uuid, editable=False, max_length=40)
    nb = models.CharField(max_length=30, null=False, default='Lista ' + get_random_string_name(), blank=False)
    slugUrl = models.SlugField(max_length=20, default=get_random_string_fun(11), editable=False, null=False,
                               unique=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nb


class Item(models.Model):

    id = models.CharField(primary_key=True, unique=True, default=generate_uuid, editable=False, max_length=40)
    nb = models.CharField(max_length=40)
    img = models.ImageField(upload_to=get_upload_path)
    list = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nb
