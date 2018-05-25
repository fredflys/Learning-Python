from django.contrib import admin
from app01 import models

# Register your models here.
# 在models中创建的表注册到这里就可以在admin后台管理这些表
# 不注册也可以使用，只是无法在admin页面管理
admin.site.register(models.UserInfo)
admin.site.register(models.Book)
admin.site.register(models.BookType)
