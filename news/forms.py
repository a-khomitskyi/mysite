from django import forms
from .models import News
from django.core.exceptions import ValidationError
import re


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     content = forms.CharField(label='Контекст новини', widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5
#     }))
#     photo = forms.ImageField(required=False, label='Фото', widget=forms.FileInput(attrs={
#         'class': 'form-control'
#     }))
#     is_published = forms.BooleanField(label='Опублікувати', initial=True, widget=forms.CheckboxInput(attrs={
#         'class': 'form-check-input'
#     }))
#     category = forms.ModelChoiceField(Categories.objects.all(), label='Категорія', empty_label='Оберіть категорію',
#                 widget=forms.Select(attrs={
#                     'class': 'form-select'
#                 }))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'photo', 'is_published', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва не повинна починатися з цифри')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        pattern = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_.%-+]{,63}@[a-zA-Z0-9]{1}[a-zA-Z0-9.-]{0,}\.[a-z|A-Z]{2,}]{,254}$'
        if re.match(pattern, content):
            raise ValidationError('Не повинно містити e-mail!')
        return content
