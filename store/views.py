from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category, Cart
from .serializers import ProductSerializer, CategorySerializer, CartSerializer


# ViewSet to handle all CRUD operations for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#  “Create an API for me to do all operations (add, view, update, delete) on Products.”
# ViewSet to handle CRUD for Products, with search, filter, and ordering
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Add this line
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View cart items
class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart, created = Cart.objects.get_or_create(user=request.user)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

#  Add product to cart
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            product_id = request.data.get("product_id")
            if not product_id:
                return Response({"error": "Product ID is required"}, status=400)

            product = Product.objects.get(id=product_id)
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.products.add(product)
            return Response({"message": "Product added to cart"}, status=201)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

# Update cart
class UpdateCartView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        try:
            product_ids = request.data.get("product_ids", [])
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.products.set(product_ids)  # Replace current products with new ones
            return Response({"message": "Cart updated successfully"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


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