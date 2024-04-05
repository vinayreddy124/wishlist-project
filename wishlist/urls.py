"""
URL configuration for wishlist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wishlistapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registration, name='registration'),
    path('homepage/', views.homepage, name='homepage'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('dealerdashboard/', views.dealerdashboard, name='dealerdashboard'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),path('create_product/', views.create_product, name='create_product'),
    path('productlist/', views.productlist, name='productlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
]