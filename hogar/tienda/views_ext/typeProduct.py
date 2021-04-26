from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from rolepermissions.mixins import HasRoleMixin
from tienda.models import TypeProduct
from tienda.form import TypeProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from io import BytesIO
from django.core.files import File
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from django.utils.timezone import now


class CreateTypeProduct(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:type_product_list")
    template_name = "shop/common/string_form.html"
    model = TypeProduct
    form_class = TypeProductForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Producto"
        return context


class ListTypeProduct(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/common/type_product_list.html"
    model = TypeProduct

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateTypeProduct(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:type_product_list")
    template_name = "shop/common/string_form.html"
    model = TypeProduct
    form_class = TypeProductForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Tipo de Producto"
        return context

@login_required
def ItemEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            TypeProduct.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:socket_list'))