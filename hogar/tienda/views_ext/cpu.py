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
from tienda.model_ext.cpu import Serie
from tienda.models import CPU
############### ENDS MODEL IMPORT ###############

############### FORM IMPORT ####################
from tienda.form import SerieForm
############### ENDS FORM IMPORT ###############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
############### ENDS OTHER IMPORT ################


######################################
#           Navegacion               #
#                                    #
#   1- Serie Clases                  #
#   2- Frame Sync Clases             #
#   3- Cooling Clases                #
#   4- External Power Clases         #
#   5- GPU Clases                    #
#   6- AJAX Petition                 #
#                                    #
######################################

########################
# 1 - Serie Clases     #
########################


class CreateSerie (LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/cpu/string_form.html"
    model = Serie
    success_url = reverse_lazy("tienda:interface_list")
    form_class = SerieForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Interfaz"
        return context

class ListSerie (LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/params_string_list.html"
    model = Serie

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:interface_update"
        context['add'] = "tienda:interface_add"
        context['delete'] = "tienda:interface_eliminar"

        return context

class UpdateSerie (LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/string_form.html"
    model = Serie
    form_class = SerieForm
    success_url = reverse_lazy('tienda:interface_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Interfaz"
        return context


@login_required
def SerieEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Serie.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:interface_list'))
