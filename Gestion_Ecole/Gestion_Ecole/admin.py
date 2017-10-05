from django.contrib import admin
from Gestion_Ecole.models import Eleve, Maitre, Matiere, Note, Sequence, Trimestre, Directeur, Classe, Personne


admin.site.register(Eleve)
admin.site.register(Maitre)
admin.site.register(Matiere)
admin.site.register(Directeur)
admin.site.register(Note)
admin.site.register(Classe)
admin.site.register(Sequence)
admin.site.register(Trimestre)
admin.site.register(Personne)
