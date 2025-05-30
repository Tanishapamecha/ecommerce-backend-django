from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, Cart
from .serializers import ProductSerializer, CategorySerializer


# ViewSet to handle all CRUD operations for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ViewSet to handle CRUD for Products, with search, filter, and ordering
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Add this line
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    filterset_fields = ['category']

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# API View to delete the current user's cart
class DeleteCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            carts = Cart.objects.filter(user=request.user)
            if not carts.exists():
                return Response({"error": "Cart does not exist."}, status=status.HTTP_404_NOT_FOUND)
            carts.delete()
            return Response({"message": "Cart(s) deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
