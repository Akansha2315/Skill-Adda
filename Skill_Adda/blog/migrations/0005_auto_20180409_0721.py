# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-09 07:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180408_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 7, 21, 55, 259830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 7, 21, 55, 258921, tzinfo=utc)),
        ),
    ]
