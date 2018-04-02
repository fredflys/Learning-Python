from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    pwd = models.CharField(max_length=64)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)


class UserType(models.Model):
    nid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=16)




