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
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class ProductViewSet(ModelViewSet):
    """ 
    API endpoint for managing products in the e-commerce store.
    - Allows authenticated admin users to create, update, and delete products.
    - Allows all users to view products, product details and filter products. 
    - Supports searching by name, description and category
    - Supports ordering by price and updated_at.
    """
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

    @swagger_auto_schema(
            operation_summary="List all products with pagination, filtering, searching, and ordering (All Users)",
            operation_description="Retrieve a paginated list of products. Supports filtering by category, price range, and availability. Supports searching by name and description. Supports ordering by price and last updated date.",
    )
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of products with pagination, filtering, searching, and ordering.
        """
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary="Create a new product (Admin only)",
            operation_description="Only admin users can create new products.",
            request_body=SimpleProductSerializer,
            responses={201: SimpleProductSerializer, 400: 'Bad Request'},
    )
    def create(self, request, *args, **kwargs):
        # """
        # Only admin users can create new products.
        # """
        return super().create(request, *args, **kwargs)

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