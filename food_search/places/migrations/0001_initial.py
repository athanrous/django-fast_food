# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='images/', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('menu', models.CharField(max_length=100)),
                ('web', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='images/', null=True)),
                ('map', models.ImageField(upload_to='images/', null=True)),
                ('gmap_url', models.CharField(null=True, max_length=200)),
                ('votes', models.IntegerField(default=4, choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('food', models.ForeignKey(to='places.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='town',
            field=models.ForeignKey(to='places.Town'),
        ),
    ]
