from django.db import models

# Create your models here.
# 数据库模型  M


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class BookType(models.Model):
    caption = models.CharField(max_length=32)


class Book(models.Model):
    name = models.CharField(max_length=32)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pubdate = models.DateField()
    # 外键
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)

    def __str__(self):
        return "Book Object: %s %sp %s元" % (self.name, self.pages, self.price)