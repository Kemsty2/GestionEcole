from .forms import LoginForm, RegisterForm
from django.urls import reverse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http.response import HttpResponseRedirect
from .models import Directeur, Maitre, Personne, Classe, Eleve
from django.views import generic

def login(request):
    logged_user_name = get_logged_user_from_request(request)
    if logged_user_name:
        return HttpResponseRedirect('/welcome')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                mot_de_passe = form.cleaned_data['mot_de_passe']
                logged_user = Personne.objects.get(Email = user_email, Mot_De_Passe = mot_de_passe)
                request.session['logged_user_name'] = logged_user.Nom
                return HttpResponseRedirect('/welcome')
            else:
                form = LoginForm()
                return render(request, 'Gestion_Ecole/login.html',
                    {'form':form, 'error' : "Email ou mot de passe incorrect."})
        else:
            form = LoginForm()
            return render(request, 'Gestion_Ecole/login.html', {'form':form})

def welcome(request):
    logged_user_name = get_logged_user_from_request(request)
    if logged_user_name:
        liste_classes = Classe.objects.order_by('id')
        return render(request, 'Gestion_Ecole/welcome.html',
            {'logged_user_name' : logged_user_name, 'liste_classes' : liste_classes})
    else:
        return HttpResponseRedirect('/login')

def get_logged_user_from_request(request):
    if 'logged_user_name' in request.session:
        logged_user_name = request.session['logged_user_name']
        if len(Directeur.objects.filter(Nom=logged_user_name)) == 1:
            return logged_user_name
        else:
            return None
    else:
        return None

def logout(request):
    del request.session['logged_user_name']
    return HttpResponseRedirect('/login')

def classe(request, classe_id):
    classe_choisie = get_object_or_404(Classe, pk=classe_id)
    liste_classes = Classe.objects.order_by('id')
    logged_user_name = request.session['logged_user_name']
    try:
        liste_eleves = classe_choisie.eleve_set.order_by("Nom")
        return render(request, 'Gestion_Ecole/classe.html',
            {
            'logged_user_name' : logged_user_name,
            'liste_eleves' : liste_eleves,
            'liste_classes' : liste_classes,
            'classe_choisie' : classe_choisie,
            })
    except:
        return render(request, 'Gestion_Ecole/welcome.html',
            {'logged_user_name' : logged_user_name, 'liste_classes' : liste_classes})

def eleve(request, eleve_id):

    eleve_choisi = get_object_or_404(Eleve, pk=eleve_id)
    classe_choisie = Classe.objects.get(pk=eleve_choisi.Classe.id)
    liste_classes = Classe.objects.order_by('id')
    logged_user_name = request.session['logged_user_name']
    try:
        print request.POST
        liste_matieres = classe_choisie.matiere_set.order_by("Nom")
        return render(request, 'Gestion_Ecole/eleve.html',
            {
            'logged_user_name' : logged_user_name,
            'liste_classes' : liste_classes,
            'liste_matieres' : liste_matieres,
            'eleve_choisi' : eleve_choisi,
            'classe_choisie' : classe_choisie,
            })
    except:
        return render(request, 'Gestion_Ecole/welcome.html',
            {'logged_user_name' : logged_user_name, 'liste_classes' : liste_classes})
