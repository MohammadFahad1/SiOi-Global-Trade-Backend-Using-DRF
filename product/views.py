from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review, ProductImage
from product.serializers import ProductSerializer, CategorySerializer, SimpleProductSerializer, ReviewSerializer, ProductImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from django.core.exceptions import PermissionDenied
from product.permissions import IsReviewAuthorOrReadOnly
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'updated_at']
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # def get_permissions(self):
    #     # if self.action in ['list', 'retrieve']:
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProductSerializer
        return SimpleProductSerializer

class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs['product_pk'])

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])

    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise PermissionDenied("Authentication required to create a review.")
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        if self.request.user.is_anonymous:
            raise PermissionDenied("Authentication required to update a review.")
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}