from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from .views import OrderViewSet, CartViewSet

urlpatterns = [
    #crear un carrito
    path('users/<int:u_id>/', CartViewSet.as_view({'post': 'create'}), name='nuevo_pedido'),
    #añadir ordenes 
    path('users/<int:u_id>/<str:product>/<int:quantity>/', OrderViewSet.as_view({'post': 'add_order'}), name='actualizar_carrito'),
    #check out - 
    path('users/<int:u_id>/checkout/', CartViewSet.as_view({'delete': 'checkout'}), name='realizar_pedido')
]