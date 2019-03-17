# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-09 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module2', '0010_auto_20181208_1802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalmodule2',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Module 3 Data - Introduction to Mental Shortcuts'},
        ),
        migrations.AlterModelOptions(
            name='module2',
            options={'verbose_name': 'Module 3 Data - Introduction to Mental Shortcuts', 'verbose_name_plural': 'Module 3 Data - Introduction to Mental Shortcuts'},
        ),
    ]