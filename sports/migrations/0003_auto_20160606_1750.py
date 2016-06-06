# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 17:50
from __future__ import unicode_literals

from django.db import migrations
from sports.models import SjBaseballStats


def add_data(apps, schema_editor):
    SjBaseballStats.objects.create(full_name='Tucker Cascadden', position='INF', number=17, avg=.268, hr=0, rbi=3, runs=7)
    SjBaseballStats.objects.create(full_name='Max Wood', position='OF', number=33, avg=.378, hr=7, rbi=48, runs=42)
    SjBaseballStats.objects.create(full_name='Aaron Bond', position='OF/RHP', number=34, avg=.200, hr=0, rbi=0, runs=3)
    SjBaseballStats.objects.create(full_name='Devin Wilson', position='INF', number=12, avg=.125, hr=0, rbi=2, runs=2)
    SjBaseballStats.objects.create(full_name='Chris Roberts', position='OF/RHP', number=34, avg=.200, hr=0, rbi=0, runs=3)
    SjBaseballStats.objects.create(full_name='Brandon Montgomery', position='INF', number=7, avg=.385, hr=6, rbi=40, runs=40)
    SjBaseballStats.objects.create(full_name='Donivan Lopez', position='INF/OF', number=20, avg=.346, hr=0, rbi=35, runs=37)
    SjBaseballStats.objects.create(full_name='Ryan January', position='C/OF', number=8, avg=.351, hr=10, rbi=45, runs=45)
    SjBaseballStats.objects.create(full_name='Liam Scafariello', position='INF/OF', number=44, avg=.314, hr=11, rbi=33, runs=34)
    SjBaseballStats.objects.create(full_name='Baine Schoenvogel', position='C/RHP', number=10, avg=.390, hr=2, rbi=24, runs=22)


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20160606_1746'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
