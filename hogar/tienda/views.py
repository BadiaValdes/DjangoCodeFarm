from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .models import Category
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
from django.utils.timezone import now
from rolepermissions.decorators import has_role_decorator


def index(request):
    # notify.send(request.user, recipient=request.user, verb='The items  have been deleted by {}'.format(request.user.username), level='info')
    if request.user is not None:
        category = Category.objects.all().order_by('nombre')
        context = {"category": category}
        return render(request, '../templates/shop/index.html', context)
    else:
        return HttpResponse('Not user found')


@login_required
@has_role_decorator('admin')
def dashboard(request):
    category = Category.objects.all().order_by('nombre')
    context = {"category": category,
               "nomencladores": ['shipping',
                                 'type_memory',
                                 'tags',
                                 'case',
                                 'type_case',
                                 'power_supply',
                                 'side_panel',
                                 'front_panel',
                                 'serie',
                                 'microArch',
                                 'graphic',
                                 "coreFamily",
                                 "interface",
                                 "frame_sync",
                                 "cooling",
                                 "external_power",
                                 "ethernet",
                                 "wireless",
                                 "tiemposRAM",
                                 "eccRAM",
                                 "chipset",
                                 "color",
                                 "socket",
                                 "type_product",
                                 "form_factor",
                                 "manufacturer", ]
               }

    return render(request, '../templates/shop/dashboard/dashboard.html', context)
