from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryNews.as_view(), name='category'),
    path('published/<int:pk>/', ViewNews.as_view(), name='news_info'),
    path('help-us/', CreateNews.as_view(), name='news_propose'),
    path('find/', get_find_result, name='view_find_result'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact-us/', contact_us, name='contact_us'),
]
