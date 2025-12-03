from django.contrib import admin
from order.models import Cart, CartItem, Order, OrderItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']

# Register your models here.
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

# Register your models here.