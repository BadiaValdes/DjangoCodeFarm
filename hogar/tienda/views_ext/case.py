from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from rolepermissions.mixins import HasRoleMixin
from tienda.model_ext.case import TypeCase, SidePanelWindow, PowerSupply, FrontPanelUSB
from tienda.model_ext.generales import Manufacturer, TypeProduct, Color, FormFactor
from tienda.models import Case, Category, Tags, Shipping
from tienda.form import TypeCaseForm, PowerSupplyForm, SidePanelWindowForm, FrontPanelUSBForm, CaseForm
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


######################################
#           Navegacion               #
#                                    #
#   1- Type Case Clases              #
#   2- Power Supply Clases           #
#   3- Side Panel Window Clases      #
#   4- Front Panel USB Clases        #
#   5- Case Clases                   #
#   6- AJAX Petition                 #
#                                    #
######################################

########################
# 1 - Type Case Clases #
########################

class CreateTypeCase(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:type_case_list")
    template_name = "shop/case/string_form.html"
    model = TypeCase
    form_class = TypeCaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Tipo de Torre"
        return context


class ListTypeCase(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/case/params_string_list.html"
    model = TypeCase

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:type_case_update"
        context['add'] = "tienda:type_case_add"
        context['delete'] = "tienda:type_case_eliminar"

        return context


class UpdateTypeCase(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:type_case_list")
    template_name = "shop/case/string_form.html"
    model = TypeCase
    form_class = TypeCaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Tipo de Torre"
        return context


@login_required
def ItemEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            TypeCase.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:type_case_list'))


##########################
# 2- Power Supply Clases #
##########################

class CreatePowerSupply(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:power_supply_list")
    template_name = "shop/case/int_form.html"
    model = PowerSupply
    form_class = PowerSupplyForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Capacidad de energía"
        return context


class ListPowerSupply(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/case/params_int_list.html"
    model = PowerSupply

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:power_supply_update"
        context['add'] = "tienda:power_supply_add"
        context['delete'] = "tienda:power_supply_eliminar"

        return context


class UpdatePowerSupply(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:power_supply_list")
    template_name = "shop/case/int_form.html"
    model = PowerSupply
    form_class = PowerSupplyForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Capacidad de energía"
        return context


@login_required
def EliminarPowerSupply(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            PowerSupply.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:power_supply_list'))


################################
# 3- Side Panel Windows Clases #
################################

class CreateSidePanelWindow(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:side_panel_list")
    template_name = "shop/case/string_form.html"
    model = SidePanelWindow
    form_class = SidePanelWindowForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Panel Lateral"
        return context


class ListSidePanelWindow(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/case/params_string_list.html"
    model = SidePanelWindow

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:side_panel_update"
        context['add'] = "tienda:side_panel_add"
        context['delete'] = "tienda:side_panel_eliminar"

        return context


class UpdateSidePanelWindow(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:side_panel_list")
    template_name = "shop/case/int_form.html"
    model = SidePanelWindow
    form_class = SidePanelWindowForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Panel Lateral"
        return context


@login_required
def EliminarSidePanelWindow(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            SidePanelWindow.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:side_panel_list'))


################################
# 4- Front Panel USB Clases    #
################################

class CreateFrontPanelUSB(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:front_panel_list")
    template_name = "shop/case/string_form.html"
    model = FrontPanelUSB
    form_class = FrontPanelUSBForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Panel Frontal"
        return context


class ListFrontPanelUSB(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/case/params_string_list.html"
    model = FrontPanelUSB

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:front_panel_update"
        context['add'] = "tienda:front_panel_add"
        context['delete'] = "tienda:front_panel_eliminar"

        return context


class UpdateFrontPanelUSB(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:front_panel_list")
    template_name = "shop/case/int_form.html"
    model = FrontPanelUSB
    form_class = FrontPanelUSBForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Panel Frontal"
        return context


@login_required
def EliminarFrontPanelUSB(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            FrontPanelUSB.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:front_panel_list'))


################################
# 5- Case Clases               #
################################

class CreateCase(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:front_panel_list")
    template_name = "shop/case/case_form.html"
    model = Case
    form_class = CaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Panel Frontal"

        return context


class ListCase(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/case/case_list.html"
    model = Case

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UpdateCase(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:front_panel_list")
    template_name = "shop/case/int_form.html"
    model = Case
    form_class = CaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Panel Frontal"
        return context


@login_required
def EliminarCase(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Case.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:front_panel_list'))



################################
# 6- AJAX Petition             #
################################

@login_required
def CaseDetail(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        case = Case.objects.get(id=item_id)
        data = {
            "nb": case.nombre,
            "slug": case.slug,
            "tags" : case.Tags(),
            "category": case.category.nombre,
            "precio": case.precio,
            "precio_descuento": case.precioDescuento(),
            "img": case.photo.url,
            "shipping": case.shipping.nombre,
            "manufacturer": case.manufacturer.nombre,
            "type": case.type_case.nombre,
            "power_supply": case.power_supply.Capacidad(),
            "side_panel": case.side_panel_window.nombre,
            "front_panel": case.front_panel_USB.nombre,
            "color": case.color.nombre,
            "from_factor": case.formFactor.nombre,
            "external_bays_5": case.external_bays_5,
            "external_bays_3": case.external_bays_3,
            "internal_bays_3": case.internal_bays_3,
            "internal_bays_2": case.internal_bays_2,
            "full_h_expansion_slot": case.full_h_expansion_slot,
            "half_h_expansion_slot": case.half_h_expansion_slot,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")
