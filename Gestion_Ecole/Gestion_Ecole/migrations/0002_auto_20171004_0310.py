# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Ecole', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='Nom_Mere',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Nom_Pere',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Numero_Mere',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Numero_Pere',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
