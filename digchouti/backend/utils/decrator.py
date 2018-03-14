#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import functools
import config
from backend.utils.response import BaseResponse


# 装饰器实现页面的用户登录状态验证

# 普通请求
# 若用户没有登陆，则返回到登陆页面
def auth_login_redirect(func):

    def inner(self, *args, **kwargs):
        if not self.session['is_login']:
            self.redirect(config.LOGIN_URL)
            return
        func(self, *args, **kwargs)
    return inner


# 解决ajax请求的验证问题
# ajax请求的后台是无法进行跳转的，即使写redirect方法也没用
# 前端收到后台返回的json后，自行判断，进行跳转
def auth_login_json(func):

    def inner(self, *args, **kwargs):
        if not self.session['is_login']:
            rep = BaseResponse()
            rep.summary = "auth failed"
            self.write(json.dumps(rep.__dict__))
            return
        func(self, *args, **kwargs)
    return inner
