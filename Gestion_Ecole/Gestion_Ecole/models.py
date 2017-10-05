'''
Created on 30 sept. 2017

@author: kemsty
'''
from django.db import models
from datetime import datetime
from django.db.models.fields.related import ManyToManyField
from django.db.models.fields import DateTimeField

class Personne(models.Model):
    Nom = models.CharField(max_length = 50)
    Prenom = models.CharField(max_length = 50)
    Mot_De_Passe = models.CharField(max_length = 50)
    SEXE_CHOICE = (
        ('M', 'Masculin'),
        ('F', 'Feminin')
        )
    Sexe = models.CharField(max_length = 10, choices = SEXE_CHOICE)
    Email = models.EmailField()
<<<<<<< HEAD
    def __str__(self):
        return self.Email
#    class Meta:
#        abstract = True

class Classe(models.Model):
    Nom = models.CharField(max_length = 50)
=======

    def __str__(self):
        return self.Email

class Classe(models.Model):
    Nom = models.CharField(max_length = 50)

>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79
    def __str__(self):
        return self.Nom

class Trimestre(models.Model):
    Nom = models.CharField(max_length = 50)
<<<<<<< HEAD
    Date = models.DateField(auto_now = True, auto_now_add = False)
=======
    Date = models.DateField(auto_now = True,auto_now_add = False)

>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79
    def __str__(self):
        return self.Nom


class Directeur(Personne):
    type_personne = 'directeur'
    def __str__(self):
        return self.Nom

class Maitre(Personne):
    type_personne = 'maitre'
    Age = models.IntegerField()
<<<<<<< HEAD
=======
    #Photo = models.ImageField(upload_to = 'Images/', default = 'Images/no-img.jpg')
>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79
    Numero_Telephone = models.CharField(max_length = 20)
    Classes = ManyToManyField(Classe)
    Actif = models.BooleanField(default = True) #c'est le directeur qui doit activer leur compte ou un super administrateur

    def __str__(self):
        return self.Nom + " " + self.Prenom

class Sequence(models.Model):
    Nom = models.CharField(max_length = 50)
    Trimestre = models.ForeignKey(Trimestre, null= True)
    Date = models.DateField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.Nom

class Eleve(models.Model):
    type_personne = 'eleve'
    Nom = models.CharField(max_length = 50)
    Prenom = models.CharField(max_length = 50)
    Age = models.IntegerField()
<<<<<<< HEAD
    Numero_Pere = models.CharField(max_length = 10, null = True, blank=True)
    Numero_Mere = models.CharField(max_length = 10, null = True, blank=True)
    Nom_Pere = models.CharField(max_length = 50, null = True, blank=True)
    Nom_Mere = models.CharField(max_length = 50, null = True, blank=True)
=======
    #Photo = models.ImageField(upload_to = 'Images/', default = 'Images/no-img.jpg')
    Numero_Pere = models.CharField(max_length = 10, null = True)
    Numero_Mere = models.CharField(max_length = 10, null = True)
    Nom_Pere = models.CharField(max_length = 50, null = True)
    Nom_Mere = models.CharField(max_length = 50, null = True)
>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79
    Classe = models.ForeignKey(Classe)
    Date_Inscription = models.DateField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.Nom + " " + self.Prenom


class Matiere(models.Model):
    Nom = models.CharField(max_length = 50)
    Classe = models.ForeignKey(Classe)

    def __str__(self):
        return self.Nom

class Note(models.Model):
    Note = models.FloatField()
    Eleve = models.ForeignKey(Eleve)
    Matiere = models.ForeignKey(Matiere)
    Sequence = models.ForeignKey(Sequence)

    def __str__(self):
        return self.Eleve.Nom + " " + self.Sequence.Nom
