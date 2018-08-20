# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# Model to create individual teams.
class Team(models.Model):
	full_name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=15)
	abbreviation = models.CharField(max_length=3)
    	
	def __unicode__(self):
		return self.full_name