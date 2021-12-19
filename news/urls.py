from django.urls import path
from .views import index, category_news


urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', category_news),
]
