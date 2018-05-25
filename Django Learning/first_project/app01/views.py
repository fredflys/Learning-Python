from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.
# 业务处理逻辑
import json
from decimal import Decimal
from datetime import date


class DecimalDatetimeEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, o)


def index(request):
    # 定义要给前端传递的字典
    post_ret_dict = {'status': True, 'content': None}
    if request.method == 'POST':
        try:
            # 获取前端抛来的字符串
            post_data_str = request.POST.get('post_data', None)
            # 反序列化
            post_data_dict = json.loads(post_data_str)
            # post_data_dict: {'name': ['nameA', 'nameB'],'price':[20,30,40] }
            from django.db.models import Q
            # 构造Q搜索
            condition = Q()
            for k, v in post_data_dict.items():
                # 同一搜索框内（同一条件）的输入是OR关系（主关系）
                q = Q()
                q.connector = 'OR'
                for item in v:
                    # 这里的k就是前端传来的name属性的值，也就是搜索条件（子关系）
                    q.children.append((k, item))
                condition.add(q, 'AND')
            # 将Q搜索直接作为filter的条件传入，并再用values方法取到想要的值
            # 这里用book_type__caption双下划线的形式找到外键表的caption域的值
            # 返回值仍是Queryset对象，可通过list转换为列表
            list_ret = list(models.Book.objects.filter(condition).values('name', 'pages', 'price', 'pubdate', 'book_type__caption'))  # QuerySet
            post_ret_dict['content'] = list_ret
        except Exception as e:
            post_ret_dict['status'] = False
        # 最后再序列化要给前端的内容
        # 注意价格是Decimal类型，印刷日期是Datetime类型，这两类都不是python内置类型，无法直接用json.dumps方法序列化
        # 这里可以借助第二个参数，构造一个自定义的解析类，自行处理
        post_ret_str = json.dumps(post_ret_dict, cls=DecimalDatetimeEncoder)
        return HttpResponse(post_ret_str)

        # django提供的序列化方法，但是无法获得外键表的对应值，不能在使用values方法后序列化
        # from django.core.serializers import serialize
        # ret = models.Book.objects.filter(condition)  # QuerySet
        # str_ret = serialize('json', ret)
        # print(str_ret)
        # return HttpResponse(str_ret)

    if request.method == 'POST':
        pass
    return render(request, "index.html")


def form(request):
    from app01.forms import MyForm
    empty_form = MyForm()
    if request.method == 'POST':
        f = MyForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            # 这里只是为了使得正确提交后不至于
            return render(request, "form.html", {'myform': empty_form})
        return render(request, "form.html", {"errors": f.errors, "myform": f} )
    else:
        return render(request, "form.html", {'myform': empty_form})
