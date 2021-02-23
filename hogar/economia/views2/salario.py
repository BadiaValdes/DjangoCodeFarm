from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from ..models import Operaciones, Salario, Deudas, Tipo_OP
from ..forms import TipoOperacionForm, OperacionForm, SalarioForm
from ..util import restoSalario
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.timezone import now
# Create your views here.

class CreateSalario(LoginRequiredMixin, CreateView):
    model = Salario
    form_class = SalarioForm
    template_name = 'economy/salario_add.html'
    success_url = reverse_lazy('economia:index')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(CreateSalario, self).form_valid(form)


class SalarioList(LoginRequiredMixin, ListView):
    model = Salario
    template_name = 'economy/salario_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SalarioDetailView(LoginRequiredMixin, DetailView):
    model = Salario
    template_name = 'economy/salario_details.html'

    #def get_queryset(self):
        #queryset = Lista.objects.filter(id=self.kwargs['pk']).first()
        #return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        salario = Salario.objects.filter(id=self.kwargs['pk']).first()
        salarioID = salario.id
        context['operaciones'] = Operaciones.objects.filter(salario=salarioID)
        context['dineroDepositado'] = salario.cantidad()
        context['deposito'] = salario.fecha_deposito
        context['restoSalario'] = salario.amount + restoSalario(salario.id)
        context['cantOperaciones'] = Operaciones.objects.filter(salario=salarioID).count()
        context['cantOperacionesSalida']= Operaciones.objects.filter(salario=salarioID, tipo_op__tipo='Salida').count()
        context['cantOperacionesEntrada'] = Operaciones.objects.filter(salario=salarioID, tipo_op__tipo='Entrada').count()
        #context['cantDeudas'] = Deudas.objects.filter(salario=salarioID, tipo__exact='DEUDAS').count()
        #context['cantPrestamos'] = Deudas.objects.filter(salario=salarioID, tipo__exact='PRESTAMOS').count()
        #context['cantDeudasLiquidadas'] = Deudas.objects.filter(salario=salarioID, estado__exact='Liquidada').count()
        #context['cantDeudasPendientes'] = Deudas.objects.filter(salario=salarioID, estado__exact='Pendiente').count()
        return context