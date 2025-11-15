from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view()
def view_products(request):
    return Response({"message": "List of products"})

@api_view()
def view_categories(request):
    return Response({"message": "List of categories"})