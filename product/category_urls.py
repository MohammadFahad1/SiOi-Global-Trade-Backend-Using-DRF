from django.urls import path
from product import views

urlpatterns = [
    path('', views.view_categories, name='category_list'),
    path('<int:pk>/', views.view_specific_category, name='category_detail'),
]
