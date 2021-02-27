# import os
#
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application
# from dashboard import consumer
# from django.urls import path
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
#
# websocket_urlPattern = [
#     path('ws/test/', consumer.DashConsumer.as_asgi()),
# ]
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter(websocket_urlPattern)
#     )
#     # Just HTTP for now. (We can add other protocols later.)
# })
