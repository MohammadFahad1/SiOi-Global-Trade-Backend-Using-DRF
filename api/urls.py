from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from order.views import CartViewSet, CartItemViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    # other paths can go here
]

