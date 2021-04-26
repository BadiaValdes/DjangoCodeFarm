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

@login_required
def index(request):
    # notify.send(request.user, recipient=request.user, verb='The items  have been deleted by {}'.format(request.user.username), level='info')
    if request.user is not None:
        category = Category.objects.all().order_by('nombre')
        context = {"category" : category}
        return render(request, '../templates/shop/index.html', context)
    else:
        return HttpResponse('Not user found')