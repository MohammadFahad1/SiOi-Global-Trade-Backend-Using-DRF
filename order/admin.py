from django.contrib import admin
from order.models import Cart, CartItem, Order, OrderItem, WishList, WishListItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'total_price', 'created_at', 'updated_at']

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']

@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    list_display = ['wishlist', 'product', 'created_at', 'updated_at']

# Register your models here.
admin.site.register(CartItem)
admin.site.register(OrderItem)

# Register your models here.