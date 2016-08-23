# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsfeed', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('is_published', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Post Feeds',
            },
        ),
    ]