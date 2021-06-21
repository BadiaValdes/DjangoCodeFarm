############### MODELS IMPORT ###################
from cart.models import Cart, ListaDeseos, Order


from tienda.models import Producto

############### ENDS MODEL IMPORT ###############

############### OTROS IMORT ###############
from django.http import JsonResponse, HttpResponse

from django.contrib.auth.decorators import login_required
############### END OTROS IMORT ###########


# Añadir elemento al carrito
@login_required
def addToCart(request):
    if request.method == 'GET':
        # Obtener el producto pasado por GET
        product = request.GET['product']

        # Obtener todas las propiedades del producto
        product_selected = Producto.objects.get(id__exact=product)

        # Preguntar si está en stock
        if(product_selected.amount_stock > 0):

            # Disminuir en 1 la cantidad de productos
            product_selected.amount_stock = product_selected.amount_stock - 1

            # Preguntar si llegó a 0
            if(product_selected.amount_stock == 0):
                product_selected.available = False

            # Salvar los cambios
            product_selected.save()

            # crear el carrito
            object = Cart.objects.get_or_create(usuario_id=request.user.id, state=0)

            # obtener el carrito
            object = Cart.objects.get(id__exact=object[0])

            # Asignar usuario
            object.usuario = request.user

            # Salvar carrito
            object.save()

            # adicionar productos, el through_defaults, es para agregar otros campos que se encuentren dentro de la tabla de muchos a muchos
            object.products.add(product, through_defaults={'cantidad': 5})

            print(object)

            data = {
                'product': product,
                'ad': True,
                'outOfStock': False,
            }
            return JsonResponse(data)
        else:
            data = {
                'outOfStock': True,
            }
            return JsonResponse(data)

    else:
        return HttpResponse("Bad!")


# Pagar lo que está en el carrito
@login_required
def payOut(request):
    if request.method == 'POST':

        # Buscar el carrito actual del usuario
        object = Cart.objects.get(usuario_id=request.user.id, state=0)

        # Crear una orden para la venta
        order_ticket = Order.objects.create()

        # Poner en carrito como estado de pagado
        object.state = 1
        object.order = order_ticket

        # Salvar el carrito y enviar vendido
        object.save()

        data = {
            'sold': True,
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")

# Obtener todos los productos de un carrito
@login_required
def getProductos(request):
    if request.method == 'GET':

        # Obtener el carrito actual del usuario
        try:
            object = Cart.objects.get(usuario_id=request.user.id, state=0)

            product_name=[]

            # recorrer todos los productos pertenecientes a un carrito
            for obj in object.products.all():
                product_name.append([obj.nombre, obj.precioDescuento(), obj.photo.url, obj.slug])

            # json a devolver, guarda todos los productos en forma de lista
            data = {
                'products' :  product_name,
                'empty': False
            }

        except:
            data = {
                'empty': True

            }
        return JsonResponse(data)
    else:
        return HttpResponse("Bad!")

@login_required
def CartDeleteItem(request):
    if (request.GET['data']):
        datos = request.GET['data']
        print(datos)

        # Buscar el producto y aumentar en uno su cantidad
        product = Producto.objects.get(slug__exact=datos)
        product.amount_stock = product.amount_stock  + 1

        # En caso de que el producto se no este disponible, hacerlo disponible
        if not product.available :
            product.available = True

        product.save()

        # Obtener el producto según el id del usuario
        object = Cart.objects.get(usuario_id=request.user.id, state=0)

        # Eliminar el producto de la tabla de muchos a muchos
        object.products.remove(product.id)

        text = True
    else:
        text = False
    data = {
        'text' : text
    }
    return JsonResponse(data)
