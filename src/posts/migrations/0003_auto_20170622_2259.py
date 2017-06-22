# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 22:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 6, 22, 22, 59, 50, 605324, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
