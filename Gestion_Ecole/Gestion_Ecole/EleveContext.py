"Contient toutes les fonctions a utiliser pour gerer les eleves "

from Gestion_Ecole.models import Eleve, Classe, Note, Sequence, Trimestre

def GetEleve(nom, prenom):
    "Recupere L'eleve de nom et de prenom (nom, prenom)"
    eleve = Eleve.objects.get(Nom = nom, Prenom = prenom)
    return eleve

def GetEleve(id):
    "Recupere l'eleve ayant l'id (id)"
    eleve = Eleve.objects.get(id = id)
    return eleve

def ListeEleveClasse(idClasse):
    "Recupere tout les eleves d'une classe"
    classe = Classe.objects.get(id = idClasse)
    ListeEleve = classe.eleve_set.all()
    return ListeEleve

def SupprimerEleve(id):
    "Supprimer un eleve avec son id"
    eleve = Eleve.objects.get(id = id)
    eleve.delete()

def SupprimerEleve(nom, prenom):
    "Supprimer un eleve avec son nom et prenom"
    eleve = Eleve.objects.get(Nom = nom, Prenom = prenom)
    eleve.delete()

def GetEleveNote(idEleve, idSequence):
    "Recuperer toutes les notes d'un eleve pour une sequence"
    eleve = Eleve.objects.get(id = idEleve)
    sequence = Sequence.objects.get(id = idSequence)
    notes = Note.objects.filter(Eleve = eleve, Sequence = sequence)
    return notes

def GetMoyenneEleve(idEleve, idSequence):
    "Recupere la moyenne d'un eleve lors d'une sequence"
    notes = GetEleveNote(idEleve, idSequence)
    moyenne = 0.0
    somme = 0.0
    for note in notes:
        somme = somme + note.Note
    moyenne = somme/notes.len()

    return moyenne


def ListeEleveNote(idSequence, idClasse):
    "Recuperer toutes les notes de tout les eleves d'une classe pour une sequence"

    listeEleve = ListeEleveClasse(idClasse)
    liste = []

    for eleve in listeEleve:
        liste.append((eleve,GetEleveNote(idEleve, idSequence) ))

    return liste

def ListeMoyenneEleve(idSequence, idClasse):
    "Recupere toutes les moyennes de tout les eleves d'une classe pour une sequence"
    liste = []
    listeEleve = ListeEleveClasse(idClasse)

    for eleve in listeEleve:
        liste.append((eleve, GetMoyenneEleve(idEleve, idSequence)))
    return liste

def RangSequence(idSequence, idClasse):
    "Recupere les rangs des eleves d'une classe pour une sequence"

    rang = 1
    liste = []
    moyenne_eleve = ListeMoyenneEleve(idSequence, idClasse)
    listeEleve = ListeEleveClasse(idClasse)
    moyenne_eleve = sorted(moyenne_eleve, key = lambda colonnes: colennes[1])

    for elt in moyenne_eleve:
        liste.append((eleve, rang))
        rang += 1
