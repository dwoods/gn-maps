from django import template

register = template.Library()

@register.filter
def modeltype(obj):
    classname = obj.__class__.__name__
    return classname
