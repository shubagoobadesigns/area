# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 04:20
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ArchetypesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ArchType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=0)),
                ('arch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area_app.ArchetypesModel')),
            ],
        ),
        migrations.CreateModel(
            name='CheetahSheets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet', models.CharField(max_length=128)),
                ('archetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area_app.ArchetypesModel')),
            ],
        ),
        migrations.CreateModel(
            name='CriticalConcepts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept1', models.CharField(default='', max_length=256)),
                ('concept2', models.CharField(default='', max_length=256)),
                ('concept3', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DecisionTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision_type', models.CharField(max_length=255)),
                ('decision', models.CharField(max_length=255)),
                ('options', models.CharField(max_length=255)),
                ('time_frame', models.CharField(max_length=255)),
                ('decision_type_other', models.CharField(max_length=255)),
                ('success', models.CharField(max_length=255)),
                ('commitment_days', models.IntegerField(default=7)),
                ('commitment', models.TextField(default='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40, null=True)),
                ('answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=256)),
                ('answer_yes', models.CharField(max_length=256, null=True)),
                ('answer_no', models.CharField(max_length=256, null=True)),
                ('why', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to='area_app.QuestionModel'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='decisiontypes',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area_app.Problem'),
        ),
        migrations.AddField(
            model_name='criticalconcepts',
            name='problem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='area_app.Problem'),
        ),
        migrations.AddField(
            model_name='archtype',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area_app.Problem'),
        ),
    ]
