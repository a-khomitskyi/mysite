from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import News
import re


class NewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = News
        fields = ('title', 'content', 'photo', 'is_published', 'category')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва не повинна починатися з цифри')
        return title


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Логін')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='E-Mail адреса')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повторіть пароль')
    captcha = CaptchaField(label='Підтвердження')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.match(r"[\d]{4,60}", username):
            raise ValidationError('Логін повинен містити лише літери, цифри та нижнє підкреслення!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_.%-+]{,63}@[a-zA-Z0-9]{1}[a-zA-Z0-9.-]{0,}\.[a-z|A-Z]{2,}]{,254}$'
        if not re.match(pattern, email):
            raise ValidationError('Не вірний e-mail!')
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Логін')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    captcha = CaptchaField(label='Підтвердження')


class ContactUsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Ваше ім'я")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Ваша E-Mail адреса')
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Тема листа')
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 7}), label='Контент листа')
    captcha = CaptchaField(label='Підтвердження')

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_.%-+]{,63}@[a-zA-Z0-9]{1}[a-zA-Z0-9.-]{0,}\.[a-z|A-Z]{2,}]{,254}$'
        if not re.match(pattern, email):
            raise ValidationError('Не вірний e-mail!')
        return email
