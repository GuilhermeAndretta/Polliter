# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('initials', models.CharField(max_length=10)),
                ('vision', models.CharField(max_length=1000)),
                ('picture', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=45)),
                ('about', models.CharField(max_length=1000)),
                ('picture', models.CharField(max_length=1000)),
                ('political_party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='politician.PoliticalParty')),
            ],
        ),
    ]
