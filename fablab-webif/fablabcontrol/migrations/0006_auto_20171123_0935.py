# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-23 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fablabcontrol', '0005_auto_20171123_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usagemonitor',
            name='datestop',
            field=models.DateTimeField(blank=True, verbose_name='Work end'),
        ),
    ]
