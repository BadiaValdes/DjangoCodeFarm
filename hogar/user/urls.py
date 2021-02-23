"""hogar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('list/', views.UserListView.as_view(), name='list'),
                  path('add/', views.UserAddView.as_view(), name='add'),
                  path('del/', views.UserEliminar, name='del'),
                  re_path('info/(?P<pk>[0-9a-f]{32})', views.UserDetailView.as_view(), name='info'),
                  re_path('mod/(?P<pk>[0-9a-f]{32})', views.UserUpdateView.as_view(), name='mod'),
                  re_path('admin/(?P<pk>[0-9a-f]{32})', views.UserAdminUpdateView.as_view(), name='modadmin'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
