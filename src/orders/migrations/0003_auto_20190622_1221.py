# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-22 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('orders', '0002_auto_20190619_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
            preserve_default=False,
        ),
    ]
