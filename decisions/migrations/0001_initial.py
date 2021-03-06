# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 19:30
from __future__ import unicode_literals

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_on', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_on', models.DateField(null=True)),
                ('step', models.CharField(default='', max_length=20)),
                ('answers', models.TextField(default='')),
                ('cc0', models.CharField(default='', max_length=255)),
                ('cc1', models.CharField(default='', max_length=255)),
                ('cc2', models.CharField(default='', max_length=255)),
                ('decision', models.CharField(default='', max_length=255)),
                ('cc', models.CharField(default='', max_length=255)),
                ('cc_not', models.CharField(default='', max_length=255)),
                ('decision_buddy', models.CharField(default='', max_length=80)),
                ('decision_buddy_email', models.EmailField(default='', max_length=80)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decisions.Course')),
            ],
        ),
    ]
