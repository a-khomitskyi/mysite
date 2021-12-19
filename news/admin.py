from django.contrib import admin
from .models import News, Categories


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title', )
    list_display_links = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Categories, CategoryAdmin)
