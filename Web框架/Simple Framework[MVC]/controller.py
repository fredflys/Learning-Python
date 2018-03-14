# -*- coding:utf-8 -*-
import os
from jinja2 import Template


def new():
    f = open(os.path.join('views', 'new.html'), 'r')
    data = f.read()
    f.close()
    return data


def index():
    f = open(os.path.join('views', 'original.html'), 'r')
    result = f.read()
    template = Template(result)
    data = template.render(name='Yeff Xu', user_list=['John', 'Mike'])
    return data.encode('utf-8')
