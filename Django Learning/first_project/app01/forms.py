from django import forms
from app01 import models


def mobile_validate(value):
    import re
    mobile_re = re.compile("^(13[0-9]|14[579]|15[0-3,5-9]|1 6[6]|17[0135678]|18[0-9]|19[89])\\d{8}$")
    if not mobile_re.match(value):
        print('123123')
        raise forms.ValidationError('手机号码格式不对哦')


class MyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['book_type'] = forms.CharField(
            widget=forms.Select(choices=models.BookType.objects.values_list('id', 'caption'))
        )

    user = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput)
    pwd = forms.CharField(error_messages={'required': '为什么不输入密码？？'})
    email = forms.EmailField(error_messages={'required': '邮箱还没输入哦', 'invalid': '邮箱格式错误'})
    # book_type_choices = (
    #     (0, '小说'),  value
    #     (1, '科普'),  innerText
    # )  # 元组内有元组
    # 从数据库获得数据

    # 注意这里filed都是静态字段
    # 类的静态字段只创建一次以后不会再修改，新的对象都会使用同一份数据
    # 所以MyForm这里的静态字段只会执行一次
    # 加入数据库中的数据更新了，服务器不重启的话，这里从数据库取来的值是不会变的
    # 因此将该字段写入类的初始化方法里，不要忘了执行父类的初始化方法哦
    # book_type_choices = models.BookType.objects.values_list('id', 'caption')
    # book_type = forms.CharField(
    #     widget=forms.Select(choices=book_type_choices)
    # )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'border:1px solid red;'})
    )  # 可以为生成的标签添加属性

    mobile = forms.CharField(
        validators=[mobile_validate, ],
        error_messages={'required': '手机号不填不行'},
        widget=forms.TextInput
    )

