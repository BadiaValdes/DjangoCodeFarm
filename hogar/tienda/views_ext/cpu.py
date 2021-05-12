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
from tienda.model_ext.cpu import Serie, MicroArch, CoreFamily, IntegrateGraphic
from tienda.models import CPU
############### ENDS MODEL IMPORT ###############

############### FORM IMPORT ####################
from tienda.form import SerieForm, MicroArchForm, IntegrateGraphicForm, CoreFamilyForm, CPUForm
############### ENDS FORM IMPORT ###############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


############### ENDS OTHER IMPORT ################


######################################
#           Navegacion               #
#                                    #
#   1- Serie Class                   #
#   2- Micro Architecture Class      #
#   3- Integrate Graphic Class       #
#   4- Core Family Class             #
#   5- CPU Class                     #
#   6- AJAX Petition                 #
#                                    #
######################################

########################
# 1 - Serie Class      #
########################


class CreateSerie(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/cpu/string_form.html"
    model = Serie
    success_url = reverse_lazy("tienda:serie_list")
    form_class = SerieForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar CPU Serie"
        return context


class ListSerie(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/params_string_list.html"
    model = Serie

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:serie_update"
        context['add'] = "tienda:serie_add"
        context['delete'] = "tienda:serie_eliminar"

        return context


class UpdateSerie(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/string_form.html"
    model = Serie
    form_class = SerieForm
    success_url = reverse_lazy('tienda:serie_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar CPU Serie"
        return context


@login_required
def SerieEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            Serie.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:serie_list'))


#####################################
# 2 - Micro Architecture Class      #
#####################################

class CreateMicroArch(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/cpu/string_form.html"
    model = MicroArch
    success_url = reverse_lazy("tienda:microArch_list")
    form_class = MicroArchForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Micro Arquitectura del CPU"
        return context


class ListMicroArch(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/params_string_list.html"
    model = MicroArch

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:microArch_update"
        context['add'] = "tienda:microArch_add"
        context['delete'] = "tienda:microArch_eliminar"

        return context


class UpdateMicroArch(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/string_form.html"
    model = MicroArch
    form_class = MicroArchForm
    success_url = reverse_lazy('tienda:microArch_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Micro Arquitectura del CP"
        return context


@login_required
def MicroArchEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            MicroArch.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:microArch_list'))


####################################
# 3 - Integrate Graphic Class      #
####################################

class CreateIntegrateGraphic(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/cpu/string_form.html"
    model = IntegrateGraphic
    success_url = reverse_lazy("tienda:graphic_list")
    form_class = IntegrateGraphicForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Grafica Integrada"
        return context


class ListIntegrateGraphic(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/params_string_list.html"
    model = IntegrateGraphic

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:graphic_update"
        context['add'] = "tienda:graphic_add"
        context['delete'] = "tienda:graphic_eliminar"

        return context


class UpdateIntegrateGraphic(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/string_form.html"
    model = IntegrateGraphic
    form_class = IntegrateGraphicForm
    success_url = reverse_lazy('tienda:graphic_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Grafica Integrada"
        return context


@login_required
def IntegrateGraphicEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            IntegrateGraphic.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:graphic_list'))


###########################
# 4 - Core Family Class   #
###########################

class CreateCoreFamily(LoginRequiredMixin, HasRoleMixin, CreateView):
    template_name = "shop/cpu/string_form.html"
    model = CoreFamily
    success_url = reverse_lazy("tienda:coreFamy_list")
    form_class = CoreFamilyForm
    allowed_roles = ['admin']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar Generación CPU"
        return context


class ListCoreFamily(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/params_string_list.html"
    model = CoreFamily

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = "tienda:coreFamy_update"
        context['add'] = "tienda:coreFamy_add"
        context['delete'] = "tienda:coreFamy_eliminar"

        return context


class UpdateCoreFamily(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/string_form.html"
    model = CoreFamily
    form_class = CoreFamilyForm
    success_url = reverse_lazy('tienda:coreFamy_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar Generación CPU"
        return context


@login_required
def CoreFamilyEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            CoreFamily.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:coreFamy_list'))

###########################
# 5 - CPU Class           #
###########################


class CreateCPU(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:front_panel_list")
    template_name = "shop/cpu/cpu_form.html"
    model = CPU
    form_class = CPUForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Adicionar CPU"

        return context


class ListCPU(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = ['admin']
    template_name = "shop/cpu/cpu_list.html"
    model = CPU

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UpdateCPU(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = ['admin']
    success_url = reverse_lazy("tienda:cpu_list")
    template_name = "shop/cpu/cpu_form.html"
    model = CPU
    form_class = CPUForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Modificar CPU"
        return context


@login_required
def CPUEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            CPU.objects.filter(id=dat).delete()
    return redirect(reverse_lazy('tienda:cpu_list'))


################################
# 6- AJAX Petition             #
################################

@login_required
def AvailableCPU(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        gpu = CPU.objects.get(id=item_id)
        gpu.available = False if (gpu.available == True) else True
        gpu.save()
        data = {
            'available': gpu.available,
        }
        return JsonResponse(data)

    else:
        return HttpResponse("Bad!")

@login_required
def DetailCPU(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        cpu = CPU.objects.get(id=item_id)
        data = {
            "nb": cpu.nombre,
            "slug": cpu.slug,
            "available": cpu.available,
            "tags" : cpu.Tags(),
            "category": cpu.category.nombre,
            "precio": cpu.precio,
            "precio_descuento": cpu.precioDescuento(),
            "img": cpu.photo.url,
            "shipping": cpu.shipping.nombre,
            "manufacturer": cpu.manufacturer.nombre,
            "socket" : cpu.socket.nombre,
            "coreCount" : cpu.coreCount,
            "coreClok" : cpu.coreClok,
            "tdp" : cpu.tdp,
            "serie" : cpu.serie.nombre,
            "microArch" : cpu.microArch.nombre,
            "coreFamy" : cpu.coreFamy.nombre,
            "graphics" : cpu.graphics.nombre,
            "suportECC" : cpu.suportECC,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")