# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookauthor', to='book_review.Authors'),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='review',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
