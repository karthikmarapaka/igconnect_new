# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.TextField(max_length=50)),
                ('projectDescription', models.TextField(max_length=50)),
                ('shortDesc', models.CharField(max_length=25)),
                ('projectImage', models.ImageField(blank=True, null=True, upload_to=projects.models.get_project_pic_path)),
                ('publishedDate', models.DateField()),
                ('branchList', models.TextField(null=True)),
                ('contributorsList', models.ManyToManyField(related_name='list_of_contributors', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
