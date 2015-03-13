from django.db import models


class Content(models.Model):
	TYPES = (
        (1, 'Sorting'),
        (2, 'Search'),
        (3, 'Data Structure'),
        (4, 'Heaps'),
        (5, 'Graphs')
    )
	title  = models.CharField(max_length=200)
	description = models.TextField()
	tag = models.CharField(max_length=10)
	algo_type = models.CharField(max_length=20, choices=TYPES)

	def __unicode__(self):
		return self.title
