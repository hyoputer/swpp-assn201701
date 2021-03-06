# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 06:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debtpages_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debts_as_borrower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debt',
            name='lender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debts_as_lender', to=settings.AUTH_USER_MODEL),
        ),
    ]
