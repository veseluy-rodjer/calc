# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Erudmodel(models.Model):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = [(a, 'вариант a'), (b, 'вариант b'), (c, 'вариант c'), (d, 'пропустить вопрос')]
    erud_task = models.TextField(max_length=400)
    erud_sol = models.CharField(default=None, max_length=100, choices=e, null=True)
    erud_answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.pk)
