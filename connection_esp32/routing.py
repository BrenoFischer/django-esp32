from django.urls import path
from .consumers import ConnectionConsumer, ReceiveCommandConsumer, PostConsumer


ws_urlpatterns = [
  path('ws/connection/', ConnectionConsumer.as_asgi()),
  path('ws/receive/', ReceiveCommandConsumer.as_asgi()),
  path('ws/post/', PostConsumer.as_asgi())
]