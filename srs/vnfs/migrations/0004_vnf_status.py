# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('vnfs', '0003_vnf_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='vnf',
            name='status',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
