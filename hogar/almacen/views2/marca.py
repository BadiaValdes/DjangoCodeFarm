from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Marca
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..forms import MarcaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CreateMarcaView(LoginRequiredMixin, CreateView):
    template_name = 'almacen/marca_add.html'
    form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('almacen:marca_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(CreateMarcaView, self).form_valid(form)


class UpdateMarcaView(LoginRequiredMixin, UpdateView):
    template_name = 'almacen/marca_update.html'
    form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('almacen:marca_list')


class DeleteMarcaView(LoginRequiredMixin, DeleteView):
    model = Marca
    success_url = reverse_lazy('almacen:marca_list')


class MarcaListView(LoginRequiredMixin, ListView):
    model = Marca
    template_name = 'almacen/marca_list.html'

    #def get_queryset(self):
    #    queryset = Marca.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MarcaDetailView(LoginRequiredMixin, DetailView):
    model = Marca
    template_name = 'almacen/marca_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def MarcaEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Marca.objects.filter(id=dat).delete()
    return redirect('/almacen/marca/')
