from django.db import models

import os
import uuid
import datetime
from django.utils.crypto import get_random_string
from tienda.models import Producto


def generate_uuid():
    return uuid.uuid4().hex[:10]


def get_RandomString():
    return get_random_string(7, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')

class Order(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=10, default=get_RandomString, unique=True, blank=True)
    date = models.DateField(null=True,blank=True, auto_now_add=True)

    def __str__(self):
        return self.id.__str__()


class Cart(models.Model):
    class State(models.TextChoices):
        Iniciado = 0
        Acabado = 1

    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=15)
    slug = models.SlugField(max_length=10, default=get_RandomString, unique=True, blank=True)
    state = models.IntegerField(choices=State.choices, default=State.Iniciado)
    products = models.ManyToManyField(Producto, through='Compras', null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)

    # producto = models.ManyToManyField(Tags)

    def __str__(self):
        return self.id.__str__()


class Compras(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, max_length=15)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, max_length=15)
    cantidad = models.IntegerField(null=True, blank=True)


class ListaDeseos(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=5, default=get_RandomString, unique=True, blank=True)
    products = models.ManyToManyField(Producto)
    usuario = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.id.__str__()