# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 05:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basictracker',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 2, 5, 30, 49, 347034, tzinfo=utc)),
            preserve_default=False,
        ),
    ]