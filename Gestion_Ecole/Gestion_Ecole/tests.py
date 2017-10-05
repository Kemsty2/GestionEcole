from django.test import TestCase
from Gestion_Ecole.models import Classe, Eleve, Sequence,Note, Trimestre, Matiere
from Gestion_Ecole.EleveContext import GetEleveNote

class EleveTests(TestCase):
    
    def setUp(self):
        Classe.objects.create(Nom_Classe = "CM1")
        Trimestre.objects.create(Nom_Trimestre = "Trimestre 1")
        classe = Classe.objects.get(Nom_Classe = "CM1")
        Eleve.objects.create(Nom = "kemsty", Prenom = "moyo", Age= 4, Classe = classe)
        trimestre = Trimestre.objects.get(Nom_Trimestre = "Trimestre 1")        
        Sequence.objects.create(Nom = "Sequence 1", Trimestre = trimestre)
        Matiere.objects.create(Nom = "Anglais", Classe = classe)
        matiere = Matiere.objects.get(Nom = "Anglais")
        eleve = Eleve.objects.get(Nom = "kemsty")
        sequence = Sequence.objects.get(Nom = "Sequence 1")
        Note.objects.create(Note = 15, Eleve = eleve, Sequence = sequence, Matiere = matiere)
        
    def test_recupere_note_eleve(self):
        eleve = Eleve.objects.get(Nom = "kemsty")
        sequence = Sequence.objects.get(Nom = "Sequence 1")
        
        noteEleve = GetEleveNote(eleve.id, sequence.id)
        
        for note in noteEleve:
            self.assertEqual(note.Note, 15, "les notes correspondent")
        
        
        