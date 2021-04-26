from django import forms
from .models import Category, Shipping, Tags
from .model_ext.generales import SLI, TypeMemory, Chipset, Color, Socket, TypeProduct, FormFactor, Manufacturer
from crispy_forms.helper import FormHelper
from dal import autocomplete
from crispy_forms.layout import Layout, Row, Column, Field

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('nombre','slug','photo')

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
        fields = ('nombre','precio')

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
        fields = ('nombre','slug')

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
        fields = ('nombre','slug')

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
        fields = ('nombre','slug', 'type')

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
        fields = ('nombre','slug',)

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
        fields = ('nombre','slug',)

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
        fields = ('nombre','slug',)

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
        fields = ('nombre','slug','type')

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
        fields = ('nombre','slug','type')

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