# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-28 15:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='venue',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
