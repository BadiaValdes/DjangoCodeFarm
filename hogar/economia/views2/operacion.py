from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from ..models import Operaciones, Salario, Deudas, Tipo_OP
from ..forms import TipoOperacionForm, OperacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.timezone import now
# Create your views here.

class CreateOperacion(LoginRequiredMixin, CreateView):
    model = Tipo_OP
    form_class = OperacionForm
    template_name = 'economy/operacion_add.html'
    success_url = reverse_lazy('economia:index')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(CreateOperacion, self).form_valid(form)



class OperacionList(LoginRequiredMixin, ListView):
    model = Operaciones
    template_name = 'economy/operacion_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context