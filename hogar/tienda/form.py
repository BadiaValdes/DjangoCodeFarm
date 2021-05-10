from django import forms
from .models import Category, Shipping, Tags
from .model_ext.generales import SLI, TypeMemory, Chipset, Color, Socket, TypeProduct, FormFactor, Manufacturer
from .model_ext.case import TypeCase, PowerSupply, FrontPanelUSB, SidePanelWindow
from .model_ext.gpu import Interface, FrameSync, Cooling, ExternalPower
from .models import Case, GPU
from crispy_forms.helper import FormHelper
from dal import autocomplete
from crispy_forms.layout import Layout, Row, Column, Field
from crispy_forms.bootstrap import PrependedAppendedText


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('nombre', 'slug', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
            Row(
                Column('photo')
            )
        )


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ('nombre', 'precio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('precio')
            ),
        )


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ('nombre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
        )


# Common
class SLIForm(forms.ModelForm):
    class Meta:
        model = SLI
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class TypeMemoryForm(forms.ModelForm):
    class Meta:
        model = TypeMemory
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class ChipsetForm(forms.ModelForm):
    class Meta:
        model = Chipset
        fields = ('nombre', 'slug', 'type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
            Row(
                Column('type')
            ),
        )


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ('nombre', 'slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ('nombre', 'slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class TypeProductForm(forms.ModelForm):
    class Meta:
        model = TypeProduct
        fields = ('nombre', 'slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class FormFactorForm(forms.ModelForm):
    class Meta:
        model = FormFactor
        fields = ('nombre', 'slug', 'type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
            Row(
                Column('type')
            ),
        )


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('nombre', 'slug', 'type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
            Row(
                Column('type')
            ),
        )


class TypeCaseForm(forms.ModelForm):
    class Meta:
        model = TypeCase
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class SidePanelWindowForm(forms.ModelForm):
    class Meta:
        model = SidePanelWindow
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class FrontPanelUSBForm(forms.ModelForm):
    class Meta:
        model = FrontPanelUSB
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )


class PowerSupplyForm(forms.ModelForm):
    class Meta:
        model = PowerSupply
        fields = ('capacidad', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('capacidad')
            ),
            Row(
                Column('slug')
            ),
        )


class CaseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoría",
        widget=autocomplete.ModelSelect2(url='tienda:ac_category', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    shipping = forms.ModelChoiceField(
        queryset=Shipping.objects.all(),
        label="Método de entrega",
        widget=autocomplete.ModelSelect2(url='tienda:ac_shipping', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        label="Compañia",
        widget=autocomplete.ModelSelect2(url='tienda:ac_manufacturer', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    type_case = forms.ModelChoiceField(
        queryset=TypeCase.objects.all(),
        label="Tipo de Chasis",
        widget=autocomplete.ModelSelect2(url='tienda:ac_type_case', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    power_supply = forms.ModelChoiceField(
        queryset=PowerSupply.objects.all(),
        label="Capacidad para la fuente",
        widget=autocomplete.ModelSelect2(url='tienda:ac_power_supply', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    side_panel_window = forms.ModelChoiceField(
        queryset=SidePanelWindow.objects.all(),
        label="Panel Lateral",
        widget=autocomplete.ModelSelect2(url='tienda:ac_side_panel', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )
    front_panel_USB = forms.ModelChoiceField(
        queryset=FrontPanelUSB.objects.all(),
        label="Panel Frontal",
        widget=autocomplete.ModelSelect2(url='tienda:ac_front_panel', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    color = forms.ModelChoiceField(
        queryset=Color.objects.all(),
        label="Colores",
        widget=autocomplete.ModelSelect2(url='tienda:ac_color', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    formFactor = forms.ModelChoiceField(
        queryset=FormFactor.objects.all(),
        label="Tamaño",
        widget=autocomplete.ModelSelect2(url='tienda:ac_form_factor', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        label="Etiquetas",
        widget=autocomplete.ModelSelect2Multiple(url='tienda:ac_tags', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    external_bays_5 = forms.IntegerField(label="Baías externas de 5.25 pulgadas",
                                         max_value=12, min_value=0,
                                         # error_messages={'invalid':'Introduzca un numero entre 0 y 12'},
                                         widget=forms.NumberInput(attrs={
                                             # 'id': 'form_homework',
                                             # 'step': "0.01"
                                             'placeholder': 0,
                                         })
                                         )
    external_bays_3 = forms.IntegerField(label="Baías externas de 3.5 pulgadas",
                                         max_value=15, min_value=0,
                                         # error_messages={'invalid':'Introduzca un numero entre 0 y 12'},
                                         widget=forms.NumberInput(attrs={
                                             # 'id': 'form_homework',
                                             # 'step': "0.01"
                                             'placeholder': 0,
                                         })
                                         )

    internal_bays_3 = forms.IntegerField(label="Baías internas de 3.5 pulgadas",
                                         max_value=20, min_value=0,
                                         # error_messages={'invalid':'Introduzca un numero entre 0 y 12'},
                                         widget=forms.NumberInput(attrs={
                                             # 'id': 'form_homework',
                                             # 'step': "0.01"
                                             'placeholder': 0,
                                         })
                                         )
    internal_bays_2 = forms.IntegerField(label="Baías internas de 2.5 pulgadas",
                                         max_value=17, min_value=0,
                                         # error_messages={'invalid':'Introduzca un numero entre 0 y 12'},
                                         widget=forms.NumberInput(attrs={
                                             # 'id': 'form_homework',
                                             # 'step': "0.01"
                                             'placeholder': 0,
                                         })
                                         )

    full_h_expansion_slot = forms.IntegerField(label="Conectores de expansión de tamaño completo",
                                               max_value=11, min_value=0,
                                               # error_messages={'invalid':'Introduzca un numero entre 0 y 12'},
                                               widget=forms.NumberInput(attrs={
                                                   # 'id': 'form_homework',
                                                   # 'step': "0.01"
                                                   'placeholder': 0,
                                               })
                                               )

    half_h_expansion_slot = forms.IntegerField(label="Conectores de expansión de tamaño medio",
                                               max_value=6, min_value=0,
                                               # error_messages={'invalid':'Introduzca un numero entre 0 y 12'},
                                               widget=forms.NumberInput(attrs={
                                                   # 'id': 'form_homework',
                                                   # 'step': "0.01"
                                                   'placeholder': 0,
                                               })
                                               )

    class Meta:
        model = Case
        fields = "__all__"
        exclude = ("id",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            # Row(
            #     Column(PrependedAppendedText('category', '<i class="bi-alarm form_icon"></i>'))
            # ),

        )

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )

class FrameSyncForm(forms.ModelForm):
    class Meta:
        model = FrameSync
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )

class CoolingForm(forms.ModelForm):
    class Meta:
        model = Cooling
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )

class ExternalPowerForm(forms.ModelForm):
    class Meta:
        model = ExternalPower
        fields = ('nombre', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre')
            ),
            Row(
                Column('slug')
            ),
        )

class GPUForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        label="Etiquetas",
        widget=autocomplete.ModelSelect2Multiple(url='tienda:ac_tags', attrs={
            # Set some placeholder
            'data-placeholder': 'Tags ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoría",
        widget=autocomplete.ModelSelect2(url='tienda:ac_category', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    shipping = forms.ModelChoiceField(
        queryset=Shipping.objects.all(),
        label="Método de entrega",
        widget=autocomplete.ModelSelect2(url='tienda:ac_shipping', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        label="Compañia",
        widget=autocomplete.ModelSelect2(url='tienda:ac_manufacturer', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    color = forms.ModelChoiceField(
        queryset=Color.objects.all(),
        label="Colores",
        widget=autocomplete.ModelSelect2(url='tienda:ac_color', attrs={
            # Set some placeholder
            'data-placeholder': 'Autocomplete ...',
            # Only trigger autocompletion after 3 characters have been typed
            'minimumResultsForSearch': 1,
        }, )
    )

    chipset = forms.ModelChoiceField(
        queryset=Chipset.objects.all(),
        label="Chipset",
        widget=autocomplete.ModelSelect2(url='tienda:ac_chipset', attrs={
            'data-placeholder' : 'Chipset...',
            'minimumResultsForSearch': 1,
        })
    )

    type = forms.ModelChoiceField(
        queryset=TypeMemory.objects.all(),
        label="Tipo de memoria",
        widget=autocomplete.ModelSelect2(url='tienda:ac_type_memory', attrs={
            'data-placeholder' : 'Tipo de memoria',
            'minimumResultsForSearch' : 1,
        })
    )

    inteface = forms.ModelChoiceField(
        queryset=Interface.objects.all(),
        label="Interfaz",
        widget=autocomplete.ModelSelect2(url='tienda:ac_interface', attrs={
            'data-placeholder' : 'Interfaz ...',
            'minimumResultsForSearch' : 1,
        })
    )

    frame_sync = forms.ModelChoiceField(
        queryset=FrameSync.objects.all(),
        label="Frame Sync",
        widget=autocomplete.ModelSelect2(url='tienda:ac_frame_sync', attrs={
            'data-placeholder' : 'Frame Sync ...',
            'minimumResultsForSearch' : 1,
        })
    )

    sli= forms.ModelChoiceField(
        queryset=SLI.objects.all(),
        label="SLI / CROSS FIRE",
        widget=autocomplete.ModelSelect2(url='tienda:ac_sli', attrs={
            'data-placeholder' : 'SLI / CROSS FIRE ...',
            'minimumResultsForSearch' : 1,
        })
    )

    cooling = forms.ModelChoiceField(
        queryset=Cooling.objects.all(),
        label="Enfriamiento",
        widget=autocomplete.ModelSelect2(url='tienda:ac_cooling', attrs={
            'data-placeholder' : 'Enfriamiento ...',
            'minimumResultsForSearch' : 1,
        })
    )

    external_power = forms.ModelChoiceField(
        queryset=ExternalPower.objects.all(),
        label="Fuente Externa",
        widget=autocomplete.ModelSelect2(url='tienda:ac_external_power', attrs={
            'data-placeholder' : 'Fuente Externa ...',
            'minimumResultsForSearch' : 1,
        })
    )

    class Meta:
        model = GPU
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(

        )