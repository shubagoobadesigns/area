# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-02-25 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module3', '0003_auto_20200225_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmodule3',
            name='br',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='module3',
            name='br',
            field=models.TextField(default=''),
        ),
    ]