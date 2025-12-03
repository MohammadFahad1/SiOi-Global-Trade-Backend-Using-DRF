from rest_framework import serializers
from order.models import Cart, CartItem
from product.models import Product
from decimal import Decimal

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price']
class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'subtotal']
        

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
    
    def get_total_price(self, cart: Cart):
        return sum([item.product.price * item.quantity for item in cart.items.all()])