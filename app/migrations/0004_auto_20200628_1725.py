# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-28 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200628_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.FileField(upload_to='teams/'),
        ),
    ]
