# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-23 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TxnBuffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('receiver', models.CharField(max_length=255)),
                ('product_hash', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
