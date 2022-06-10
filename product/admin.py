from django.contrib import admin
from numpy import product

from product.models import Category, OrderStatus, ProductOrder, Products, UserOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(OrderStatus)
admin.site.register(ProductOrder)
admin.site.register(Products)
admin.site.register(UserOrder)
