from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..models import Lista, State, Item
from ..forms import ListaForm
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

class ListaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'list/list_add.html'
    form_class = ListaForm
    success_url = reverse_lazy('lista:lista')
    model = Lista

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(ListaCreateView, self).form_valid(form)


class ListaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'list/list_update.html'
    form_class = ListaForm
    success_url = reverse_lazy('lista:lista')
    model = Lista

class ListaDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('lista:lista')
    model = Lista


class ListaDetailView(LoginRequiredMixin, DetailView):
    model = Lista
    template_name = 'list/list_details.html'

    #def get_queryset(self):
        #queryset = Lista.objects.filter(id=self.kwargs['pk']).first()
        #return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Item.objects.filter(list__id=self.kwargs['pk'])
        context['state'] = State.objects.all()
        context['list_a'] = Lista.objects.filter(id=self.kwargs['pk']).first()
        return context

@login_required
def ListaEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Lista.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('lista:lista'))
