from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, DeleteCartView ,CartDetailView, AddToCartView, UpdateCartView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)  # /api/products/
router.register(r'categories', CategoryViewSet)  # /api/categories/

urlpatterns = [
    path('', include(router.urls)),  


    # Cart URLs
    path('cart/', CartDetailView.as_view(), name='cart-detail'),         # GET
    path('cart/add/', AddToCartView.as_view(), name='cart-add'),         # POST
    path('cart/update/', UpdateCartView.as_view(), name='cart-update'),  # PUT
    path('cart/delete/', DeleteCartView.as_view(), name='delete-cart'),  
]
