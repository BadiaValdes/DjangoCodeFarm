from django.shortcuts import render, get_object_or_404, redirect
from ..models import Posicion
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..forms import PosicionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from dal import autocomplete

import os


# Ubicacion = posicion
class CreateUbicacionView(LoginRequiredMixin, CreateView):
    template_name = 'almacen/posicion_add.html'
    form_class = PosicionForm
    model = Posicion
    success_url = reverse_lazy('almacen:ubicacion_list')


class UpdateUbicacionView(LoginRequiredMixin, UpdateView):
    template_name = 'almacen/posicion_update.html'
    form_class = PosicionForm
    model = Posicion
    success_url = reverse_lazy('almacen:ubicacion_list')


class DeleteUbicacionView(LoginRequiredMixin, DeleteView):
    model = Posicion
    success_url = reverse_lazy('almacen:ubicacion_list')


class UbicacionListView(LoginRequiredMixin, ListView):
    model = Posicion
    template_name = 'almacen/posicion_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UbicacionDetailView(LoginRequiredMixin, DetailView):
    model = Posicion
    template_name = 'almacen/posicion_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def UbicacionEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Posicion.objects.filter(id=dat).delete()
    return redirect('/almacen/ubicacion/')


class UbicacionAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Posicion.objects.none()
        qs = Posicion.objects.all()
        if self.q:
            qs = qs.filter(nombre__istartswith=self.q)
        return qs