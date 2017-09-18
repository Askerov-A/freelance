# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_content', models.CharField(max_length=1000)),
                ('date_of_pub', models.DateTimeField(verbose_name='Создано')),
                ('done', models.BooleanField(verbose_name='Доделано или нет')),
            ],
        ),
    ]