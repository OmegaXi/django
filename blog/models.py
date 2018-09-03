from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    objects = None
    title = models.CharField(max_length=32, default='')
    content = models.TextField(null=True)

    def __str__(self):  # 增加该方法
        return self.title
