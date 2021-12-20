from django.shortcuts import render
from news.models import News, Categories


def index(requests):
    news = News.objects.all().filter(is_published=True)
    return render(requests, 'index.html', {'news': news})


def category_news(request, category_id):
    news = News.objects.filter(id=category_id, is_published=True)
    category = Categories.objects.get(id=category_id)
    return render(request, 'category_news.html', {'news': news, 'category': category})


def show_full_news(requests, news_id):
    news = News.objects.all().get(id=news_id)
    return render(requests, 'news_detail.html', {'news': news})
