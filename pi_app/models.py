from __future__ import unicode_literals

from django.db import models

class Belt(models.Model):
	color = models.CharField(max_length = 10)
	def __unicode__(self):
		return u'%s' % self.color

class Employee(models.Model):
	employeeId = models.CharField(max_length = 6, unique = True)
	employeeName = models.CharField(max_length = 50)
	level = models.IntegerField(default = 1)
	belt = models.ForeignKey(Belt, null = True, blank = True)
	def __unicode__(self):
		return u'%s %s %s' % (self.employeeId, self.employeeName, self.level)
