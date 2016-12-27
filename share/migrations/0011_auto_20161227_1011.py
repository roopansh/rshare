# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 10:11
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_auto_20161224_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2017, 1, 3), help_text='Choose the expiry date of the file. NOTE: By default, the file would expire after 7 days of uploading'),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
