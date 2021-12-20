from django import template
from ..models import Categories


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_category():
    return Categories.objects.all()


@register.inclusion_tag('inc/_navbar.html')
def show_categories():
    categories = Categories.objects.all()
    return {'categories': categories}
