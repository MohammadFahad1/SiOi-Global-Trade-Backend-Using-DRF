from django.urls import path
from product import views

urlpatterns = [
    path('', views.ViewCategories.as_view(), name='category_list'),
    path('<int:pk>/', views.ViewSpecificCategory.as_view(), name='category_detail'),
]
