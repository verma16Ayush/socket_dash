from django.urls import path
from .consumers import *
from socket_dash import consumers

websocket_urlpatterns = [
    path('ws/', consumers.Dashboard.as_asgi()),
]