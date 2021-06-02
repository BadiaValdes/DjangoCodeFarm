############### MODELS IMPORT ###################
from cart.models import Cart, ListaDeseos, Order
from django.contrib.auth.decorators import login_required

from tienda.models import Producto

############### ENDS MODEL IMPORT ###############

############### OTROS IMORT ###############
from django.http import JsonResponse, HttpResponse


############### END OTROS IMORT ###########


@login_required
def addToCart(request):
    if request.method == 'GET':
        product = request.GET['product']

        object = Cart.objects.get_or_create(usuario_id=request.user.id, state=0)

        object = Cart.objects.get(id__exact=object[0])

        object.usuario = request.user
        object.save()

        object.products.add(product, through_defaults={'cantidad': 5})

        print(object)

        data = {
            'product': product,
            'ad': True,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")


@login_required
def payOut(request):
    if request.method == 'POST':
        product = request.POST.getlist('product')

        object = Cart.objects.get(usuario_id=request.user.id, state=0)
        order_ticket = Order.objects.create()
        object.state = 1
        object.order = order_ticket[0]

        object.save()

        data = {
            'sold': True,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")

@login_required
def getProductos(request):
    if request.method == 'GET':
        object = Cart.objects.get(usuario_id=request.user.id, state=0)
        product_name=[]
        for obj in object.products.all():
            product_name.append([obj.nombre, obj.precioDescuento(), obj.photo.url, obj.slug])


        print(product_name)

        data = {
            'products' :  product_name

        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")

@login_required
def CartDeleteItem(request):
    if (request.GET['data']):
        datos = request.GET['data']
        print(datos)
        product = Producto.objects.get(slug__exact=datos)
        object = Cart.objects.get(usuario_id=request.user.id, state=0)
        object.products.remove(product.id)

        text = True
    else:
        text = False
    data = {
        'text' : text
    }
    return JsonResponse(data)
