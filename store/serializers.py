# This serializer converts Product model instances to JSON format and vice versa, facilitating API interactions.
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']

