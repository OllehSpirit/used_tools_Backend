# Generated by Django 4.2.5 on 2023-09-16 09:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.CharField(blank=True, default='', max_length=20)),
                ('price', models.FloatField(blank=True)),
                ('photos', models.ImageField(blank=True, null=True, upload_to='photos/posts/%Y/%m/%d/')),
                ('rate', models.FloatField(blank=True)),
                ('Owner', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, default='', max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='Rated_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, default=0)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rated_Product',
                'verbose_name_plural': 'Rated_Products',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='Rated',
            field=models.ManyToManyField(related_name='rated', through='App.Rated_Products', to=settings.AUTH_USER_MODEL),
        ),
    ]