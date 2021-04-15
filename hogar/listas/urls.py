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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views2 import tipo, state, list, item

app_name = "lista"

urlpatterns = [
    # list
    path('', views.index, name='lista'),
    path('add', list.ListaCreateView.as_view(), name='lista_add'),
    path('delete', list.ListaEliminar, name='lista_eliminar'),
    path('detail_list/item', item.ItemDetail, name="item_details"),
    re_path('eliminar_lista/(?P<pk>[0-9a-f]{32})', list.ListaDeleteView.as_view(), name='lista_delete'),
    re_path('update_lista/(?P<pk>[0-9a-f]{32})', list.ListaUpdateView.as_view(), name='lista_update'),
    re_path('detail_list/(?P<pk>[0-9a-f]{32})', list.ListaDetailView.as_view(), name='lista_details'),

    # item
    re_path('item/add/(?P<pk>[0-9a-f]{32})', item.ItemCreateView.as_view(), name='item_add'),

    # path('item/add', item.ItemCreateView.as_view(), name='item_add'),
    path('item/delete', item.ItemEliminar, name='item_eliminar'),
    re_path('item/eliminar/(?P<pk>[0-9a-f]{32})', item.ItemDeleteView.as_view(), name='item_delete'),
    re_path('item/update/(?P<pk>[0-9a-f]{32})', item.ItemUpdateView.as_view(), name='item_update'),
    re_path('item/state/(?P<pk_item>[0-9a-f]{32})/(?P<pk_state>[0-9a-f]{32})', views.change_sate,
            name='item_change'),
    re_path('item/state2/(?P<pk_list>[0-9a-f]{32})/(?P<pk_item>[0-9a-f]{32})/(?P<pk_state>[0-9a-f]{32})',
            views.change_sate_details,
            name='item_change_details'),

    # tipo
    path('tipo/add', tipo.TipoCreateView.as_view(), name='tipo_add'),
    path('tipo/', tipo.TipoListView.as_view(), name='tipo_list'),
    path('tipo/delete', tipo.TipoEliminar, name='tipo_eliminar'),
    re_path('tipo/eliminar/(?P<pk>[0-9a-f]{32})', tipo.TipoDeleteView.as_view(), name='tipo_delete'),
    re_path('tipo/update/(?P<pk>[0-9a-f]{32})', tipo.TipoUpdateView.as_view(), name='tipo_update'),

    # state
    path('state/add', state.StateCreateView.as_view(), name='state_add'),
    path('state/', state.StateListView.as_view(), name='state_list'),
    path('state/delete', state.StateEliminar, name='state_eliminar'),
    re_path('state/eliminar/(?P<pk>[0-9a-f]{32})', state.StateDeleteView.as_view(), name='state_delete'),
    re_path('state/update/(?P<pk>[0-9a-f]{32})', state.StateUpdateView.as_view(), name='state_update'),
]
