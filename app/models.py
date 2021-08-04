# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime, timedelta
from django.core.validators import RegexValidator


# Create your models here.


def MatchShedule(date, teams, venue):
    matches = Match()

    matches.date = date
    matches.team_1 = teams[0]
    matches.team_2 = teams[1]
    matches.venue = venue
    matches.save()

    return date


class Team(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    image = models.FileField(upload_to='teams/')
    goal_scored = models.IntegerField(default=0)
    no_of_matches = models.IntegerField(default=0)
    no_of_matches_win = models.IntegerField(default=0)
    match_dates = models.DateField('Date', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class TeamMember(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    team_name = models.ForeignKey(Team, related_name='team_name', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Coach(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    team_name = models.ForeignKey(Team, related_name='coach_team_name', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Manager(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                     message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(default="+91", validators=[phone_regex], max_length=17)
    name = models.CharField(max_length=100, blank=True, null=True)
    team_name = models.ForeignKey(Team, related_name='manager_team_name', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Match(models.Model):
    date = models.DateField('Date', null=True, blank=True)
    team_1 = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name="team_1")
    team_2 = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name="team_2")

    player_1_score = models.PositiveIntegerField(default=0)
    player_2_score = models.PositiveIntegerField(default=0)

    winner = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name="matches_won")

    def __str__(self):
        return str(self.date)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, default="others", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.description


class Point_Table(models.Model):
    name = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
