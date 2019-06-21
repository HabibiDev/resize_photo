# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-06-20 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('background_photo', '0005_auto_20190620_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='photo',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='original_photo',
            field=models.ImageField(blank=True, null=True, upload_to='story1399/original'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='resize_photo',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to='story1399'),
        ),
    ]