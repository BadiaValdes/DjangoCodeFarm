############### MODELS IMPORT ###################
from tienda.model_ext.case import TypeCase, SidePanelWindow, PowerSupply, FrontPanelUSB
from tienda.model_ext.gpu import Interface, FrameSync, Cooling, ExternalPower
from tienda.model_ext.generales import Manufacturer, TypeProduct, Color, FormFactor, Chipset, TypeMemory, SLI
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