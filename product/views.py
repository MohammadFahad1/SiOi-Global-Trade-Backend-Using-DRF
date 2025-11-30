from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer, SimpleProductSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet 
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    # serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProductSerializer
        return SimpleProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 10:
            return Response({"message": "Product with stock more than 10 could not be deleted."})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer