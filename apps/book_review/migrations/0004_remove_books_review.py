# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0003_auto_20161118_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='review',
        ),
    ]
