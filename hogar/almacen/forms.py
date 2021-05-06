from django import forms
from .models import Almacen, ProductoTipo, Posicion, Marca
from crispy_forms.helper import FormHelper
from dal import autocomplete
from crispy_forms.layout import Layout, Row, Column, Field


class ProductForm(forms.ModelForm):
    ubicacion = forms.ModelChoiceField(
        queryset=Posicion.objects.all(),
        widget=autocomplete.ModelSelect2(url='almacen:ac_ubicacion', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )





    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
    )

    tipo = forms.ModelChoiceField(
        queryset=ProductoTipo.objects.all(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False



    class Meta:
        model = Almacen
        fields = ('nombre', 'marca', 'ubicacion', 'tipo', 'cantidad', 'photo')


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class PosicionForm(forms.ModelForm):
    class Meta:
        model = Posicion
        fields = ('nombre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class ProductTipoForm(forms.ModelForm):
    class Meta:
        model = ProductoTipo
        fields = ('nombre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
