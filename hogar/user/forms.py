from django import forms
from .models import User
from django.contrib.auth.models import Group
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout, Row, Column


class UserForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "avatar", "group"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "avatar"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class UserUpdateFormAdmin(forms.ModelForm):
    options = Group.objects.all()
    group = forms.ModelMultipleChoiceField(
        queryset=options, widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = User
        fields = ["group"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

