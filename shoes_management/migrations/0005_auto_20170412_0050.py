# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_management', '0004_auto_20170412_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='billitem',
            name='bill',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoes_management.Bill'),
        ),
        migrations.AddField(
            model_name='billitem',
            name='item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoes_management.ShoeInstance'),
        ),
    ]
