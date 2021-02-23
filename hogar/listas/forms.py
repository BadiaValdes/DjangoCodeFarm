from django import forms
from .models import Tipo, State, Lista, Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class TipoForm (forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False



class StateForm (forms.ModelForm):
    class Meta:
        model = State
        fields = ('nb', 'tipo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class ListaForm (forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nb', 'tipo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class ItemForm (forms.ModelForm):


    class Meta:
        model = Item
        fields = "__all__"
        exclude = ('user', 'list')

    def __init__(self, *args, **kwargs):
        list_type = kwargs.pop('list', None)
        lista = Lista.objects.get(id__contains=list_type)
        # al realizar el super, se pierden los parametros enviados por lo que es necesario realizar la peticion antes
        #lis = Tipo.objects.get(id__contains=lista.tipo)
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.filter(tipo__id=lista.tipo_id) #mediante fields se puede acceder a los campos del formulario
        self.helper = FormHelper()
        self.helper.form_tag = False





