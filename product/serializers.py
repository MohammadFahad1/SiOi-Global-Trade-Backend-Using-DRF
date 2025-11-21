from rest_framework import serializers
from decimal import Decimal
from product.models import Category, Product

""" class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField() """

""" class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category = serializers.StringRelatedField()
    # category = CategorySerializer()
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name='category_detail',
    )

    def calculate_tax(self, product):
        return round(product.price * Decimal('1.1'), 2) """

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']
    
    product_count = serializers.IntegerField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_info', 'price_with_tax']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_info = serializers.HyperlinkedRelatedField(queryset=Category.objects.all(), view_name='category_detail', source='category')
    category = CategorySerializer()

    def calculate_tax(self, product):
        return round(product.price * Decimal('1.1'), 2)