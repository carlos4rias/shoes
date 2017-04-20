# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes_management', '0005_auto_20170412_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemIncoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('incoming', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoes_management.Incoming')),
                ('item', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoes_management.ShoeInstance')),
            ],
        ),
    ]