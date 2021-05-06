import os
import uuid

from reportlab.platypus.doctemplate import onDrawStr
from tienda.model_ext.motherboard import MemoryType, Ethernet, Wireless
from tienda.model_ext.cpu import Serie, MicroArch, CoreFamily, IntegrateGraphic
from tienda.model_ext.ram import TiemposRAM, ECCRAM
from tienda.model_ext.gpu import Interface, FrameSync, Cooling, ExternalPower
from tienda.model_ext.case import TypeCase, PowerSupply, SidePanelWindow, FrontPanelUSB
from tienda.model_ext.caseFan import Size, LED, Connector, Controller
from tienda.model_ext.generales import Socket, SLI, TypeProduct, TypeMemory, Manufacturer, FormFactor, Chipset, Color
from django.utils.text import slugify

from django.contrib.postgres.fields import ArrayField

from django.db import models

# Create your models here.

from django.utils.crypto import get_random_string


def get_upload_path(instance, filename):
    return os.path.join("{0}".format(instance.category.nombre), filename)


def generate_uuid():
    return uuid.uuid4().hex[:10]


def get_RandomString():
    return get_random_string(7, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')


def get_name_slug(instance):
    return slugify(instance.nombre)


class Tags(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Shipping(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20)
    precio = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.nombre


class Category(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, default=get_RandomString, unique=True, blank=True)
    photo = models.ImageField(upload_to='category/', default='category/18.jpg')

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=10, default=get_RandomString, unique=True, blank=True)
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    precio = models.FloatField(null=False, blank=False)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    descuento = models.FloatField(default=0, null=False, blank=False,
                                  help_text="Descuento en 0, no tiene")
    photo = models.ImageField(upload_to=get_upload_path)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, null=False)
    available = models.BooleanField(default=True, null=False, blank=False, verbose_name="Disponible")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, verbose_name="Compañía")

    def __str__(self):
        return self.nombre

    def precioFinal(self):
        return self.precio - (
                self.precio * self.descuento) + self.shipping.precio if self.descuento != 0 else self.precio + self.shipping.precio

    def precioDescuento(self):
        return self.precio - (self.precio * self.descuento / 100) if self.descuento != 0 else self.precio

    def Tags(self):
        tags_array = ""
        for t in self.tags.all():
            tags_array += t.nombre + "/"
        return tags_array


class ListaCompra(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=10, default=get_RandomString, unique=True, blank=True)

    # producto = models.ManyToManyField(Tags)

    def __str__(self):
        return self.nombre


