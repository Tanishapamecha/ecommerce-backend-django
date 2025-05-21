from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)


# This will allow you to add, edit, and delete products through the admin panel.