############### MODELS IMPORT ###################
from tienda.model_ext.case import TypeCase, SidePanelWindow, PowerSupply, FrontPanelUSB
from tienda.model_ext.gpu import Interface, FrameSync, Cooling, ExternalPower
from tienda.model_ext.cpu import Serie, MicroArch, IntegrateGraphic, CoreFamily
from tienda.model_ext.motherboard import Wireless, Ethernet
from tienda.model_ext.ram import TiemposRAM, ECCRAM
from tienda.model_ext.generales import Manufacturer, TypeProduct, Color, FormFactor, Chipset, TypeMemory, SLI, Socket
from tienda.models import Case, Category, Tags, Shipping, GPU
############### ENDS MODEL IMPORT ###############


############### DAL IMPORT #####################
from dal import autocomplete
############### ENDS DAL IMPORT ################


class CategoryAutoComplete(autocomplete.Select2QuerySetView):
    def create_object(self, text):
        slug = text.lower()
        slug = slug.replace(" ", "_")
        return self.get_queryset().get_or_create(**{self.create_field: text, 'slug': slug})[0]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()
        qs = Category.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class ShippingAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Shipping.objects.none()
        qs = Shipping.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class TagsAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tags.objects.none()
        qs = Tags.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class ManufacturerAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Manufacturer.objects.none()
        # tp = TypeProduct.objects.get(nombre__exact='GPU')
        # qs = Manufacturer.objects.filter(type__id=tp.id)
        qs = Manufacturer.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class TypeCaseAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return TypeCase.objects.none()
        qs = TypeCase.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class PowerSupplyAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return PowerSupply.objects.none()
        qs = PowerSupply.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class SidePanelWindowAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SidePanelWindow.objects.none()
        qs = SidePanelWindow.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class FrontPanelUSBAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return FrontPanelUSB.objects.none()
        qs = FrontPanelUSB.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class ColorAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Color.objects.none()
        qs = Color.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs


class FormFactorAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return FormFactor.objects.none()
        qs = FormFactor.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class ChipsetAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Chipset.objects.none()
        qs = Chipset.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class TypeMemoryAutoComplete(autocomplete.Select2QuerySetView):
    def create_object(self, text):
        slug = text.lower()
        slug = slug.replace(" ", "_")
        return self.get_queryset().get_or_create(**{self.create_field: text, 'slug': slug})[0]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return TypeMemory.objects.none()
        qs = TypeMemory.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class InterfaceAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Interface.objects.none()
        qs = Interface.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class FrameSyncAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return FrameSync.objects.none()
        qs = FrameSync.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class SLIAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SLI.objects.none()
        qs = SLI.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class CoolingAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Cooling.objects.none()
        qs = Cooling.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class ExternalPowerAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return ExternalPower.objects.none()
        qs = ExternalPower.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class SerieAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Serie.objects.none()
        qs = Serie.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class MicroArchAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return MicroArch.objects.none()
        qs = MicroArch.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class IntegrateGraphicAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return IntegrateGraphic.objects.none()
        qs = IntegrateGraphic.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class CoreFamilyAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CoreFamily.objects.none()
        qs = CoreFamily.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class SocketAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Socket.objects.none()
        qs = Socket.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class EthernetAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Ethernet.objects.none()
        qs = Ethernet.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class WirelessAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Wireless.objects.none()
        qs = Wireless.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class TiemposRAMAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return TiemposRAM.objects.none()
        qs = TiemposRAM.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs

class ECCAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return ECCRAM.objects.none()
        qs = ECCRAM.objects.all()
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        return qs