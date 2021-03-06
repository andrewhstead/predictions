# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_remove_competition_teams'),
        ('teams', '0003_remove_team_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='competitions.Area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='competition',
            field=models.ManyToManyField(blank=True, related_name='teams', to='competitions.Competition'),
        ),
    ]
