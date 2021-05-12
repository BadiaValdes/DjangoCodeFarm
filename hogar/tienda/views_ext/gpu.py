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
from tienda.model_ext.gpu import Interface, FrameSync, Cooling, ExternalPower
from tienda.models import GPU
############### ENDS MODEL IMPORT ###############

############### FORM IMPORT ####################
from tienda.form import InterfaceForm, FrameSyncForm, CoolingForm, ExternalPowerForm, GPUForm
############### ENDS FORM IMPORT ###############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


############### ENDS OTHER IMPORT ################


######################################
#           Navegacion               #
#                                    #
#   1- Interface Clases              #
#   2- Frame Sync Clases             #
#   3- Cooling Clases                #
#   4- External Power Clases         #
#   5- GPU Clases                    #
#   6- AJAX Petition                 #
#                                    #
######################################

########################
# 1 - Interface Clases #
########################

class CreateInterface(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/gpu/string_form.html"
    model = Interface
    success_url = reverse_lazy("tienda:interface_list")
    form_class = InterfaceForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Interfaz"
        return context


class ListInterface(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/params_string_list.html"
    model = Interface

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:interface_update"
        context['add'] = "tienda:interface_add"
        context['delete'] = "tienda:interface_eliminar"

        return context


class UpdateInterface(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/string_form.html"
    model = Interface
    form_class = InterfaceForm
    success_url = reverse_lazy('tienda:interface_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Interfaz"
        return context


@login_required
def ItemEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Interface.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:interface_list'))


########################
# 2- Frame Sync Clases #
########################

class CreateFrameSync(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/gpu/string_form.html"
    model = FrameSync
    success_url = reverse_lazy("tienda:frame_sync_list")
    form_class = FrameSyncForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Frame Sync"
        return context


class ListFrameSync(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/params_string_list.html"
    model = FrameSync

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:frame_sync_update"
        context['add'] = "tienda:frame_sync_add"
        context['delete'] = "tienda:frame_sync_eliminar"

        return context


class UpdateFrameSync(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/string_form.html"
    model = FrameSync
    form_class = FrameSyncForm
    success_url = reverse_lazy('tienda:frame_sync_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Frame Sync"
        return context


@login_required
def EliminarFrameSync(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            FrameSync.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:frame_sync_list'))


########################
# 3- Cooling Clases    #
########################


class CreateCooling(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/gpu/string_form.html"
    model = Cooling
    success_url = reverse_lazy("tienda:cooling_list")
    form_class = CoolingForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Cooling"
        return context


class ListCooling(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/params_string_list.html"
    model = Cooling

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:cooling_update"
        context['add'] = "tienda:cooling_add"
        context['delete'] = "tienda:cooling_eliminar"

        return context


class UpdateCooling(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/string_form.html"
    model = Cooling
    form_class = CoolingForm
    success_url = reverse_lazy('tienda:cooling_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Cooling"
        return context


@login_required
def EliminarCooling(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Cooling.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:cooling_list'))


###############################
# 4- External Power Clases    #
###############################

class CreateExternalPower(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/gpu/string_form.html"
    model = ExternalPower
    success_url = reverse_lazy("tienda:external_power_list")
    form_class = ExternalPowerForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar External Power"
        return context


class ListExternalPower(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/params_string_list.html"
    model = ExternalPower

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:external_power_update"
        context['add'] = "tienda:external_power_add"
        context['delete'] = "tienda:external_power_eliminar"

        return context


class UpdateExternalPower(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/string_form.html"
    model = ExternalPower
    form_class = ExternalPowerForm
    success_url = reverse_lazy('tienda:external_power_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar External Power"
        return context


@login_required
def EliminarExternalPower(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            ExternalPower.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:external_power_list'))


###############################
# 5- GPU Clases               #
###############################

class CreateGPU(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/gpu/gpu_form.html"
    model = GPU
    success_url = reverse_lazy("tienda:gpu_list")
    form_class = GPUForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar GPU"
        return context


class ListGPU(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/gpu_list.html"
    model = GPU

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateGPU(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/gpu/gpu_form.html"
    model = GPU
    form_class = GPUForm
    success_url = reverse_lazy('tienda:gpu_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar GPU"
        return context


@login_required
def EliminarGPU(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            GPU.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:gpu_list'))


################################
# 6- AJAX Petition             #
################################

@login_required
def AvailableGPU(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        gpu = GPU.objects.get(id=item_id)
        gpu.available = False if (gpu.available == True) else True
        gpu.save()
        data = {
            'available': gpu.available,
        }
        return JsonResponse(data)

    else:
        return HttpResponse("Bad!")

@login_required
def GPUDetail(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        gpu = GPU.objects.get(id=item_id)
        data = {
            "nb": gpu.nombre,
            "slug": gpu.slug,
            "available": gpu.available,
            "tags" : gpu.Tags(),
            "category": gpu.category.nombre,
            "precio": gpu.precio,
            "precio_descuento": gpu.precioDescuento(),
            "img": gpu.photo.url,
            "shipping": gpu.shipping.nombre,
            "manufacturer": gpu.manufacturer.nombre,
            "chipset": gpu.chipset.nombre,
            "type": gpu.type.nombre,
            "core_clock": gpu.core_clock,
            "boost_clock": gpu.boost_clock,
            "inteface": gpu.inteface.nombre,
            "frame_sync": gpu.frame_sync.nombre,
            "color": gpu.color.nombre,
            "sli": gpu.sli.nombre,
            "cooling": gpu.cooling.nombre,
            "external_power": gpu.external_power.nombre,
            "length_gpu": gpu.length,
            "tdp": gpu.tdp,
            "dvi_port": gpu.dvi_port,
            "hdmi_port": gpu.hdmi_port,
            "display_port": gpu.display_port,
            "mini_display_port": gpu.mini_display_port,
            "expansion_width": gpu.expansion_width,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")
