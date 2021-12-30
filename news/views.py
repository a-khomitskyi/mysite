from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .forms import NewsForm
from news.models import News, Categories


class HomeNews(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новинний сайт'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryNews(ListView):
    model = News
    template_name = 'category_news.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


class CreateNews(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    form_class = NewsForm
    template_name = 'news_propose.html'


def get_find_result(request):
    to_find = request.GET.get('q')
    if to_find:
        queryset = News.objects.filter(content__icontains=to_find).select_related(
            'category') or News.objects.filter(title__icontains=to_find).select_related('category')

        paginator = Paginator(queryset, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'view_result.html', {'page_obj': page_obj, 'q': to_find, 'count': len(queryset)})
    else:
        return render(request, 'view_result.html')
