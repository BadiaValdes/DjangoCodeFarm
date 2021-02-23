from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Almacen
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from dal import autocomplete
import os


# Producto
class CreateProductoView(LoginRequiredMixin, CreateView):
    template_name = 'almacen/producto_add.html'
    form_class = ProductForm
    model = Almacen
    success_url = '/almacen/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(CreateProductoView, self).form_valid(form)


class UpdateProductoView(LoginRequiredMixin, UpdateView):
    template_name = 'almacen/producto_update.html'
    form_class = ProductForm
    model = Almacen
    success_url = '/almacen/'


class DeleteProductoView(LoginRequiredMixin, DeleteView):
    model = Almacen
    success_url = "/almacen/"


@login_required
def eliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Almacen.objects.filter(id=dat).delete()
        notify.send(request.user, recipient=request.user,
                    verb='The items  have been deleted by {}'.format(request.user.username), level='info')
    return redirect('/almacen/')


