# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-06-19 13:16
from __future__ import unicode_literals

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('background_photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='photo',
            field=smartfields.fields.ImageField(upload_to=b''),
        ),
    ]