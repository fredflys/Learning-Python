from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.


def index(request):
    """
    obj = models.UserType(caption='管理员')
    obj.save()

    user_dict = {'caption': '普通用户'}
    models.UserType.objects.create(**user_dict)
    """

    # user_info_dict = {
    #     'user': 'yeff', 'email': 'xxx@126.com',
    #     'pwd': '123456', 'user_type': models.UserType.objects.get(nid=1)
    # }
    # models.UserInfo.objects.create(**user_info_dict)
    # user_info_dict = {
    #     'user': 'john', 'email': 'yyy@qq.com',
    #     'pwd': '123456', 'user_type_id': 1,  # 以外键约束赋值
    # }
    # ret = models.UserInfo.objects.all().values('user', 'user_type__caption')  # 返回可迭代的QuerySet对象
    # # 其中每一个都是UserType对象，封装了当前行内所有数据的对象，其属性可以取出对应列的值
    # # item.nid, item.caption
    # print(ret.query)  # 查看对应的sql语句
    # for i in ret:
    #     print(i.user, i.user_type_id, i.user_type.caption)


    # 取出所有用户类型是管理员的用户,并显示其用户名和用户类型信息
    ret = models.UserInfo.objects.filter(user_type__caption='管理员').values('user', 'user_type__caption')
    print(ret)
    # for item in ret:
    #     print(item.id, item.user_type_id, item.user_type.caption)
    # ret2 = models.UserType.objects.all().values('nid')
    # # ret2仍然是QuerySet
    # # 但内部每一个元素是一个个字典
    # ret3 = models.UserType.objects.all().values_list('nid')
    # # ret3仍然是queryset， 但内部是一个个元组
    #
    # models.UserInfo.objects.create(**user_info_dict1)


    # 反向查询
    # .表名_set.all()
    obj = models.UserInfo.objects.filter(caption='管理员').first()
    print(obj.userinfo_set.all())

    return HttpResponse('OK')
