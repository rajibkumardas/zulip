# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0089_auto_20170710_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='high_contrast_mode',
            field=models.BooleanField(default=False),
        ),
    ]
