# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-14 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alg', '0008_remove_solution_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='sol',
            field=models.IntegerField(null=True),
        ),
    ]
