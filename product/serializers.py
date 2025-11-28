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

class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock', 'category_info', 'price_with_tax']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_info = serializers.HyperlinkedRelatedField(queryset=Category.objects.all(), view_name='category_detail', source='category')
    # category = serializers.ModelField(model_field=Category()._meta.get_field('name'))
    category = NestedCategorySerializer()

    def calculate_tax(self, product):
        return round(product.price * Decimal('1.1'), 2)

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'stock', 'price']

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return price
    
    