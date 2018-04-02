from django.db import models

# Create your models here.
# 数据库模型  M


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
