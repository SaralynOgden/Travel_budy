# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('loginreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='trip',
            field=models.ManyToManyField(related_name='tripsusers', to='main.Trip'),
        ),
    ]