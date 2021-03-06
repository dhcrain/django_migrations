# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 20:40
from __future__ import unicode_literals

from django.db import migrations
from take_two.models import SjBbStat


def add_data(apps, schema_editor):
    SjBbStat.objects.create(full_name='Tucker Cascadden', position='INF', number=17, avg=.268, hr=0, rbi=3, runs=7)
    SjBbStat.objects.create(full_name='Max Wood', position='OF', number=33, avg=.378, hr=7, rbi=48, runs=42)
    SjBbStat.objects.create(full_name='Aaron Bond', position='OF/RHP', number=34, avg=.200, hr=0, rbi=0, runs=3)
    SjBbStat.objects.create(full_name='Devin Wilson', position='INF', number=12, avg=.125, hr=0, rbi=2, runs=2)
    SjBbStat.objects.create(full_name='Chris Roberts', position='OF/RHP', number=34, avg=.200, hr=0, rbi=0, runs=3)
    SjBbStat.objects.create(full_name='Brandon Montgomery', position='INF', number=7, avg=.385, hr=6, rbi=40, runs=40)
    SjBbStat.objects.create(full_name='Donivan Lopez', position='INF/OF', number=20, avg=.346, hr=0, rbi=35, runs=37)
    SjBbStat.objects.create(full_name='Ryan January', position='C/OF', number=8, avg=.351, hr=10, rbi=45, runs=45)
    SjBbStat.objects.create(full_name='Liam Scafariello', position='INF/OF', number=44, avg=.314, hr=11, rbi=33, runs=22)
    SjBbStat.objects.create(full_name='Baine Schoenvogel', position='C/RHP', number=10, avg=.390, hr=2, rbi=24, runs=22)


class Migration(migrations.Migration):

    dependencies = [
        ('take_two', '0003_sjbbstat'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
