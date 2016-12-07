from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Logmodel(models.Model):
	log_task = models.TextField(max_length=400)
	log_sol = models.CharField(max_length=100, blank=True, null=True)
	log_answer = models.CharField(max_length=100, editable=False, blank=True, null=True)

	def __str__(self):
		return self.pk

