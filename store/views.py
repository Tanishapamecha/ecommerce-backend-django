from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
# This viewset provides CRUD operations for the Product model via the API.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    