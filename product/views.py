from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer, SimpleProductSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SimpleProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ProductList(ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.select_related('category').all()
    
    def get_serializer_class(self):
        return ProductSerializer if self.request.method == 'GET' else SimpleProductSerializer
    
    # def get_serializer_context(self):
    #     return {'request': self.request}


class ViewSpecificProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = SimpleProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        copy_of_product = ProductSerializer(product, context={'request': request}).data
        product.delete()
        return Response(copy_of_product, status=status.HTTP_204_NO_CONTENT)

class ViewCategories(APIView):
    def get(self, request):
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories, many=True, context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificCategory(APIView):
    def get(self, request, pk):
        # category = Category.objects.annotate(product_count=Count('products')).get(pk=pk)
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=pk)
        serializer = CategorySerializer(category).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        copy_of_category = CategorySerializer(category).data
        category.delete()
        return Response(copy_of_category, status=status.HTTP_204_NO_CONTENT)