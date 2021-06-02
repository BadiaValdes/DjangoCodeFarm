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
from cart.models import Cart, ListaDeseos, Order
############### ENDS MODEL IMPORT ###############

############### UTIL IMPORT ###################

############### ENDS UTIL IMPORT ##############

############### OTHER IMPORT #####################
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
############### ENDS OTHER IMPORT ################

class ListaCompraList(LoginRequiredMixin, ListView):
    template_name = "shop/product/product_list.html"


