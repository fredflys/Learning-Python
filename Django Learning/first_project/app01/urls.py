from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'', views.index),
]