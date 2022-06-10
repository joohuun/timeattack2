from django.db import models
from django.forms import IntegerField

# Create your models here.

STATE_CHOICE = (
    ('주문완료', '주문완료'),
    ('결제완료', '결제완료'),
    ('배송준비중', '배송준비중'),
    ('배송중', '배송중'),
    ('배송완료', '배송완료'),
)


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    img = models.ImageField()
    desc = models.TextField(blank=True)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()

    class Meta:
        db_table = "product"


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"


# 유저의 주문 상태, 유저는 여러 상품의 주문 상태를 가짐
class OrderStatus(models.Model):
    state = models.CharField(max_length=50, choices=STATE_CHOICE)

    class Meta:
        db_table = 'orderstatus'


# 유저가 주문한 상품의 갯수 저장
class ProductOrder(models.Model):
    order_count = models.IntegerField()

    class Meta:
        db_table = 'productorder'


# 유저의 주문정보를 저장, 한 유저는 여러개의 주문정보를 가질수 있고, 주문정보는 여러개의 제품을 가질수 있음
class UserOrder(models.Model):
    name = models.ManyToManyField(Products, related_name='product_name')
    status = models.ForeignKey(OrderStatus)

    address = models.CharField(max_length=256)
    ordered_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DateField(max_length=50)
    discount = models.FloatField()
    boolean = models.BooleanField(null=True)

    class Meta:
        db_table = 'userorder'
