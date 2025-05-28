# serializers.py
# This file converts Django model instances into JSON format and back,
# so we can send data over the API and receive it too.

from rest_framework import serializers
from .models import Product, Category

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  
        fields = '__all__'  


# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  
        fields = '__all__'  
        read_only_fields = ['user']  
