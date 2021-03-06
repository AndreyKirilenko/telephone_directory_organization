# Generated by Django 3.2.9 on 2021-12-03 15:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100)),
                ('work_phone', models.CharField(blank=True, max_length=12)),
                ('personal_phone', models.CharField(blank=True, max_length=12, unique=True)),
                ('fax_number', models.CharField(blank=True, max_length=12)),
                ('staffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['staffer'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('adress', models.CharField(max_length=100, verbose_name='Адрес')),
                ('description', models.TextField(max_length=200, verbose_name='Описание компании')),
                ('created', models.DateField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thecompany', to=settings.AUTH_USER_MODEL)),
                ('staffer', models.ManyToManyField(related_name='staffers', to='catalog.Staffer', verbose_name='Сотрудники')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['name'],
            },
        ),
    ]
