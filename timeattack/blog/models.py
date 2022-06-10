from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=20, null=False)
    des = models.CharField(max_length=200, null=False)


class Article(models.Model):
    class Meta:
        db_table = "article"

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=200)
