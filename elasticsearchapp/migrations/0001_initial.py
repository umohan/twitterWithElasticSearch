# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-05 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('id', models.TextField(max_length=10000, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.CharField(max_length=20000)),
                ('userId', models.TextField(max_length=1000)),
            ],
        ),
    ]
