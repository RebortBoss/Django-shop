# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-07 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='youneed_konw',
            field=models.CharField(default='', max_length=300, verbose_name='课程须知'),
        ),
    ]
