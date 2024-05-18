from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/activity/', consumers.UserActivityConsumer.as_asgi()),
]
