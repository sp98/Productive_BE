# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20170604_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
