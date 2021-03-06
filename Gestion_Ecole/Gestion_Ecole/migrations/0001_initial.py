# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Numero_Pere', models.CharField(max_length=10, null=True)),
                ('Numero_Mere', models.CharField(max_length=10, null=True)),
                ('Nom_Pere', models.CharField(max_length=50, null=True)),
                ('Nom_Mere', models.CharField(max_length=50, null=True)),
                ('Date_Inscription', models.DateField(auto_now_add=True)),
                ('Classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.FloatField()),
                ('Eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.Eleve')),
                ('Matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.Matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Mot_De_Passe', models.CharField(max_length=50)),
                ('Sexe', models.CharField(choices=[(b'M', b'Masculin'), (b'F', b'Feminin')], max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Directeur',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Gestion_Ecole.Personne')),
            ],
            bases=('Gestion_Ecole.personne',),
        ),
        migrations.CreateModel(
            name='Maitre',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Gestion_Ecole.Personne')),
                ('Age', models.IntegerField()),
                ('Numero_Telephone', models.CharField(max_length=20)),
                ('Actif', models.BooleanField(default=True)),
                ('Classes', models.ManyToManyField(to='Gestion_Ecole.Classe')),
            ],
            bases=('Gestion_Ecole.personne',),
        ),
        migrations.AddField(
            model_name='sequence',
            name='Trimestre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.Trimestre'),
        ),
        migrations.AddField(
            model_name='note',
            name='Sequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.Sequence'),
        ),
    ]
