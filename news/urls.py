from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', category_news, name='category'),
    path('published/<int:news_id>/', show_full_news, name='news_info'),
]
