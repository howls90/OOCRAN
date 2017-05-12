# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-01 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RRH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ip', models.CharField(max_length=120)),
                ('place', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=120)),
                ('longitude', models.CharField(max_length=120)),
                ('pt', models.IntegerField(default=20)),
                ('neighbor', models.CharField(blank=True, max_length=500, null=True)),
                ('bw', models.CharField(max_length=500)),
                ('driver_version', models.CharField(max_length=20)),
                ('freCs', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('first_band', models.CharField(max_length=50)),
                ('second_band', models.CharField(max_length=50)),
                ('third_band', models.CharField(max_length=50)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-update'],
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='EETAC', max_length=120)),
                ('latitude', models.FloatField(default='41.275621', max_length=120)),
                ('longitude', models.FloatField(default='1.986591', max_length=120)),
                ('description', models.TextField(default='Sample one mobile network deployed on the EETAC')),
                ('total_infras', models.IntegerField(default=0)),
                ('active_infras', models.IntegerField(default=0)),
                ('ips', models.IntegerField(default=2)),
                ('file', models.FileField(upload_to='scenarios/')),
                ('price', models.FloatField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operators.Operator')),
                ('rrh', models.ManyToManyField(to='scenarios.RRH')),
            ],
            options={
                'ordering': ['-timestamp', '-update'],
            },
        ),
    ]
