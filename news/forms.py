from django import forms
from .models import Categories


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    content = forms.CharField(label='Контекст новини', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))
    photo = forms.ImageField(required=False, label='Фото', widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    is_published = forms.BooleanField(label='Опублікувати', initial=True, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    category = forms.ModelChoiceField(Categories.objects.all(), label='Категорія', empty_label='Оберіть категорію',
                widget=forms.Select(attrs={
                    'class': 'form-select'
                }))

