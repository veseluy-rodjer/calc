# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-02 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('humor', '0002_auto_20170403_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='humormodel',
            name='humor_answer',
        ),
        migrations.RemoveField(
            model_name='humormodel',
            name='humor_exp',
        ),
        migrations.RemoveField(
            model_name='humormodel',
            name='humor_sol',
        ),
    ]
