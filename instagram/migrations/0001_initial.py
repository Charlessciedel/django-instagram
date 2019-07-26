# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('name', models.TextField(default='Anonymous')),
                ('profile_pic', models.ImageField(default='users/user.png', upload_to='users/')),
                ('bio', models.TextField(default='Welcome Me!')),
            ],
        ),
    ]
