# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_room_win'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='win',
        ),
    ]
