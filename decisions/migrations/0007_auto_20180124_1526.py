# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-24 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decisions', '0006_auto_20171130_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='module2',
            name='bias0',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='bias1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='bias2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='fact0',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='fact1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='fact2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='source0',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='source1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='module2',
            name='source2',
            field=models.CharField(default='', max_length=255),
        ),
    ]
