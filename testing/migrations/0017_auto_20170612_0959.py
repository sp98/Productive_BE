# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0016_auto_20170612_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_tasks',
            name='taskStatus',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]