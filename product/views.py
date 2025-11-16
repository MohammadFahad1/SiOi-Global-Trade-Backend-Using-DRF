from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer
# Create your views here.
@api_view()
def view_specific_products(request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product).data
        return Response(serializer, status=status.HTTP_200_OK)

@api_view()
def view_categories(request):
    return Response({"message": "List of categories"})