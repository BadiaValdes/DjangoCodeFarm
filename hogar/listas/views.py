from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Lista, Item, State

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

@login_required
def index(request):
    if request.user.is_authenticated:
        list = Lista.objects.filter(user__id=request.user.id)
        item = Item.objects.all().order_by('nb')
        state = State.objects.all()

        contex = {
            'list': list,
            'item': item,
            'state': state,
        }
        return render(request, 'list/list.html', contex)


@login_required
def change_sate(request, pk_item, pk_state):
    if request.user.is_authenticated:
        Item.objects.filter(id=pk_item).update(state=pk_state)


        return redirect(reverse_lazy('lista:lista'))


def change_sate_details(request, pk_list, pk_item, pk_state):
    if request.user.is_authenticated:
        Item.objects.filter(id=pk_item).update(state=pk_state)

        lista = Lista.objects.filter(id=pk_list).first()

        return redirect(reverse_lazy('lista:lista_details', args = [lista.id]))
