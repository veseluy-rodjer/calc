# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-02 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Humormodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erud_task', models.TextField(max_length=400)),
                ('erud_sol', models.CharField(choices=[('a', '\u0432\u0430\u0440\u0438\u0430\u043d\u0442 a'), ('b', '\u0432\u0430\u0440\u0438\u0430\u043d\u0442 b'), ('c', '\u0432\u0430\u0440\u0438\u0430\u043d\u0442 c')], default=None, max_length=100, null=True)),
                ('erud_answer', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
