# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.CharField(choices=[('BTech', 'B.Tech'), ('MTech', 'M.Tech'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('PHD', 'Phd')], default='BTech', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('MECH', 'Mechanical Engineering'), ('ME', 'Metallurgy Engineering'), ('CHE', 'Chemical Engineering'), ('CIVIL', 'Civil Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('BIO', 'Biotechnology')], max_length=10),
        ),
    ]
