# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 03:41
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='users',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='daily_tasks',
            old_name='task_description',
            new_name='taskDescription',
        ),
        migrations.RemoveField(
            model_name='daily_tasks',
            name='task_name',
        ),
        migrations.RemoveField(
            model_name='daily_tasks',
            name='task_status',
        ),
        migrations.RemoveField(
            model_name='users',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.AddField(
            model_name='daily_tasks',
            name='taskCadence',
            field=models.CharField(default='Daily', max_length=20),
        ),
        migrations.AddField(
            model_name='daily_tasks',
            name='taskDate',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='daily_tasks',
            name='taskName',
            field=models.CharField(default='', max_length=230),
        ),
        migrations.AddField(
            model_name='daily_tasks',
            name='taskStatus',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='daily_tasks',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]