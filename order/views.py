from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer, OrderSerializer
from order.models import Cart, CartItem, Order, OrderItem
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Cart.objects.all()
        return Cart.objects.filter(user=self.request.user)

class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AddCartItemSerializer
        elif self.action == 'partial_update':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
