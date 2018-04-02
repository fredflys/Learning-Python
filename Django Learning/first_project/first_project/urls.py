"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import app01.views
# 路由系统
# 不会把所有路由都写在一个文件里，需要进行路由分发
# 高内聚（一个函数只做一件事），低藕荷（组块之间关联性不强）
# 一个积木块只有一个功能，且可以通过多种方式与其它块拼接
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index/', include('app01.urls')),
]

