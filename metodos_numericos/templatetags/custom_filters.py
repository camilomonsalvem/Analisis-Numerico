from django import template

register = template.Library()

@register.filter
def zip_lists(a, b):
    """Combina dos listas en pares"""
    return zip(a, b)