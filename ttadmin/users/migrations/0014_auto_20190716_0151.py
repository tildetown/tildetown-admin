# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-07-16 01:51
from __future__ import unicode_literals

from django.db import migrations

def set_state(apps, _):
    Townie = apps.get_model('users', 'Townie')
    for townie in Townie.objects.all():
        if townie.reviewed:
            townie.state = Townie.ACCEPTED

        townie.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190716_0148'),
    ]

    operations = [
            migrations.RunPython(set_state)
    ]
