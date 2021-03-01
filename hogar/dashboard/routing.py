# chat/routing.py
from django.urls import re_path, path

from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/test/$', consumer.DashConsumer.as_asgi()),
]
