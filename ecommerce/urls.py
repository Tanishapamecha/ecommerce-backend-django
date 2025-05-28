"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

# Simple home view for base URL
def home(request):
    return HttpResponse("Welcome to the Ecommerce backend!")

urlpatterns = [
    path('admin/', admin.site.urls),              
    path('api/', include('store.urls')),         
    path('api-token-auth/', obtain_auth_token),   
    path('', home),                               
]
