# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-16 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_app', '0007_auto_20170416_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='commitment',
            field=models.TextField(default=''),
        ),
    ]