# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_management', '0003_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='sold_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
