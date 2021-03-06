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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import metrics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('almacen/', include('almacen.urls')),
    path('chat/', include('chat.urls')),
    path('compra/', include('compra.urls')),
    path('user/', include('user.urls')),
    path('list/', include('listas.urls')),
    path('economia/', include('economia.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('tienda/', include('tienda.urls')),
    path('metrics/', include('metrics.urls')),
    path('cart/', include('cart.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
