from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Categories


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'views_count', 'get_photo')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    fields = ('title', 'category', 'content', 'get_photo', 'photo', 'views_count', 'created_at', 'updated_at', 'is_published')
    readonly_fields = ('get_photo', 'views_count', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" style="width: 75px">')
        else:
            return '-'

    get_photo.short_description = 'Мініатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title', )
    list_display_links = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Categories, CategoryAdmin)
