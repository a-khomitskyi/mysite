from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Categories
from django.views.generic import ListView
from .forms import NewsForm


class HomeNews(ListView):

    model = News
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)
# def index(requests):
#     news = News.objects.all().filter(is_published=True)
#     return render(requests, 'index.html', {'news': news})


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
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(requests, 'news_propose.html', context={'form': form})
