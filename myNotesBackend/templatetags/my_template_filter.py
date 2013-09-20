__author__ = 'Abdellah'
from django import template

register = template.Library()
@register.filter(name='split')
def split(string, arg):
    return string.split(arg)