# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-28 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200628_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='static/img/teams/default-logo.png', upload_to='static/img/teams'),
        ),
    ]
