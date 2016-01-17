# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia_platnosci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwota', models.FloatField(default=0.0)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_uslugi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='katalog.Usluga', to_field='katalog.Usluga.id_uslugi')),
            ],
        ),
        migrations.CreateModel(
            name='Platnosc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wartosc', models.FloatField(default=0.0)),
                ('czestotliwosc', models.IntegerField(default=1)),
                ('dlugosc', models.FloatField(null=True)),
                ('id_uslugi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='katalog.Usluga', to_field='katalog.Usluga.id_uslugi')),
            ],
        ),
    ]
