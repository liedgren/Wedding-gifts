from django.db import models

class Gift(models.Model):
	name = models.CharField(max_length = 200)
	link = models.CharField(max_length = 200)
	number = models.IntegerField()
	bought = models.IntegerField(default = 0)

	def __unicode__(self):
		return u'%s' % (self.name)
