from django.contrib import admin
from wishlistapp.models import CustomUser, Product



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_user', 'is_dealer']



admin.site.register(CustomUser, CustomUserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'quantity', 'price']

admin.site.register(Product, ProductAdmin)
