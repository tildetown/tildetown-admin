# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-01-19 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_auto_20171110_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
