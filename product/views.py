from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
# Create your views here.

@api_view()
def view_products(request):
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def view_specific_products(request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)

@api_view()
def view_categories(request):
    return Response({"message": "List of categories"})

@api_view()
def view_specific_category(request, pk):
     category = get_object_or_404(Category, pk=pk)
     serializer = CategorySerializer(category).data
     return Response(serializer, status=status.HTTP_200_OK)