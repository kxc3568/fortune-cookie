# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fortune',
            old_name='fortune',
            new_name='message',
        ),
        migrations.AddField(
            model_name='fortune',
            name='emotions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]