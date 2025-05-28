from django.db import models
from django.contrib.auth.models import User

# Category model to group products
class Category(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name


# Product model to store product details
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=255)  
    description = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.PositiveIntegerField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name


# Cart model to hold products user wants to buy
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one cart per user
    products = models.ManyToManyField(Product, blank=True)  # products in cart
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username}'s Cart"
