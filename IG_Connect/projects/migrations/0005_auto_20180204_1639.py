# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-04 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170703_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectName',
            field=models.CharField(max_length=200),
        ),
    ]