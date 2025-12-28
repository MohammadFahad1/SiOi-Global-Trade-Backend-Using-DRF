from django.contrib import admin
from product.models import Product, Category, Review, Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock', 'category', 'brand']
    search_fields = ['name', 'description', 'category__name', 'brand__name']
    list_filter = ['category', 'brand']
    ordering = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)