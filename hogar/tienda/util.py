############### MODELS IMPORT ###################
from tienda.models import MotherBoard, Category, RAM, Shipping, CPU, Producto, Case, Tags, GPU
############### ENDS MODEL IMPORT ###############

def getModel (model_name):
    model = {
        'Case': [Case, 'shop/product/partials/_case.html'],
        'Motherboard' : [MotherBoard, 'shop/product/partials/_motherboard.html'],
        'RAM' : [RAM, 'shop/product/partials/_ram.html'],
        'CPU' : [CPU, 'shop/product/partials/_cpu.html'],
        'GPU' : [GPU, 'shop/product/partials/_gpu.html'],
    }

    returned_values = model.get(model_name)

    return  returned_values[0], returned_values[1]



