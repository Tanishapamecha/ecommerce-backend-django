# serializers.py
# This file converts Django model instances into JSON format and back,
# so we can send data over the API and receive it too.

from rest_framework import serializers
from .models import Product, Category

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # specify model to serialize
        fields = '__all__'  # include all model fields


# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # specify model to serialize
        fields = '__all__'  # include all model fields
        read_only_fields = ['user']  # user field should not be changed by API requests
