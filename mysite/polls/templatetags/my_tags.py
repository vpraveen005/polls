from django import template

register = template.Library()

@register.filter
def to_number(value):
    return f"{value:,}"

@register.filter
def to_title(value):
    return value.title()

@register.filter
def mask(value):
    result = 'X' *(len(value)- 4) + value[-4:]
    return result