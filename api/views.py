
from rest_framework import viewsets , generics
from .models import ClientUser, Cart, Product ,Order
from .serializers import ProductSerializer, OrderSerializer, CartSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.http import HttpResponse
"""
import pandas as pd
import flask as fs
"""
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny] # aqui iria authentificacion de usuario


    def update_excel(self,title , quantity, cost):
        pass
    def update_cart(self,user, quantity, cost):
        clientcart = Cart.objects.get(user=user)
        clientcart.count += quantity
        clientcart.total += cost
        clientcart.save()

    @action(detail=False)
    def add_order(self,request,u_id=None,product=None,quantity=None): #Asumimos que es un POST 
        selected_product = self.queryset.objects.filter(title=product)
        order_cost = selected_product.price * quantity
        self.update_excel(selected_product.title ,quantity,order_cost)
        self.update_cart(u_id, quantity, order_cost)
        return(HttpResponse(status=201)) #devolvemos un codigo objeto creado

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny] # aqui iria authentificacion de usuario
        #def create_excel(''): #añadir como se hace
    """
        def create_excel('update_excel'): #añadir como se hace
        df = pd.DataFrame (Cart.objects.all(self,title , quantity, cost), columns = ['selected_product', 'u_id, quantity'])
    """
        pass
    def create(self, request,u_id=None):
        newcart= Cart(user=u_id,count=0, total=0)
        newcart.save()
        self.create_excel(u_id)
        
        return(HttpResponse(status=201)) #añadir else resolver error 
    
    def checkout(self, request,u_id=None):
        clientcart = self.queryset.objects.filter(user=u_id)
        #mandar mail
        
        #destruir carrito
        clientcart.delete()
        return(HttpResponse(status=204)) #añadir else para resolver error

        #crear excel 
        # df.to_excel (r'Path para almacenar el archivo excel exportado \ Nombre de archivo.xlsx ', índice = Falso)
    #https://datatofish.com/export-dataframe-to-excel/

