# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-29 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_team_registration_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='status',
        ),
    ]
