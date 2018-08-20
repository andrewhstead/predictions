# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# The country or continent in which a competition is based.
class Area(models.Model):
	name = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=3)

	def __unicode__(self):
		return self.name


# The details of a competition.
class Competition(models.Model):
	area = models.ForeignKey(Area, related_name='competitions')
	name = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=3)
    	
	def __unicode__(self):
		return self.name