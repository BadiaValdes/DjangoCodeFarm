from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from . import views
from .views_ext import category, shipping, tags, sli, typeMemory, chipset, color, socket, typeProduct, formFactor, \
    manufacturer, case, gpu, autocomplete

app_name = "tienda"

######################################
#            Navegacion              #
#                                    #
#   1- CATEGORY                      #
#   2- SHIPPING                      #
#   3- TAGS                          #
#   4- CASE                          #
#       4.1- TYPE CASE               #
#       4.2- POWER SUPPLY            #
#       4.3- SIDE PANEL WINDOW       #
#       4.4- FRONT PANEL USB         #
#   5- CPU                           #
#   6- GPU                           #
#       6.1- INTERFACE               #
#       6.2- FRAME SYNC              #
#       6.3- COOLING                 #
#       6.4- EXTERNAL POWER          #
#   7- MOTHERBOARD                   #
#   8- FAN                           #
#   9- RAM                           #
#   10- COMMON                       #
#       10.1- SLI                    #
#       10.2- TYPE MEMORY            #
#       10.3- CHIPSET                #
#       10.4- COLOR                  #
#       10.5- SOCKET                 #
#       10.6- TYPE PRODUCT           #
#       10.7- FORM FACTORY           #
#       10.8- MANUFACTURER           #
#   11- AUTO COMPLETE URL            #
######################################

