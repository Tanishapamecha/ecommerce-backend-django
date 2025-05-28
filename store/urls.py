from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, DeleteCartView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)  # /api/products/
router.register(r'categories', CategoryViewSet)  # /api/categories/

urlpatterns = [
    path('', include(router.urls)),  
    path('cart/delete/', DeleteCartView.as_view(), name='delete-cart'),  
]
