# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('vnfs', '0002_vnf_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='vnf',
            name='log',
            field=models.TextField(blank=True, null=True),
        ),
    ]
