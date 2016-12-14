# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Logmodel(models.Model):
    a = 'v1'
    b = 'v2'
    c = 'v3'
    x = 'v4'
    a_a = 'A < B'
    b_b = 'A > B'
    c_c = 'A = B'
    x_x = 'пропустить вопрос'
    d = [(a, a_a), (b, b_b), (c, c_c), (x, x_x)]
    log_task = models.TextField(max_length=400)
    log_sol = models.CharField(default=None, max_length=100, choices=d)
    log_answer = models.CharField(max_length=100, blank=True)

    def __str__(self):
		return str(self.pk)

