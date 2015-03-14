from django.db import models

class Resource(models.Model):
	TYPE = (
		('1', 'video'),
		('2', 'tutorial'),
		('3', 'code')
	)
	title = models.CharField(max_length=200)
	link = models.URLField()
	resource_type = models.IntegerField(choices=TYPE)

	def __unicode__(self):
		return self.title



class Content(models.Model):
	TYPES = (
        (1, 'Sorting'),
        (2, 'Search'),
        (3, 'Data Structure'),
        (4, 'Heaps'),
        (5, 'Graphs'),
    )
	title  = models.CharField(max_length=200)
	description = models.TextField()
	tag = models.CharField(max_length=10)
	algo_type = models.IntegerField(choices=TYPES)
	resource = models.ManyToManyField(Resource)

	def __unicode__(self):
		return self.title

