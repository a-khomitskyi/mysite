# Generated by Django 4.0.2 on 2022-02-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва статті')),
                ('content', models.TextField(blank=True, verbose_name='Контент статті')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('photo', models.ImageField(blank=True, max_length=150, upload_to='media/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубліковано')),
                ('views_count', models.IntegerField(default=0, verbose_name='Кількість переглядів')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categories', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
                'ordering': ('created_at',),
            },
        ),
    ]
