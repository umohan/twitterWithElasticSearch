# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-05 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
