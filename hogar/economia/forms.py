from django import forms
from .models import Operaciones, Tipo_OP, Salario, Deudas
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from dal import autocomplete
from crispy_forms.layout import Layout, Row, Column, Field


# class ProductForm(forms.ModelForm):
#     ubicacion = forms.ModelChoiceField(
#         queryset=Posicion.objects.all(),
#         widget=autocomplete.ModelSelect2(url='almacen:ac_ubicacion', attrs={
#             # Set some placeholder
#             'data-placeholder': 'Autocomplete ...',
#             # Only trigger autocompletion after 3 characters have been typed
#             'minimumResultsForSearch': 1,
#         }, )
#     )
#
#     marca = forms.ModelChoiceField(
#         queryset=Marca.objects.all(),
#     )
#
#     tipo = forms.ModelChoiceField(
#         queryset=ProductoTipo.objects.all(),
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#
#
#
#     class Meta:
#         model = Almacen
#         fields = ('nombre', 'marca', 'ubicacion', 'tipo', 'cantidad', 'photo')
#

class TipoOperacionForm(forms.ModelForm):
    class Meta:
        model = Tipo_OP
        fields = ('nombre', 'tipo', 'des')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class OperacionForm(forms.ModelForm):
    salario = forms.ModelChoiceField(
        queryset=Salario.objects.all(),
    )

    tipo_op = forms.ModelChoiceField(
        queryset=Tipo_OP.objects.all(),
    )

    class Meta:
        model = Operaciones
        fields = ('amount', 'des', 'salario', 'tipo_op')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class SalarioForm(forms.ModelForm):
    class Meta:
        model = Salario
        fields = ('amount',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class DeudaForm(forms.ModelForm):

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data < 0:
            raise ValidationError("La cantidad debe ser mayor que 0")
        # form validation for one filed only
        # here you have to return de value
        return data

    def clean(self):
        # form validation for more than one filed only
        # also is for comparision between
        # if you are lazy here you can do all de validation process
        # here is not need of return de value
        clean_data = super().clean()
        fechop = clean_data.get("fecha_operacion")
        fechven = clean_data.get("fecha_vencimiento")
        if fechven < fechop:
            msg = "La fecha de vencimiento debe ser mayor"
            self.add_error('fecha_vencimiento', msg)

    class Meta:
        model = Deudas
        fields = ('amount', 'tipo', 'estado', 'fecha_operacion', 'fecha_vencimiento', 'des')

    def __init__(self, *args, **kwargs):
        # self.amount = forms.IntegerField(error_messages={
        #     'invalid' : "La cantidad debe ser un número"
        # })
        # this is other way to do it
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
