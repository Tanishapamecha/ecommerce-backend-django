from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

# This will allow you to add, edit, and delete products through the admin panel.