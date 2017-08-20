# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170525_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, unique=True)),
                ('intro_course', models.BooleanField(default=True)),
                ('time', models.IntegerField(choices=[(0, 'No preference'), (1, 'Morning'), (2, 'Afternoon'), (3, 'Evening')], default=0)),
                ('num_responses', models.IntegerField(default=0)),
                ('avg_age', models.IntegerField(default=20)),
            ],
        ),
    ]
