# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-22 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineAgecy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Phone',
            field=models.CharField(max_length=24),
        ),
    ]