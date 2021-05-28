############### DECORATORS IMPORT ################
from django.contrib.auth.decorators import login_required
############### ENDS DECORATORS IMPORT ###########

############### MIXIN IMPORT #####################
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin
############### ENDS MIXIN IMPORT ################

############### GENERIC VIEW IMPORT ##############
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
############### ENDS GENERIC VIEW IMPORT #########

############### MODELS IMPORT ###################
from tienda.model_ext.ram import TiemposRAM, ECCRAM
from tienda.models import RAM
############### ENDS MODEL IMPORT ###############

############### FORM IMPORT ####################
from tienda.form import TiemposRAMForm, ECCRAMForm, RAMForm
############### ENDS FORM IMPORT ###############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


############### ENDS OTHER IMPORT ################

######################################
#           Navegacion               #
#                                    #
#   1- TiemposRAM Class              #
#   2- ECCRAM Class                  #
#   3- RAM Class                     #
#   4- AJAX Petition                 #
#                                    #
######################################

#########################
# 1 - TiemposRAM Class  #
#########################

class CreateTiemposRAM(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/ram/string_form.html"
    model = TiemposRAM
    success_url = reverse_lazy("tienda:tiempos_ram_list")
    form_class = TiemposRAMForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Teimpos RAM"
        return context


class ListTiemposRAM(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/ram/params_string_list.html"
    model = TiemposRAM

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:tiempos_ram_update"
        context['add'] = "tienda:tiempos_ram_add"
        context['delete'] = "tienda:tiempos_ram_eliminar"

        return context


class UpdateTiemposRAM(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/ram/string_form.html"
    model = TiemposRAM
    form_class = TiemposRAMForm
    success_url = reverse_lazy('tienda:tiempos_ram_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Teimpos RAM"
        return context


@login_required
def TiemposRAMEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            TiemposRAM.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:tiempos_ram_list'))

#####################
# 2 - ECCRAM Class  #
#####################

class CreateECCRAM(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/ram/string_form.html"
    model = ECCRAM
    success_url = reverse_lazy("tienda:ecc_ram_list")
    form_class = ECCRAMForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar ECC RAM"
        return context


class ListECCRAM(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/ram/params_string_list.html"
    model = ECCRAM

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:ecc_ram_update"
        context['add'] = "tienda:ecc_ram_add"
        context['delete'] = "tienda:ecc_ram_eliminar"

        return context


class UpdateECCRAM(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/ram/string_form.html"
    model = ECCRAM
    form_class = ECCRAMForm
    success_url = reverse_lazy('tienda:ecc_ram_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar ECC RAM"
        return context


@login_required
def ECCRAMEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            ECCRAM.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:ecc_ram_list'))

##################
# 3 - RAM Class  #
##################

class CreateRAM(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:ram_list")
    template_name = "shop/ram/ram_form.html"
    model = RAM
    form_class = RAMForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar RAM"

        return context


class ListRAM(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/ram/ram_list.html"
    model = RAM

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UpdateRAM(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:ram_list")
    template_name = "shop/ram/ram_form.html"
    model = RAM
    form_class = RAMForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar RAM"
        return context


@login_required
def RAMEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            RAM.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:ram_list'))

