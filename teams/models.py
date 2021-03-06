# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from competitions.models import Area, Competition

# Create your models here.
# Model to create individual teams.
class Team(models.Model):
	area = models.ForeignKey(Area, related_name='teams')
	competition = models.ManyToManyField(Competition, related_name='teams', blank=True)
	full_name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=15)
	abbreviation = models.CharField(max_length=3)
    	
	def __unicode__(self):
		return self.full_name