# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-27 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logica', '0012_auto_20161227_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodel',
            name='log_sol',
            field=models.CharField(choices=[('v1', 'A < B'), ('v2', 'A > B'), ('v3', 'A = B'), ('v4', '\u043f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441')], default=None, max_length=100, null=True),
        ),
    ]
