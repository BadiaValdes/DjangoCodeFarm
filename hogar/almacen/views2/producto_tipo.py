from ..models import ProductoTipo
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..forms import ProductTipoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Producto tipo
class CreateProductoTipoView(LoginRequiredMixin, CreateView):
    template_name = 'almacen/producto_tipo_add.html'
    form_class = ProductTipoForm
    model = ProductoTipo
    success_url = '/almacen/producto_tipo'


class UpdateProductoTipoView(LoginRequiredMixin, UpdateView):
    template_name = 'almacen/producto_tipo_update.html'
    form_class = ProductTipoForm
    model = ProductoTipo
    success_url = '/almacen/'


class DeleteProductoTipoView(LoginRequiredMixin, DeleteView):
    model = ProductoTipo
    success_url = "/almacen/"


class ProductoTipoListView(LoginRequiredMixin, ListView):
    model = ProductoTipo
    template_name = 'almacen/producto_tipo_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductoTipoDetailView(LoginRequiredMixin, DetailView):
    model = ProductoTipo
    template_name = 'almacen/producto_tipo_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def eliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            ProductoTipo.objects.filter(id=dat).delete()
    return redirect('/almacen/producto_tipo')
