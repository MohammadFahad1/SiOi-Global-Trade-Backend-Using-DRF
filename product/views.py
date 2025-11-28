from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer, SimpleProductSerializer
from django.db.models import Count
# Create your views here.

@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SimpleProductSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def view_specific_products(request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)

@api_view()
def view_categories(request):
    categories = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(categories, many=True, context={'request': request}).data
    return Response(serializer, status=status.HTTP_200_OK)

@api_view()
def view_specific_category(request, pk):
    category = Category.objects.annotate(product_count=Count('products')).get(pk=pk)
    serializer = CategorySerializer(category).data
    return Response(serializer, status=status.HTTP_200_OK)