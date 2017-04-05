# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Humormodel(models.Model):
    humor_task = models.TextField(max_length=400)
    def __str__(self):
        return str(self.pk)
