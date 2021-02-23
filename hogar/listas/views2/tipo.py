from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..models import Tipo, State, Lista, Item
from ..forms import TipoForm
from django.contrib.auth.decorators import login_required
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


# Create your views here.

class TipoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'list/tipo_add.html'
    form_class = TipoForm
    success_url = reverse_lazy('lista:tipo_list')
    model = Tipo


class TipoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'list/tipo_update.html'
    form_class = TipoForm
    success_url = reverse_lazy('lista:tipo_list')
    model = Tipo

class TipoDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('lista:tipo_list')
    model = Tipo

class TipoListView(LoginRequiredMixin, ListView):
    model = Tipo
    template_name = 'list/tipo_list.html'

    #def get_queryset(self):
    #    queryset = Marca.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def TipoEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Tipo.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('lista:tipo_list'))
