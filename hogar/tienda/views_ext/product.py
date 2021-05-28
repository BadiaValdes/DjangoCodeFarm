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
from tienda.models import MotherBoard, Category, RAM, Shipping, CPU, Producto, Case, Tags, GPU
############### ENDS MODEL IMPORT ###############

############### UTIL IMPORT ###################
from tienda.util import getModel
############### ENDS UTIL IMPORT ##############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


############### ENDS OTHER IMPORT ################

class ListProduct(LoginRequiredMixin, ListView):
    template_name = "shop/product/product_list.html"
    model = MotherBoard

    def get_context_data(self, *, object_list=None, **kwargs):
        slug = self.kwargs['slug']
        print(slug)
        context = super().get_context_data(**kwargs)
        context['product'] = Producto.objects.filter(category__slug=slug)
        return context


def ProductInfo(request, **kwargs):
    category = Producto.objects.get(slug__exact=kwargs.get('slug1'))

    model, render_to_page = getModel(category.category.nombre)

    obj = get_object_or_404(model, slug=kwargs.get('slug1'))

    data = {
        'model': obj,
        'renderToPage': render_to_page,
    }

    return render(request, '../templates/shop/product/product_info.html', data)
