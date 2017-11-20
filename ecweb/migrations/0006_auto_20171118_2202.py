# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecweb', '0005_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menssage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menssage', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date_start',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='event',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='local',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='calendar',
            name='menssage',
            field=models.ManyToManyField(to='ecweb.Menssage'),
        ),
    ]