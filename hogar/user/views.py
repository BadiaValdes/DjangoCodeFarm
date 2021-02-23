from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm, UserUpdateForm, UserUpdateFormAdmin
from rolepermissions.checkers import has_role
from django.contrib.auth.mixins import PermissionRequiredMixin
from rolepermissions.mixins import HasRoleMixin, HasPermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse


# Create your views here.

@login_required()
def index(request):
    return render(request, '../templates/user/profile.html')


class UserAddView(LoginRequiredMixin, CreateView):
    model = User
    template_name = '../templates/user/create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('user:index')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = '../templates/user/modify_user.html'
    success_url = reverse_lazy('user:index')


class UserAdminUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateFormAdmin
    template_name = '../templates/user/modify_user.html'
    success_url = reverse_lazy('user:list')


    def form_valid(self, form):
        self.object.groups.clear()
        for gr in form.data['group']:
            self.object.groups.add(gr)
        return super(UserAdminUpdateView, self).form_valid(form)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def UserEliminar(request):
    if (request.POST.getlist('delete')):
        datos = request.POST.getlist('delete')
        for dat in datos:
            User.objects.filter(id=dat).delete()
    return redirect('/user/list')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_info.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
