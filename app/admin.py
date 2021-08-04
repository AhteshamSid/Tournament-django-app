# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ['date', 'team_1', 'team_2', 'player_1_score', 'player_2_score', 'winner']

    def save_model(self, request, obj, form, change):
        team1 = Team.objects.get(id=obj.team_1.id)

        if obj.winner is not None:
            team1.match_dates = obj.date
            team1.goal_scored = int(obj.player_1_score)
            team1.no_of_matches = 1

            team1.save()

            team2 = Team.objects.get(id=obj.team_2.id)

            team2.match_dates = obj.date
            team2.goal_scored = int(obj.player_2_score)
            team2.no_of_matches = 1
            team2.save()

            team = Team.objects.get(id=obj.winner.id)
            team.no_of_matches_win = 1
            team.save()

        obj.save()


admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Coach)
admin.site.register(Manager)
admin.site.register(Match, MatchAdmin)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Point_Table)
