# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-28 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fablabcontrol', '0008_machine_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsageMonitor',
            new_name='UserActivityMonitor',
        ),
    ]
