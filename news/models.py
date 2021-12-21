from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва статті')
    content = models.TextField(blank=True, verbose_name='Контент статті')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    photo = models.ImageField(verbose_name='Фото', upload_to='media/%Y/%m/%d/', max_length=150, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_info', kwargs={'news_id': self.pk})


class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ('id', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
