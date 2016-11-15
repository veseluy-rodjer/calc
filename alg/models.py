from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Solution(models.Model):
	task = models.CharField(max_length=50)
	sol = models.IntegerField(blank=True, null=True)
	answer = models.IntegerField(editable=False, blank=True, null=True)
	check = models.CharField(max_length=20, blank=True, null=True)
	def __str__(self):
		return self.task