# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='politicians',
            field=models.ManyToManyField(to='politician.Politician'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='themes',
            field=models.ManyToManyField(to='theme.Theme'),
        ),
    ]