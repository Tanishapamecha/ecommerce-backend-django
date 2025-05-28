# from django.contrib import admin
# from .models import Product, Category

# # Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

# # This will allow you to add, edit, and delete products through the admin panel.



from django.contrib import admin
from .models import Product, Category

# Register the Product model to appear in admin site
admin.site.register(Product)

# Register the Category model to appear in admin site
admin.site.register(Category)

# Now you can add, edit, and delete products and categories in Django admin
