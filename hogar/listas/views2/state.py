from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..models import State
from ..forms import StateForm
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

class StateCreateView(LoginRequiredMixin, CreateView):
    template_name = 'list/state_add.html'
    form_class = StateForm
    success_url = reverse_lazy('lista:state_list')
    model = State


class StateUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'list/state_update.html'
    form_class = StateForm
    success_url = reverse_lazy('lista:state_list')
    model = State

class StateDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('lista:state_list')
    model = State

class StateListView(LoginRequiredMixin, ListView):
    model = State
    template_name = 'list/state_list.html'

    #def get_queryset(self):
    #    queryset = Marca.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def StateEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            State.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('lista:state_list'))
