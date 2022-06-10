from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # DB 테이블의 이름을 지정
    class Meta:
        db_table = "user"

    bio = models.CharField(max_length=256, null=True, blank=True)
