# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-02-17 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpocket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backpocket',
            name='dd_as_question',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='backpocket',
            name='problem_to_solve',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='historicalbackpocket',
            name='dd_as_question',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='historicalbackpocket',
            name='problem_to_solve',
            field=models.TextField(default=''),
        ),
    ]
