# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestScrapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
            ],
            options={
                'db_table': 'test_scrapy1',
            },
        ),
    ]
