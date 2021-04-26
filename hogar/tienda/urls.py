from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from . import views
from .views_ext import category, shipping, tags, sli, typeMemory, chipset, color, socket, typeProduct, formFactor, manufacturer

app_name = "tienda"

urlpatterns = [
    path('', views.index, name='index'),

    # Category
    # path('category/<slug:slug>', ,name="category")
    path('category/', category.ListCategory.as_view(), name="category_list"),
    path('category/add', category.CreateCategory.as_view(), name="category_add"),
    re_path('category/update/(?P<pk>[0-9a-f]{10})', category.UpdateCategory.as_view(), name="category_update"),
    path('category/delete', category.ItemEliminar, name="category_eliminar"),

    # Shipping
    path('shipping/', shipping.ListShipping.as_view(), name="shipping_list"),
    path('shipping/add', shipping.CreateShipping.as_view(), name="shipping_add"),
    re_path('shipping/update/(?P<pk>[0-9a-f]{10})', shipping.UpdateShipping.as_view(), name="shipping_update"),
    path('shipping/delete', shipping.ItemEliminar, name="shipping_eliminar"),

    # Tags
    path('tags/', tags.ListTags.as_view(), name="tags_list"),
    path('tags/add', tags.CreateTags.as_view(), name="tags_add"),
    re_path('tags/update/(?P<pk>[0-9a-f]{10})', tags.UpdateTags.as_view(), name="tags_update"),
    path('tags/delete', tags.ItemEliminar, name="tags_eliminar"),

    # Case

    # CPU

    # GPU

    # Motherboard

    # Fan

    # RAM

    #### COMMON ####

    # SLI
    path('sli/', sli.ListSLI.as_view(), name="sli_list"),
    path('sli/add', sli.CreateSLI.as_view(), name="sli_add"),
    re_path('sli/update/(?P<pk>[0-9a-f]{10})', sli.UpdateSLI.as_view(), name="sli_update"),
    path('sli/delete', sli.ItemEliminar, name="sli_eliminar"),

    # Type memory
    path('type_memory/', typeMemory.ListTypeMemory.as_view(), name="type_memory_list"),
    path('type_memory/add', typeMemory.CreateTypeMemory.as_view(), name="type_memory_add"),
    re_path('type_memory/update/(?P<pk>[0-9a-f]{10})', typeMemory.UpdateTypeMemory.as_view(),
            name="type_memory_update"),
    path('type_memory/delete', typeMemory.ItemEliminar, name="type_memory_eliminar"),

    # Chipset
    path('chipset/', chipset.ListChipset.as_view(), name="chipset_list"),
    path('chipset/add', chipset.CreateChipset.as_view(), name="chipset_add"),
    re_path('chipset/update/(?P<pk>[0-9a-f]{10})', chipset.UpdateChipset.as_view(), name="chipset_update"),
    path('chipset/delete', chipset.ItemEliminar, name="chipset_eliminar"),

    # Color
    path('color/', color.ListColor.as_view(), name="color_list"),
    path('color/add', color.CreateColor.as_view(), name="color_add"),
    re_path('color/update/(?P<pk>[0-9a-f]{10})', color.UpdateColor.as_view(), name="color_update"),
    path('color/delete', color.ItemEliminar, name="color_eliminar"),

    # Socket
    path('socket/', socket.ListSocket.as_view(), name="socket_list"),
    path('socket/add', socket.CreateSocket.as_view(), name="socket_add"),
    re_path('socket/update/(?P<pk>[0-9a-f]{10})', socket.UpdateSocket.as_view(), name="socket_update"),
    path('socket/delete', socket.ItemEliminar, name="socket_eliminar"),

    # Type Product
    path('type_product/', typeProduct.ListTypeProduct.as_view(), name="type_product_list"),
    path('type_product/add', typeProduct.CreateTypeProduct.as_view(), name="type_product_add"),
    re_path('type_product/update/(?P<pk>[0-9a-f]{10})', typeProduct.UpdateTypeProduct.as_view(), name="type_product_update"),
    path('type_product/delete', typeProduct.ItemEliminar, name="type_product_eliminar"),

    # Form Factor
    path('form_factor/', formFactor.ListFormFactor.as_view(), name="form_factor_list"),
    path('form_factor/add', formFactor.CreateFormFactor.as_view(), name="form_factor_add"),
    re_path('form_factor/update/(?P<pk>[0-9a-f]{10})', formFactor.UpdateFormFactor.as_view(),
            name="form_factor_update"),
    path('form_factor/delete', formFactor.ItemEliminar, name="form_factor_eliminar"),

    # Manufacturer
    path('manufacturer/', manufacturer.ListManufacturer.as_view(), name="manufacturer_list"),
    path('manufacturer/add', manufacturer.CreateManufacturer.as_view(), name="manufacturer_add"),
    re_path('manufacturer/update/(?P<pk>[0-9a-f]{10})', manufacturer.UpdateManufacturer.as_view(),
            name="manufacturer_update"),
    path('manufacturer/delete', manufacturer.ItemEliminar, name="manufacturer_eliminar"),
]
