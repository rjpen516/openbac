# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('open_relay', models.BooleanField()),
                ('open_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('action_taken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=14)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ipaddr', models.TextField()),
                ('install_date', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ipaddr', models.TextField()),
                ('install_date', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Location')),
                ('paired_reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Reader')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Reader'),
        ),
        migrations.AddField(
            model_name='event',
            name='relay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Relay'),
        ),
        migrations.AddField(
            model_name='access_group',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Action'),
        ),
        migrations.AddField(
            model_name='access_group',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Location'),
        ),
        migrations.AddField(
            model_name='access_group',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bac.Reader'),
        ),
    ]