urlpatterns = [
    path('', views.index, name='index'),

    ######################################################################################################
    # 1- Category
    # path('category/<slug:slug>', ,name="category")
    path('category/', category.ListCategory.as_view(), name="category_list"),
    path('category/add', category.CreateCategory.as_view(), name="category_add"),
    re_path('category/update/(?P<pk>[0-9a-f]{10})', category.UpdateCategory.as_view(), name="category_update"),
    path('category/delete', category.ItemEliminar, name="category_eliminar"),

    ######################################################################################################

    # 2- Shipping
    path('shipping/', shipping.ListShipping.as_view(), name="shipping_list"),
    path('shipping/add', shipping.CreateShipping.as_view(), name="shipping_add"),
    re_path('shipping/update/(?P<pk>[0-9a-f]{10})', shipping.UpdateShipping.as_view(), name="shipping_update"),
    path('shipping/delete', shipping.ItemEliminar, name="shipping_eliminar"),

    ######################################################################################################

    # 3- Tags
    path('tags/', tags.ListTags.as_view(), name="tags_list"),
    path('tags/add', tags.CreateTags.as_view(), name="tags_add"),
    re_path('tags/update/(?P<pk>[0-9a-f]{10})', tags.UpdateTags.as_view(), name="tags_update"),
    path('tags/delete', tags.ItemEliminar, name="tags_eliminar"),

    ######################################################################################################

    # 4- Case
    path('case/', case.ListCase.as_view(), name="case_list"),
    path('case/details', case.CaseDetail, name="case_details"),
    path('case/add', case.CreateCase.as_view(), name="case_add"),
    re_path('case/update/(?P<pk>[0-9a-f]{10})', case.UpdateCase.as_view(), name="case_update"),
    path('case/delete', case.EliminarCase, name="case_eliminar"),

    # 4.1- TYPE CASE
    path('type_case/', case.ListTypeCase.as_view(), name="type_case_list"),
    path('type_case/add', case.CreateTypeCase.as_view(), name="type_case_add"),
    re_path('type_case/update/(?P<pk>[0-9a-f]{10})', case.UpdateTypeCase.as_view(), name="type_case_update"),
    path('type_case/delete', case.ItemEliminar, name="type_case_eliminar"),

    # 4.2- Power Supply
    path('power_supply/', case.ListPowerSupply.as_view(), name="power_supply_list"),
    path('power_supply/add', case.CreatePowerSupply.as_view(), name="power_supply_add"),
    re_path('power_supply/update/(?P<pk>[0-9a-f]{10})', case.UpdatePowerSupply.as_view(), name="power_supply_update"),
    path('power_supply/delete', case.EliminarPowerSupply, name="power_supply_eliminar"),

    # 4.3- Side Panel Window
    path('side_panel/', case.ListSidePanelWindow.as_view(), name="side_panel_list"),
    path('side_panel/add', case.CreateSidePanelWindow.as_view(), name="side_panel_add"),
    re_path('side_panel/update/(?P<pk>[0-9a-f]{10})', case.UpdateSidePanelWindow.as_view(), name="side_panel_update"),
    path('side_panel/delete', case.EliminarSidePanelWindow, name="side_panel_eliminar"),

    # 4.4- Front Panel USB
    path('front_panel/', case.ListFrontPanelUSB.as_view(), name="front_panel_list"),
    path('front_panel/add', case.CreateFrontPanelUSB.as_view(), name="front_panel_add"),
    re_path('front_panel/update/(?P<pk>[0-9a-f]{10})', case.UpdateFrontPanelUSB.as_view(), name="front_panel_update"),
    path('front_panel/delete', case.EliminarFrontPanelUSB, name="front_panel_eliminar"),

    ######################################################################################################
    # 5- CPU
    ######################################################################################################
    # 6- GPU
    path('gpu/', gpu.ListGPU.as_view(), name="gpu_list"),
    path('gpu/add', gpu.CreateGPU.as_view(), name="gpu_add"),
    re_path('gpu/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateGPU.as_view(), name="gpu_update"),
    path('gpu/delete', gpu.EliminarGPU, name="gpu_eliminar"),

    # 6.1- Interface
    path('interface/', gpu.ListInterface.as_view(), name="interface_list"),
    path('interface/add', gpu.CreateInterface.as_view(), name="interface_add"),
    re_path('interface/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateInterface.as_view(), name="interface_update"),
    path('interface/delete', gpu.ItemEliminar, name="interface_eliminar"),

    # 6.2- Frame Sync
    path('frame_sync/', gpu.ListFrameSync.as_view(), name="frame_sync_list"),
    path('frame_sync/add', gpu.CreateFrameSync.as_view(), name="frame_sync_add"),
    re_path('frame_sync/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateFrameSync.as_view(), name="frame_sync_update"),
    path('frame_sync/delete', gpu.EliminarFrameSync, name="frame_sync_eliminar"),

    # 6.3- Cooling
    path('cooling/', gpu.ListCooling.as_view(), name="cooling_list"),
    path('cooling/add', gpu.CreateCooling.as_view(), name="cooling_add"),
    re_path('cooling/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateCooling.as_view(), name="cooling_update"),
    path('cooling/delete', gpu.EliminarCooling, name="cooling_eliminar"),

    # 6.4- External Power
    path('external_power/', gpu.ListExternalPower.as_view(), name="external_power_list"),
    path('external_power/add', gpu.CreateExternalPower.as_view(), name="external_power_add"),
    re_path('external_power/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateExternalPower.as_view(),
            name="external_power_update"),
    path('external_power/delete', gpu.EliminarExternalPower, name="external_power_eliminar"),

    ######################################################################################################
    # 7- Motherboard
    ######################################################################################################
    # 8- Fan
    ######################################################################################################
    # 9- RAM
    ######################################################################################################
    # 10- COMMON

    # 10.1- SLI
    path('sli/', sli.ListSLI.as_view(), name="sli_list"),
    path('sli/add', sli.CreateSLI.as_view(), name="sli_add"),
    re_path('sli/update/(?P<pk>[0-9a-f]{10})', sli.UpdateSLI.as_view(), name="sli_update"),
    path('sli/delete', sli.ItemEliminar, name="sli_eliminar"),

    # 10.2- Type memory
    path('type_memory/', typeMemory.ListTypeMemory.as_view(), name="type_memory_list"),
    path('type_memory/add', typeMemory.CreateTypeMemory.as_view(), name="type_memory_add"),
    re_path('type_memory/update/(?P<pk>[0-9a-f]{10})', typeMemory.UpdateTypeMemory.as_view(),
            name="type_memory_update"),
    path('type_memory/delete', typeMemory.ItemEliminar, name="type_memory_eliminar"),

    # 10.3- Chipset
    path('chipset/', chipset.ListChipset.as_view(), name="chipset_list"),
    path('chipset/add', chipset.CreateChipset.as_view(), name="chipset_add"),
    re_path('chipset/update/(?P<pk>[0-9a-f]{10})', chipset.UpdateChipset.as_view(), name="chipset_update"),
    path('chipset/delete', chipset.ItemEliminar, name="chipset_eliminar"),

    # 10.4- Color
    path('color/', color.ListColor.as_view(), name="color_list"),
    path('color/add', color.CreateColor.as_view(), name="color_add"),
    re_path('color/update/(?P<pk>[0-9a-f]{10})', color.UpdateColor.as_view(), name="color_update"),
    path('color/delete', color.ItemEliminar, name="color_eliminar"),

    # 10.5- Socket
    path('socket/', socket.ListSocket.as_view(), name="socket_list"),
    path('socket/add', socket.CreateSocket.as_view(), name="socket_add"),
    re_path('socket/update/(?P<pk>[0-9a-f]{10})', socket.UpdateSocket.as_view(), name="socket_update"),
    path('socket/delete', socket.ItemEliminar, name="socket_eliminar"),

    # 10.6- Type Product
    path('type_product/', typeProduct.ListTypeProduct.as_view(), name="type_product_list"),
    path('type_product/add', typeProduct.CreateTypeProduct.as_view(), name="type_product_add"),
    re_path('type_product/update/(?P<pk>[0-9a-f]{10})', typeProduct.UpdateTypeProduct.as_view(),
            name="type_product_update"),
    path('type_product/delete', typeProduct.ItemEliminar, name="type_product_eliminar"),

    # 10.7- Form Factor
    path('form_factor/', formFactor.ListFormFactor.as_view(), name="form_factor_list"),
    path('form_factor/add', formFactor.CreateFormFactor.as_view(), name="form_factor_add"),
    re_path('form_factor/update/(?P<pk>[0-9a-f]{10})', formFactor.UpdateFormFactor.as_view(),
            name="form_factor_update"),
    path('form_factor/delete', formFactor.ItemEliminar, name="form_factor_eliminar"),

    # 10.8- Manufacturer
    path('manufacturer/', manufacturer.ListManufacturer.as_view(), name="manufacturer_list"),
    path('manufacturer/add', manufacturer.CreateManufacturer.as_view(), name="manufacturer_add"),
    re_path('manufacturer/update/(?P<pk>[0-9a-f]{10})', manufacturer.UpdateManufacturer.as_view(),
            name="manufacturer_update"),
    path('manufacturer/delete', manufacturer.ItemEliminar, name="manufacturer_eliminar"),

    ######################################################################################################

    re_path('categoryAutoComplete/', autocomplete.CategoryAutoComplete.as_view(create_field='nombre'),
            name="ac_category"),
    re_path('shippingAutoComplete/', autocomplete.ShippingAutoComplete.as_view(),
            name="ac_shipping"),
    re_path('tagsAutoComplete/', autocomplete.TagsAutoComplete.as_view(create_field='nombre'),
            name="ac_tags"),
    re_path('manufacturerAutoComplete/', autocomplete.ManufacturerAutoComplete.as_view(),
            name="ac_manufacturer"),
    re_path('typeCaseAutoComplete/', autocomplete.TypeCaseAutoComplete.as_view(),
            name="ac_type_case"),
    re_path('powerSupplyAutoComplete/', autocomplete.PowerSupplyAutoComplete.as_view(),
            name="ac_power_supply"),
    re_path('sidePanelWindowAutoComplete/', autocomplete.SidePanelWindowAutoComplete.as_view(),
            name="ac_side_panel"),
    re_path('frontPanelAutoComplete/', autocomplete.FrontPanelUSBAutoComplete.as_view(),
            name="ac_front_panel"),
    re_path('colorAutoComplete/', autocomplete.ColorAutoComplete.as_view(),
            name="ac_color"),
    re_path('formFactorAutoComplete/', autocomplete.FormFactorAutoComplete.as_view(),
            name="ac_form_factor"),
    re_path('chipsetAutoComplete/', autocomplete.ChipsetAutoComplete.as_view(),
            name="ac_chipset"),
    re_path('typeMemoryAutoComplete/', autocomplete.TypeMemoryAutoComplete.as_view(create_field='nombre'),
            name="ac_type_memory"),
    re_path('interfaceAutoComplete/', autocomplete.InterfaceAutoComplete.as_view(),
            name="ac_interface"),
    re_path('frameSyncAutoComplete/', autocomplete.FrameSyncAutoComplete.as_view(),
            name="ac_frame_sync"),
    re_path('sliAutoComplete/', autocomplete.SLIAutoComplete.as_view(),
            name="ac_sli"),
    re_path('coolingAutoComplete/', autocomplete.CoolingAutoComplete.as_view(),
            name="ac_cooling"),
    re_path('externalPowerAutoComplete/', autocomplete.ExternalPowerAutoComplete.as_view(),
            name="ac_external_power"),
]
