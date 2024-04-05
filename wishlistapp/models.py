from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_user = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.URLField()
    parent = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True)

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)