from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from . import views
from .views_ext import category, shipping, tags, sli, typeMemory, chipset, color, socket, typeProduct, formFactor, \
    manufacturer, case, gpu, autocomplete, cpu, motherboard, ram, product

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
#       5.1- Serie                   #
#       5.2- Micro Arquitectura      #
#       5.3- Integrate Graphic       #
#       5.4- Core Family             #
#   6- GPU                           #
#       6.1- INTERFACE               #
#       6.2- FRAME SYNC              #
#       6.3- COOLING                 #
#       6.4- EXTERNAL POWER          #
#   7- MOTHERBOARD                   #
#       7.1- Ethernet                #
#       7.2- Wireless                #
#   8- FAN                           #
#   9- RAM                           #
#       9.1- TiemposRAM              #
#       9.2- ECCRAM                  #
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
#   12- CAR                          #
#   13- Products                     #
#                                    #
######################################

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    ######################################################################################################
    # 1- Category
    # path('category/<slug:slug>', ,name="category")
    path('dashboard/category/', category.ListCategory.as_view(), name="category_list"),
    path('dashboard/category/add', category.CreateCategory.as_view(), name="category_add"),
    re_path('dashboard/category/update/(?P<pk>[0-9a-f]{10})', category.UpdateCategory.as_view(), name="category_update"),
    path('dashboard/category/delete', category.ItemEliminar, name="category_eliminar"),

    ######################################################################################################

    # 2- Shipping
    path('dashboard/shipping/', shipping.ListShipping.as_view(), name="shipping_list"),
    path('dashboard/shipping/add', shipping.CreateShipping.as_view(), name="shipping_add"),
    re_path('dashboard/shipping/update/(?P<pk>[0-9a-f]{10})', shipping.UpdateShipping.as_view(), name="shipping_update"),
    path('dashboard/shipping/delete', shipping.ItemEliminar, name="shipping_eliminar"),

    ######################################################################################################

    # 3- Tags
    path('dashboard/tags/', tags.ListTags.as_view(), name="tags_list"),
    path('dashboard/tags/add', tags.CreateTags.as_view(), name="tags_add"),
    re_path('dashboard/tags/update/(?P<pk>[0-9a-f]{10})', tags.UpdateTags.as_view(), name="tags_update"),
    path('dashboard/tags/delete', tags.ItemEliminar, name="tags_eliminar"),

    ######################################################################################################

    # 4- Case
    path('dashboard/case/', case.ListCase.as_view(), name="case_list"),
    path('dashboard/case/details', case.CaseDetail, name="case_details"),
    path('dashboard/case/add', case.CreateCase.as_view(), name="case_add"),
    re_path('dashboard/case/update/(?P<pk>[0-9a-f]{10})', case.UpdateCase.as_view(), name="case_update"),
    path('dashboard/case/delete', case.EliminarCase, name="case_eliminar"),

    # 4.1- TYPE CASE
    path('dashboard/type_case/', case.ListTypeCase.as_view(), name="type_case_list"),
    path('dashboard/type_case/add', case.CreateTypeCase.as_view(), name="type_case_add"),
    re_path('dashboard/type_case/update/(?P<pk>[0-9a-f]{10})', case.UpdateTypeCase.as_view(), name="type_case_update"),
    path('dashboard/type_case/delete', case.ItemEliminar, name="type_case_eliminar"),

    # 4.2- Power Supply
    path('dashboard/power_supply/', case.ListPowerSupply.as_view(), name="power_supply_list"),
    path('dashboard/power_supply/add', case.CreatePowerSupply.as_view(), name="power_supply_add"),
    re_path('dashboard/power_supply/update/(?P<pk>[0-9a-f]{10})', case.UpdatePowerSupply.as_view(), name="power_supply_update"),
    path('dashboard/power_supply/delete', case.EliminarPowerSupply, name="power_supply_eliminar"),

    # 4.3- Side Panel Window
    path('dashboard/side_panel/', case.ListSidePanelWindow.as_view(), name="side_panel_list"),
    path('dashboard/side_panel/add', case.CreateSidePanelWindow.as_view(), name="side_panel_add"),
    re_path('dashboard/side_panel/update/(?P<pk>[0-9a-f]{10})', case.UpdateSidePanelWindow.as_view(), name="side_panel_update"),
    path('dashboard/side_panel/delete', case.EliminarSidePanelWindow, name="side_panel_eliminar"),

    # 4.4- Front Panel USB
    path('dashboard/front_panel/', case.ListFrontPanelUSB.as_view(), name="front_panel_list"),
    path('dashboard/front_panel/add', case.CreateFrontPanelUSB.as_view(), name="front_panel_add"),
    re_path('dashboard/front_panel/update/(?P<pk>[0-9a-f]{10})', case.UpdateFrontPanelUSB.as_view(), name="front_panel_update"),
    path('dashboard/front_panel/delete', case.EliminarFrontPanelUSB, name="front_panel_eliminar"),

    ######################################################################################################
    # 5- CPU
    path('dashboard/cpu/', cpu.ListCPU.as_view(), name="cpu_list"),
    path('dashboard/cpu/add', cpu.CreateCPU.as_view(), name="cpu_add"),
    re_path('dashboard/cpu/update/(?P<pk>[0-9a-f]{10})', cpu.UpdateCPU.as_view(), name="cpu_update"),
    path('dashboard/cpu/delete', cpu.CPUEliminar, name="cpu_eliminar"),
    path('dashboard/cpu/available', cpu.AvailableCPU, name="cpu_available"),
    path('dashboard/cpu/details', cpu.DetailCPU, name="cpu_detail"),

    # 5.1- Serie
    path('dashboard/serie/', cpu.ListSerie.as_view(), name="serie_list"),
    path('dashboard/serie/add', cpu.CreateSerie.as_view(), name="serie_add"),
    re_path('dashboard/serie/update/(?P<pk>[0-9a-f]{10})', cpu.UpdateSerie.as_view(), name="serie_update"),
    path('dashboard/serie/delete', cpu.SerieEliminar, name="serie_eliminar"),

    # 5.2- Micro Arquitectura
    path('dashboard/microArch/', cpu.ListMicroArch.as_view(), name="microArch_list"),
    path('dashboard/microArch/add', cpu.CreateMicroArch.as_view(), name="microArch_add"),
    re_path('dashboard/microArch/update/(?P<pk>[0-9a-f]{10})', cpu.UpdateMicroArch.as_view(), name="microArch_update"),
    path('dashboard/microArch/delete', cpu.MicroArchEliminar, name="microArch_eliminar"),

    # 5.3- Integrate Graphic
    path('dashboard/graphic/', cpu.ListIntegrateGraphic.as_view(), name="graphic_list"),
    path('dashboard/graphic/add', cpu.CreateIntegrateGraphic.as_view(), name="graphic_add"),
    re_path('dashboard/graphic/update/(?P<pk>[0-9a-f]{10})', cpu.UpdateIntegrateGraphic.as_view(), name="graphic_update"),
    path('dashboard/graphic/delete', cpu.IntegrateGraphicEliminar, name="graphic_eliminar"),

    # 5.4- Core Family
    path('dashboard/coreFamily/', cpu.ListCoreFamily.as_view(), name="coreFamy_list"),
    path('dashboard/coreFamily/add', cpu.CreateCoreFamily.as_view(), name="coreFamy_add"),
    re_path('dashboard/coreFamily/update/(?P<pk>[0-9a-f]{10})', cpu.UpdateCoreFamily.as_view(), name="coreFamy_update"),
    path('dashboard/coreFamily/delete', cpu.CoreFamilyEliminar, name="coreFamy_eliminar"),

    ######################################################################################################
    # 6- GPU
    path('dashboard/gpu/', gpu.ListGPU.as_view(), name="gpu_list"),
    path('dashboard/gpu/add', gpu.CreateGPU.as_view(), name="gpu_add"),
    re_path('dashboard/gpu/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateGPU.as_view(), name="gpu_update"),
    path('dashboard/gpu/delete', gpu.EliminarGPU, name="gpu_eliminar"),
    path('dashboard/gpu/available', gpu.AvailableGPU, name="gpu_available"),
    path('dashboard/gpu/details', gpu.GPUDetail, name="gpu_details"),

    # 6.1- Interface
    path('dashboard/interface/', gpu.ListInterface.as_view(), name="interface_list"),
    path('dashboard/interface/add', gpu.CreateInterface.as_view(), name="interface_add"),
    re_path('dashboard/interface/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateInterface.as_view(), name="interface_update"),
    path('dashboard/interface/delete', gpu.ItemEliminar, name="interface_eliminar"),

    # 6.2- Frame Sync
    path('dashboard/frame_sync/', gpu.ListFrameSync.as_view(), name="frame_sync_list"),
    path('dashboard/frame_sync/add', gpu.CreateFrameSync.as_view(), name="frame_sync_add"),
    re_path('dashboard/frame_sync/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateFrameSync.as_view(), name="frame_sync_update"),
    path('dashboard/frame_sync/delete', gpu.EliminarFrameSync, name="frame_sync_eliminar"),

    # 6.3- Cooling
    path('dashboard/cooling/', gpu.ListCooling.as_view(), name="cooling_list"),
    path('dashboard/cooling/add', gpu.CreateCooling.as_view(), name="cooling_add"),
    re_path('dashboard/cooling/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateCooling.as_view(), name="cooling_update"),
    path('dashboard/cooling/delete', gpu.EliminarCooling, name="cooling_eliminar"),

    # 6.4- External Power
    path('dashboard/external_power/', gpu.ListExternalPower.as_view(), name="external_power_list"),
    path('dashboard/external_power/add', gpu.CreateExternalPower.as_view(), name="external_power_add"),
    re_path('dashboard/external_power/update/(?P<pk>[0-9a-f]{10})', gpu.UpdateExternalPower.as_view(),
            name="external_power_update"),
    path('dashboard/external_power/delete', gpu.EliminarExternalPower, name="external_power_eliminar"),

    ######################################################################################################
    # 7- Motherboard
    path('dashboard/motherboard/', motherboard.ListMotherBoard.as_view(), name="motherboard_list"),
    path('dashboard/motherboard/add', motherboard.CreateMotherBoard.as_view(), name="motherboard_add"),
    re_path('dashboard/motherboard/update/(?P<pk>[0-9a-f]{10})', motherboard.UpdateMotherBoard.as_view(),
            name="motherboard_update"),
    path('dashboard/motherboard/delete', motherboard.MotherBoardEliminar, name="motherboard_eliminar"),
    path('dashboard/motherboard/available', motherboard.AvailableMotherboard, name="motherboard_available"),
    path('dashboard/motherboard/details', motherboard.MotherboardDetail, name="motherboard_details"),

    # 7.1- Ethernet
    path('dashboard/ethernet/', motherboard.ListEthernet.as_view(), name="ethernet_list"),
    path('dashboard/ethernet/add', motherboard.CreateEthernet.as_view(), name="ethernet_add"),
    re_path('dashboard/ethernet/update/(?P<pk>[0-9a-f]{10})', motherboard.UpdateEthernet.as_view(), name="ethernet_update"),
    path('dashboard/ethernet/delete', motherboard.EthernetEliminar, name="ethernet_eliminar"),

    # 7.2- Wireless
    path('dashboard/wireless/', motherboard.ListWireless.as_view(), name="wireless_list"),
    path('dashboard/wireless/add', motherboard.CreateWireless.as_view(), name="wireless_add"),
    re_path('dashboard/wireless/update/(?P<pk>[0-9a-f]{10})', motherboard.UpdateWireless.as_view(), name="wireless_update"),
    path('dashboard/wireless/delete', motherboard.WirelessEliminar, name="wireless_eliminar"),

    ######################################################################################################
    # 8- Fan
    ######################################################################################################
    # 9- RAM
    path('dashboard/ram/', ram.ListRAM.as_view(), name="ram_list"),
    path('dashboard/ram/add', ram.CreateRAM.as_view(), name="ram_add"),
    re_path('dashboard/ram/update/(?P<pk>[0-9a-f]{10})', ram.UpdateRAM.as_view(),
            name="ram_update"),
    path('dashboard/ram/delete', ram.RAMEliminar, name="ram_eliminar"),
    # path('motherboard/available', motherboard.AvailableMotherboard, name="motherboard_available"),
    # path('motherboard/details', motherboard.MotherboardDetail, name="motherboard_details"),

    # 9.1- TiemposRAM
    path('dashboard/tiemposRAM/', ram.ListTiemposRAM.as_view(), name="tiempos_ram_list"),
    path('dashboard/tiemposRAM/add', ram.CreateTiemposRAM.as_view(), name="tiempos_ram_add"),
    re_path('dashboard/tiemposRAM/update/(?P<pk>[0-9a-f]{10})', ram.UpdateTiemposRAM.as_view(), name="tiempos_ram_update"),
    path('dashboard/tiemposRAM/delete', ram.TiemposRAMEliminar, name="tiempos_ram_eliminar"),

    # 9.2- ECCRAM
    path('dashboard/eccRAM/', ram.ListECCRAM.as_view(), name="ecc_ram_list"),
    path('dashboard/eccRAM/add', ram.CreateECCRAM.as_view(), name="ecc_ram_add"),
    re_path('dashboard/eccRAM/update/(?P<pk>[0-9a-f]{10})', ram.UpdateECCRAM.as_view(), name="ecc_ram_update"),
    path('dashboard/eccRAM/delete', ram.ECCRAMEliminar, name="ecc_ram_eliminar"),

    ######################################################################################################
    # 10- COMMON

    # 10.1- SLI
    path('dashboard/sli/', sli.ListSLI.as_view(), name="sli_list"),
    path('dashboard/sli/add', sli.CreateSLI.as_view(), name="sli_add"),
    re_path('dashboard/sli/update/(?P<pk>[0-9a-f]{10})', sli.UpdateSLI.as_view(), name="sli_update"),
    path('dashboard/sli/delete', sli.ItemEliminar, name="sli_eliminar"),

    # 10.2- Type memory
    path('dashboard/type_memory/', typeMemory.ListTypeMemory.as_view(), name="type_memory_list"),
    path('dashboard/type_memory/add', typeMemory.CreateTypeMemory.as_view(), name="type_memory_add"),
    re_path('dashboard/type_memory/update/(?P<pk>[0-9a-f]{10})', typeMemory.UpdateTypeMemory.as_view(),
            name="type_memory_update"),
    path('dashboard/type_memory/delete', typeMemory.ItemEliminar, name="type_memory_eliminar"),

    # 10.3- Chipset
    path('dashboard/chipset/', chipset.ListChipset.as_view(), name="chipset_list"),
    path('dashboard/chipset/add', chipset.CreateChipset.as_view(), name="chipset_add"),
    re_path('dashboard/chipset/update/(?P<pk>[0-9a-f]{10})', chipset.UpdateChipset.as_view(), name="chipset_update"),
    path('dashboard/chipset/delete', chipset.ItemEliminar, name="chipset_eliminar"),

    # 10.4- Color
    path('dashboard/color/', color.ListColor.as_view(), name="color_list"),
    path('dashboard/color/add', color.CreateColor.as_view(), name="color_add"),
    re_path('dashboard/color/update/(?P<pk>[0-9a-f]{10})', color.UpdateColor.as_view(), name="color_update"),
    path('dashboard/color/delete', color.ItemEliminar, name="color_eliminar"),

    # 10.5- Socket
    path('dashboard/socket/', socket.ListSocket.as_view(), name="socket_list"),
    path('dashboard/socket/add', socket.CreateSocket.as_view(), name="socket_add"),
    re_path('dashboard/socket/update/(?P<pk>[0-9a-f]{10})', socket.UpdateSocket.as_view(), name="socket_update"),
    path('dashboard/socket/delete', socket.ItemEliminar, name="socket_eliminar"),

    # 10.6- Type Product
    path('dashboard/type_product/', typeProduct.ListTypeProduct.as_view(), name="type_product_list"),
    path('dashboard/type_product/add', typeProduct.CreateTypeProduct.as_view(), name="type_product_add"),
    re_path('dashboard/type_product/update/(?P<pk>[0-9a-f]{10})', typeProduct.UpdateTypeProduct.as_view(),
            name="type_product_update"),
    path('dashboard/type_product/delete', typeProduct.ItemEliminar, name="type_product_eliminar"),

    # 10.7- Form Factor
    path('dashboard/form_factor/', formFactor.ListFormFactor.as_view(), name="form_factor_list"),
    path('dashboard/form_factor/add', formFactor.CreateFormFactor.as_view(), name="form_factor_add"),
    re_path('dashboard/form_factor/update/(?P<pk>[0-9a-f]{10})', formFactor.UpdateFormFactor.as_view(),
            name="form_factor_update"),
    path('dashboard/form_factor/delete', formFactor.ItemEliminar, name="form_factor_eliminar"),

    # 10.8- Manufacturer
    path('dashboard/manufacturer/', manufacturer.ListManufacturer.as_view(), name="manufacturer_list"),
    path('dashboard/manufacturer/add', manufacturer.CreateManufacturer.as_view(), name="manufacturer_add"),
    re_path('dashboard/manufacturer/update/(?P<pk>[0-9a-f]{10})', manufacturer.UpdateManufacturer.as_view(),
            name="manufacturer_update"),
    path('dashboard/manufacturer/delete', manufacturer.ItemEliminar, name="manufacturer_eliminar"),

    ######################################################################################################
    # 11- Auto Complete URL

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
    re_path('serieAutoComplete/', autocomplete.SerieAutoComplete.as_view(),
            name="ac_serie"),
    re_path('microArchAutoComplete/', autocomplete.MicroArchAutoComplete.as_view(),
            name="ac_microArch"),
    re_path('graphicAutoComplete/', autocomplete.IntegrateGraphicAutoComplete.as_view(),
            name="ac_graphics"),
    re_path('coreFamilyAutoComplete/', autocomplete.CoreFamilyAutoComplete.as_view(),
            name="ac_coreFamy"),
    re_path('socketAutoComplete/', autocomplete.SocketAutoComplete.as_view(),
            name="ac_socket"),
    re_path('ethernetAutoComplete/', autocomplete.EthernetAutoComplete.as_view(),
            name="ac_ethernet"),
    re_path('wirelessAutoComplete/', autocomplete.WirelessAutoComplete.as_view(),
            name="ac_wireless"),
    re_path('ecc/', autocomplete.ECCAutoComplete.as_view(),
            name="ac_ecc"),
    re_path('tiempos/', autocomplete.TiemposRAMAutoComplete.as_view(),
            name="ac_tiempos"),

    ######################################################################################################
    # 12- CAR

    ######################################################################################################
    # 13- Product
    path('categoria/<slug:slug>', product.ListProduct.as_view(), name="product_list"),
    path('<slug:slug>/<slug:slug1>', product.ProductInfo, name="product_info"),
    path('tags/<str:tags>/', product.ProductTags, name="product_tags"),
]
