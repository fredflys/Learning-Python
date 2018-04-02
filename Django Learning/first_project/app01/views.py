from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.
# 业务处理逻辑

# user_list = [
#    {"username": "abc", "password": "123"}
# ]


# HTTPRequest - HTTPResponse
def index(request):
    # return HttpResponse("hello world!") # 返回字符串
    # return render(request, "index.html")  # 渲染（打包）html文件
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # user_info_dict = {"username": username, "password": password}
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
        # user_list.append(user_info_dict)
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html", {"data": user_list})
