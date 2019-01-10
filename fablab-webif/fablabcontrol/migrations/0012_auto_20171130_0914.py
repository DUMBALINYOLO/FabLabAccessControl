# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-30 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fablabcontrol', '0011_auto_20171130_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='machines', to='fablabcontrol.FabLabUser', verbose_name='Assigned users'),
        ),
    ]