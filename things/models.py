from django.db import models

class Thing(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	quantity = models.IntegerField()
