# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180108_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.IntegerField(blank=True, choices=[(1, '一级类别'), (2, '二级类别')], null=True, verbose_name='类别级别'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='books.Category', verbose_name='子类别'),
        ),
    ]
