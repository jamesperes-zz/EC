# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecweb', '0012_studenttests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menssage',
            old_name='menssage',
            new_name='menssage_text',
        ),
        migrations.AddField(
            model_name='classroom',
            name='nivel',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Elementary', 'Elementary')], max_length=30),
        ),
        migrations.AddField(
            model_name='classroom',
            name='number_class',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='grades',
            field=models.ManyToManyField(to='ecweb.StudentTests'),
        ),
    ]