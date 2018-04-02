from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


# 博客文章
# 标题，标签，发布日期，更新时间
class Article(models.Model):
    title = models.CharField("博客标题", max_length=100)
    category = models.CharField("博客标签", max_length=50, blank=True)
    pub_date = models.DateField("发布日期", auto_now_add=True, editable=True)
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)
    content = UEditorField("文章正文")

    def __unicode__(self):
        return self.title

    # 内部类，定义元数据（模型类的一些行为特性）
    class Meta:
        ordering = ['-pub_date']  # 按时间降序排列
        verbose_name = '文章'
        verbose_name_plural = '文章'
