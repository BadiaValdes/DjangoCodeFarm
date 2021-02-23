from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..models import Item, Lista
from ..forms import ItemForm
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

class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'list/item_add.html'
    form_class = ItemForm
    success_url = reverse_lazy('lista:lista')
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_id'] = self.kwargs['pk']
        return context

    # metodo que sobreescribe el comportamiento de la inicializacion del formulario
    def get_form_kwargs(self):
        kwards = super(ItemCreateView, self).get_form_kwargs()  # Se hereda el comportamiento
        kwards['list'] = self.kwargs['pk']  # Se crea la nueva kwargs
        return kwards  # Se envia

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        li = Lista.objects.filter(id__contains=self.kwargs['pk']).first()
        object.list = li
        object.save()
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'list/item_update.html'
    form_class = ItemForm
    success_url = reverse_lazy('lista:lista')
    model = Item





class ItemDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('lista:lista')
    model = Item


@login_required
def ItemEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Item.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('lista:lista'))
