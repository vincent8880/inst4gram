# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 06:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pic',
        ),
    ]
