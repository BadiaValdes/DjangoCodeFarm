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
from tienda.model_ext.motherboard import MemoryType, Ethernet, Wireless
from tienda.models import MotherBoard
############### ENDS MODEL IMPORT ###############

############### FORM IMPORT ####################
from tienda.form import MemoryTypeForm, EthernetForm, WirelessForm, MotherboardForm
############### ENDS FORM IMPORT ###############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


############### ENDS OTHER IMPORT ################

######################################
#           Navegacion               #
#                                    #
#   1- Ethernet Class                #
#   2- Wireless Class                #
#   3- Motherboard Class             #
#   4- AJAX Petition                 #
#                                    #
######################################

#######################
# 1 - Ethernet Class  #
#######################

class CreateEthernet(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/motherboard/string_form.html"
    model = Ethernet
    success_url = reverse_lazy("tienda:ethernet_list")
    form_class = EthernetForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Ethernet"
        return context


class ListEthernet(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/motherboard/params_string_list.html"
    model = Ethernet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:ethernet_update"
        context['add'] = "tienda:ethernet_add"
        context['delete'] = "tienda:ethernet_eliminar"

        return context


class UpdateEthernet(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/motherboard/string_form.html"
    model = Ethernet
    form_class = EthernetForm
    success_url = reverse_lazy('tienda:ethernet_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Ethernet"
        return context


@login_required
def EthernetEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Ethernet.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:ethernet_list'))


#######################
# 2 - Wireless Class  #
#######################

class CreateWireless(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/motherboard/string_form.html"
    model = Wireless
    success_url = reverse_lazy("tienda:wireless_list")
    form_class = WirelessForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Wireless"
        return context


class ListWireless(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/motherboard/params_string_list.html"
    model = Wireless

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:wireless_update"
        context['add'] = "tienda:wireless_add"
        context['delete'] = "tienda:wireless_eliminar"

        return context


class UpdateWireless(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/motherboard/string_form.html"
    model = Wireless
    form_class = WirelessForm
    success_url = reverse_lazy('tienda:wireless_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Wireless"
        return context


@login_required
def WirelessEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Wireless.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:wireless_list'))


##########################
# 3 - Motherboard Class  #
##########################

class CreateMotherBoard(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:motherboard_list")
    template_name = "shop/motherboard/motherboard_form.html"
    model = MotherBoard
    form_class = MotherboardForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Motherboard"

        return context


class ListMotherBoard(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/motherboard/motherboard_list.html"
    model = MotherBoard

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UpdateMotherBoard(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:motherboard_list")
    template_name = "shop/motherboard/motherboard_form.html"
    model = MotherBoard
    form_class = MotherboardForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar CPU"
        return context


@login_required
def MotherBoardEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            MotherBoard.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:motherboard_list'))


################################
# 6- AJAX Petition             #
################################

@login_required
def AvailableMotherboard(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        motherboard = MotherBoard.objects.get(id=item_id)
        motherboard.available = False if (motherboard.available == True) else True
        motherboard.save()
        data = {
            'available': motherboard.available,
        }
        return JsonResponse(data)

    else:
        return HttpResponse("Bad!")


@login_required
def MotherboardDetail(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        motherboard = MotherBoard.objects.get(id=item_id)
        data = {
            "nb": motherboard.nombre,
            "slug": motherboard.slug,
            "available": motherboard.available,
            "manufacturer": motherboard.manufacturer.nombre,
            "tags": motherboard.Tags(),
            "category": motherboard.category.nombre,
            "precio": motherboard.precio,
            "precio_descuento": motherboard.precioDescuento(),
            "img": motherboard.photo.url,
            "socket": motherboard.socket.nombre,
            "chipset": motherboard.chipset.nombre,
            "form_Factor": motherboard.form_Factor.nombre,
            "maxMemory": motherboard.maxMemory,
            "memoryType": motherboard.memoryType.nombre,
            "memorySlot": motherboard.memorySlot,
            "color_m": motherboard.color.nombre,
            "sli": motherboard.sli.nombre,
            "pciX16Slot": motherboard.pciX16Slot,
            "pciX8Slot": motherboard.pciX8Slot,
            "pciX4Slot": motherboard.pciX4Slot,
            "pciX1Slot": motherboard.pciX1Slot,
            "pciSlot": motherboard.pciSlot,
            "sata3Port": motherboard.sata3Port,
            "sata6Port": motherboard.sata6Port,
            "m2Slot": motherboard.m2Slot,
            "mSataSlot": motherboard.mSataSlot,
            "ethernet": motherboard.ethernet.nombre,
            "wireless": motherboard.wireless.nombre,
            "boarVideo": motherboard.boarVideo,
            "suportECC": motherboard.suportECC,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")
