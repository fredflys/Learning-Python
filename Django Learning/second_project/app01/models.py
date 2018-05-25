from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    pwd = models.CharField(max_length=64)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)


class UserType(models.Model):
    nid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=16, unique=True)


# 多对多   多个部门用多台机器
class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)


class Group(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    h2g = models.ManyToManyField('Host', through='HostToGroup')


class HostToGroup(models.Model):
    hgid = models.AutoField(primary_key=True)
    host_id = models.ForeignKey('Host')
    group_id = models.ForeignKey('Group')




