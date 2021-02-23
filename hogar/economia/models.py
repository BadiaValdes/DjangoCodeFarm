import uuid

from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.crypto import get_random_string


def generate_uuid():
    return uuid.uuid4().hex


def get_RandomString():
    return get_random_string(11, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')


class Tipo_OP(models.Model):
    class Tipo(models.TextChoices):
        ENTRADA = "Entrada"
        SALIDA = "Salida"

    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    nombre = models.CharField(max_length=20)
    des = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, null=True, blank=True)
    slug = models.SlugField(max_length=11, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre


class Salario(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    amount = models.FloatField(max_length=10)
    fecha_deposito = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=11, default=get_RandomString, unique=True, blank=True)
    # fk
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        name_to_show = self.amount.__str__() + ' / ' + self.fecha_deposito.__str__()
        return name_to_show

    def cantidad(self):
        return self.amount.__str__()


class Operaciones(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    slug = models.SlugField(max_length=11, default=get_RandomString, unique=True, blank=True)
    fecha_operacion = models.DateField(default=timezone.now)
    des = models.CharField(max_length=100)
    amount = models.FloatField(max_length=10)
    # fk
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE, null=False)
    tipo_op = models.ForeignKey(Tipo_OP, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.amount.__str__()


class Deudas(models.Model):
    class State(models.TextChoices):
        LIQUIDADA = "Liquidada"
        PENDIENTE = "Pendiente"

    class Tipo(models.TextChoices):
        PRESTAMO = "PRESTAMOS"
        DEUDAS = "DEUDAS"

    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=40)
    slug = models.SlugField(max_length=11, default=get_RandomString, unique=True, blank=True)
    estado = models.CharField(max_length=20, choices=State.choices, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, null=True, blank=True)
    amount = models.FloatField(max_length=10)
    fecha_operacion = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField(default=timezone.now, null=True, blank=True)
    des = models.CharField(max_length=100)
    #fk
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.amount
