# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-02-23 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmodule3',
            name='dd_params',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='module3',
            name='dd_params',
            field=models.TextField(default=''),
        ),
    ]
