from django.urls import path
from product import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='category_list'),
    path('<int:pk>/', views.CategoryDetails.as_view(), name='category_detail'),
]
