# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-03-09 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module3', '0005_auto_20200302_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmodule3',
            name='at4',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='module3',
            name='at4',
            field=models.TextField(default=''),
        ),
    ]