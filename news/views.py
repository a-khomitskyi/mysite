from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactUsForm
from news.models import News, Categories
from .utils import parse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ви успішно зареєстровані!')
            return redirect('home')
        else:
            messages.error(request, 'Виникла помилка! Перевірте введені дані!')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, 'Ви успішно ввійшли до системи!')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Вихід здійснено успішно!')
    return redirect('home')


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            result = send_mail(f'[{form.cleaned_data["name"]}] ' + form.cleaned_data['subject'], form.cleaned_data['content'], 'andrii.khomitskyi-ipm201@nung.edu.ua', [form.cleaned_data['email']])
            if result:
                messages.success(request, 'Лист надіслано!')
                return redirect('home')
            else:
                messages.error(request, 'Виникла помилка')
                return redirect('home')
        else:
            messages.error(request, 'Не вірно введені дані')
    else:
        form = ContactUsForm()
    return render(request, 'news/contact_us.html', {'form': form})


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новинний сайт'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryNews(ListView):
    model = News
    template_name = 'news/category_news.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter = News.objects.filter(pk=self.kwargs['pk']).update(views_count=F('views_count') + 1)
        return context


class CreateNews(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    form_class = NewsForm
    template_name = 'news/news_propose.html'


def get_find_result(request):
    to_find = request.GET.get('q')
    if to_find:
        queryset = News.objects.filter(content__icontains=to_find).select_related(
            'category') or News.objects.filter(title__icontains=to_find).select_related('category')

        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'news/view_result.html', {'page_obj': page_obj, 'q': to_find, 'count': len(queryset)})
    else:
        return render(request, 'news/view_result.html')
