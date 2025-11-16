from django.urls import path
from product import views

urlpatterns = [
    path('<int:id>/', views.view_specific_products, name='product_detail'),
]
