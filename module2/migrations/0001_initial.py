# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-31 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decisions', '0015_auto_20180531_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_on', models.DateField(null=True)),
                ('step', models.CharField(default='', max_length=20)),
                ('answers', models.TextField(default='')),
                ('biases', models.TextField(default='')),
                ('nylah_bias', models.CharField(default='', max_length=40)),
                ('evidence0', models.CharField(default='', max_length=255)),
                ('evidence1', models.CharField(default='', max_length=255)),
                ('evidence2', models.CharField(default='', max_length=255)),
                ('fact0', models.CharField(default='', max_length=255)),
                ('source0', models.CharField(default='', max_length=255)),
                ('bias0', models.CharField(default='', max_length=255)),
                ('fact1', models.CharField(default='', max_length=255)),
                ('source1', models.CharField(default='', max_length=255)),
                ('bias1', models.CharField(default='', max_length=255)),
                ('fact2', models.CharField(default='', max_length=255)),
                ('source2', models.CharField(default='', max_length=255)),
                ('bias2', models.CharField(default='', max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decisions.Course')),
            ],
            options={
                'verbose_name': 'Module 2 Data',
                'verbose_name_plural': 'Module 2 Data',
            },
        ),
    ]
