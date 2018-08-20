# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from competitions.models import Competition
from teams.models import Team

# Create your models here.
# Model to create individual teams.
class Game(models.Model):
	competition = models.ForeignKey(Competition, related_name='games')
	game_date = models.DateField()
	game_time = models.TimeField()
	home_team = models.ForeignKey(Team, related_name='game_home')
	away_team = models.ForeignKey(Team, related_name='game_away')
	home_score = models.IntegerField(blank=True, null=True)
	away_score = models.IntegerField(blank=True, null=True)
    	
	def __unicode__(self):
		return self.full_name