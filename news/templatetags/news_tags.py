from django import template
from django.db.models import Count, F
from ..models import Categories


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_category():
    return Categories.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
