from django.db import models


class Content(models.Model):
	title  = models.CharField(max_length=200)
	description = models.TextField()
	tag = models.CharField(max_length=10)
	algo_type = models.CharField(max_length=20)

	def __unicode__(self):
		return self.title
