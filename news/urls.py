from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', category_news, name='category'),
    path('published/<int:news_id>/', show_full_news, name='news_info'),
    path('help-us/', news_propose, name='news_propose'),
]
