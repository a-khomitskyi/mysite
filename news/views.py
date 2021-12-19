from django.shortcuts import render
from news.models import News, Categories


def index(requests):
    news = News.objects.all().filter(is_published=True)
    categories = Categories.objects.all()
    return render(requests, 'index.html', {'news': news, 'categories': categories})


def category_news(request, category_id):
    news = News.objects.filter(id=category_id, is_published=True)
    categories = Categories.objects.all()
    category = Categories.objects.get(id=category_id)
    return render(request, 'category_news.html', {'news': news, 'categories': categories, 'category': category})
