# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-02-17 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpocket', '0005_auto_20200217_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='backpocket',
            name='at2_most',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='backpocket',
            name='at3_most',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='historicalbackpocket',
            name='at2_most',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='historicalbackpocket',
            name='at3_most',
            field=models.TextField(default=''),
        ),
    ]