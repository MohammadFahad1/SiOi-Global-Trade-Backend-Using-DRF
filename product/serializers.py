from rest_framework import serializers
from decimal import Decimal
from product.models import Category, Product, Review, ProductImage, Brand
from django.contrib.auth import get_user_model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']
    
    product_count = serializers.IntegerField(read_only=True, help_text="Returns the number of products in this category.")

class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'images', 'price', 'category', 'brand', 'stock', 'category_info', 'price_with_tax']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax', read_only=True)
    category_info = serializers.HyperlinkedRelatedField(view_name='category-detail', source='category', read_only=True)
    # category = serializers.ModelField(model_field=Category()._meta.get_field('name'))
    category = NestedCategorySerializer()

    def calculate_tax(self, product):
        return round(product.price * Decimal('1.1'), 2)

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "SimpleProductSerializer"
        model = Product
        fields = ['id', 'name', 'description', 'category', 'brand', 'stock', 'price']

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return price

class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_full_name', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_full_name(self, user):
        return user.get_full_name()


class ReviewSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'ratings', 'created_at', 'updated_at']
        read_only_fields = ['user', 'product']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

class BrandSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField()
    class Meta:
        model = Brand
        fields = ['id', 'name', 'description', 'logo']