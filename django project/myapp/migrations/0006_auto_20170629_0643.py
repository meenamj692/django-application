# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170629_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='imagefield',
            new_name='profile_pic',
        ),
    ]
