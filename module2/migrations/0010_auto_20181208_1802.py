# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-08 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('module2', '0009_module2_my_remedy'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalModule2',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('answers', models.TextField(default='')),
                ('answers2', models.TextField(default='')),
                ('biases', models.TextField(default='')),
                ('my_bias', models.TextField(default='')),
                ('my_bias_impact', models.TextField(default='')),
                ('my_bias_remedy', models.TextField(default='')),
                ('my_remedy', models.TextField(default='')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='decisions.Course')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Module 2 Data',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(
            model_name='module2',
            name='bias0',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='bias1',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='bias2',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='evidence0',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='evidence1',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='evidence2',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='fact0',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='fact1',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='fact2',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='more_facts',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='nylah_bias',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='opinions',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='opinions_important',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='opinions_reality',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='perspective',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='source0',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='source1',
        ),
        migrations.RemoveField(
            model_name='module2',
            name='source2',
        ),
    ]
