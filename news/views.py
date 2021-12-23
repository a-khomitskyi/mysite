from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Categories
from .forms import NewsForm


def index(requests):
    news = News.objects.all().filter(is_published=True)
    return render(requests, 'index.html', {'news': news})


def category_news(request, category_id):
    news = News.objects.filter(category_id=category_id, is_published=True)
    category = Categories.objects.get(id=category_id)
    return render(request, 'category_news.html', {'news': news, 'category': category})


def show_full_news(requests, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(requests, 'news_detail.html', {'news': news})


def news_propose(requests):
    if requests.method == 'POST':
        form = NewsForm(requests.POST, requests.FILES)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            news.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(requests, 'news_propose.html', context={'form': form})
