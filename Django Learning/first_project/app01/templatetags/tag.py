from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node, TemplateSyntaxError,

register = template.Library()

@register.simple_tag
def my_simple_tag(v):
    return v