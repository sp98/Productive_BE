# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0011_auto_20170610_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_tasks',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