class ListaDeseos(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    nombre = models.CharField(max_length=20)
    slug = models.SlugField(max_length=5, default=get_RandomString, unique=True, blank=True)

    def __str__(self):
        return self.nombre


class MotherBoard(Producto):
    socket = models.ForeignKey(Socket, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Socket")
    chipset = models.ForeignKey(Chipset, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Chipset")
    form_Factor = models.ForeignKey(FormFactor, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name="Tamaño")
    maxMemory = models.IntegerField(null=False, blank=False, default=2, verbose_name="Memoria RAM máxima")
    memoryType = models.ForeignKey(MemoryType, on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name="Tipo de RAM")
    memorySlot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores de RAM")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Color")
    sli = models.ForeignKey(SLI, on_delete=models.CASCADE, null=False, blank=False, verbose_name="CrossFire / SLI")
    pciX16Slot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores PCI x16")
    pciX8Slot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores PCI x8")
    pciX4Slot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores PCI x4")
    pciX1Slot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores PCI x1")
    pciSlot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores PCI")
    sata3Port = models.IntegerField(null=False, blank=False, default=2, verbose_name="Puertos SATA 3GB/s")
    sata6Port = models.IntegerField(null=False, blank=False, default=2, verbose_name="Puertos SATA 6GB/s")
    m2Slot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores M2")
    mSataSlot = models.IntegerField(null=False, blank=False, default=2, verbose_name="Conectores M2Sata")
    ethernet = models.ForeignKey(Ethernet, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Red")
    wireless = models.ForeignKey(Wireless, on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name="Conexión Inalámbrica")
    boarVideo = models.BooleanField(default=False, null=False, blank=False, verbose_name="Video en Board")
    suportECC = models.BooleanField(default=False, null=False, blank=False, verbose_name="Soporte para ECC")


class CPU(Producto):
    socket = models.ForeignKey(Socket, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Socket")
    coreCount = models.IntegerField(null=False, blank=False, default=1, verbose_name="Nucleos")
    coreClok = models.FloatField(null=False, blank=False, default=1.1, verbose_name="Frecuencia")
    tdp = models.IntegerField(null=False, blank=False, default=10, verbose_name="Potencia Electrica")
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Serie")
    microArch = models.ForeignKey(MicroArch, on_delete=models.CASCADE, null=False, blank=False,
                                  verbose_name="Micro Arquitectura")
    coreFamy = models.ForeignKey(CoreFamily, on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name="Generacion")
    graphics = models.ForeignKey(IntegrateGraphic, on_delete=models.CASCADE, null=False, blank=True,
                                 verbose_name="Tarjeta Gráfica Integrada")
    suportECC = models.BooleanField(default=False, null=False, blank=False, verbose_name="Soporte para ECC")


class RAM(Producto):
    form_Factor = models.ForeignKey(FormFactor, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name="Dimensiones")
    type = models.ForeignKey(TypeMemory, on_delete=models.CASCADE, null=False, blank=False,
                             verbose_name="Tipo")
    speed = models.IntegerField(blank=False, null=False, default=0, verbose_name="Velocidad en Mhz")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Color")
    latency = models.FloatField(blank=False, null=False, default=5.625, verbose_name="Latencia en ns")
    voltage = models.FloatField(blank=False, null=False, default=1.2, verbose_name="Voltaje en v")
    timing = models.ForeignKey(TiemposRAM, on_delete=models.CASCADE, null=False, blank=False,
                               verbose_name="Tiempos")
    ecc = models.ForeignKey(ECCRAM, on_delete=models.CASCADE, null=False, blank=False,
                            verbose_name="Color")
    heatSpreader = models.BooleanField(default=False, null=False, blank=False, verbose_name="Dicipador")


class GPU(Producto):
    chipset = models.ForeignKey(Chipset, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Chipset")

    type = models.ForeignKey(TypeMemory, on_delete=models.CASCADE, null=False, blank=False,
                             verbose_name="Tipo")
    core_clock = models.IntegerField(blank=False, null=False, default=0, verbose_name="Velocidad en Mhz")
    boost_clock = models.IntegerField(blank=False, null=False, default=0, verbose_name="Velocidad con OverClock en Mhz")
    inteface = models.ForeignKey(Interface, on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name="Interfaz")
    frame_sync = models.ForeignKey(FrameSync, on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name="Interfaz")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Color")
    sli = models.ForeignKey(SLI, on_delete=models.CASCADE, null=False, blank=False, verbose_name="CrossFire / SLI")
    length = models.IntegerField(blank=False, null=False, default=333, verbose_name="Tamaño mm")
    tdp = models.IntegerField(null=False, blank=False, default=10, verbose_name="Potencia Electrica")
    dvi_port = models.IntegerField(null=False, blank=False, default=10, verbose_name="Puertos DVI")
    hdmi_port = models.IntegerField(null=False, blank=False, default=10, verbose_name="Puertos HDMI")
    display_port = models.IntegerField(null=False, blank=False, default=10, verbose_name="Puertos DisplayPort")
    mini_display_port = models.IntegerField(null=False, blank=False, default=10,
                                            verbose_name="Puertos MIni-DisplayPort")
    expansion_width = models.IntegerField(null=False, blank=False, default=10,
                                          verbose_name="Ancho del conector de expansión")
    cooling = models.ForeignKey(Cooling, on_delete=models.CASCADE, null=False, blank=False,
                                verbose_name="Enfrieamiento")
    external_power = models.ForeignKey(ExternalPower, on_delete=models.CASCADE, null=False, blank=False,
                                       verbose_name="Fuente de alimentación")


class Case(Producto):
    type_case = models.ForeignKey(TypeCase, on_delete=models.CASCADE, null=False, blank=False,
                                  verbose_name="Tipo de Chacis")
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, null=False, blank=False,
                                     verbose_name="Capacidad de la fuente")
    side_panel_window = models.ForeignKey(SidePanelWindow, on_delete=models.CASCADE, null=False, blank=False,
                                          verbose_name="Tipo de panel lateral")
    front_panel_USB = models.ForeignKey(FrontPanelUSB, on_delete=models.CASCADE, null=False, blank=False,
                                        verbose_name="Front Panel USB")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Color")
    formFactor = models.ForeignKey(FormFactor, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Tamaño")
    external_bays_5 = models.IntegerField(blank=False, null=False, default=0,
                                          verbose_name="Baías externas de 5.25 pulgadas")
    external_bays_3 = models.IntegerField(blank=False, null=False, default=0,
                                          verbose_name="Baías externas de 3.5 pulgadas")
    internal_bays_3 = models.IntegerField(blank=False, null=False, default=0,
                                          verbose_name="Baías internas de 3.5 pulgadas")
    internal_bays_2 = models.IntegerField(blank=False, null=False, default=0,
                                          verbose_name="Baías internas de 2.5 pulgadas")
    full_h_expansion_slot = models.IntegerField(blank=False, null=False, default=0,
                                                verbose_name="Conectores de expansión de tamaño completo")
    half_h_expansion_slot = models.IntegerField(blank=False, null=False, default=0,
                                                verbose_name="Conectores de expansión de tamaño medio")


class CaseFan(Producto):
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Tamaño en mm")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Color")
    quantity = models.IntegerField(null=True, blank=True, default=0, verbose_name="Cantidad de Fans")
    pwm = models.BooleanField(default=False)
    led = models.ForeignKey(LED, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Color de los led")
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE, null=False, blank=False,
                                  verbose_name="Tipo de conector")
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name="Tipo de controlador")
