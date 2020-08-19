from django import template


register = template.Library()


@register.filter(name='multiply')
def multipy(a, b):
    return a * b
