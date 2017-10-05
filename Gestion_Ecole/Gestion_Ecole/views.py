from Gestion_Ecole.forms import LoginForm, RegisterForm
from django.urls import reverse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http.response import HttpResponseRedirect
from .models import Directeur, Maitre, Personne, Classe
<<<<<<< HEAD
from django.views import generic

def login(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        return HttpResponseRedirect('/welcome')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                mot_de_passe = form.cleaned_data['mot_de_passe']
                logged_user = Personne.objects.get(Email = user_email, Mot_De_Passe = mot_de_passe)
                request.session['logged_user_id'] = logged_user.id
                return HttpResponseRedirect('/welcome')
            else:
                form = LoginForm()
                return render(request, 'Gestion_Ecole/login.html',
                    {'form':form, 'error' : "Email ou mot de passe incorrect."})
        else:
            form = LoginForm()
            return render(request, 'Gestion_Ecole/login.html', {'form':form})

def welcome(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        liste_classes = Classe.objects.order_by('id')
        return render(request, 'Gestion_Ecole/welcome.html',
            {'logged_user' : logged_user, 'liste_classes' : liste_classes})
    else:
        return HttpResponseRedirect('/login')
=======

def welcome(request):
    liste_classes = Classe.objects.order_by('id')
    return render(request, 'Gestion_Ecole/welcome.html', {'liste_classes' : liste_classes})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            logged_user = Personne.objects.get(Email = user_email, Mot_De_Passe = mot_de_passe)
            request.session['logged_user_id'] = logged_user.id
            return HttpResponseRedirect('/welcome')
        else:
            form = LoginForm()
            return render(request, 'Gestion_Ecole/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'Gestion_Ecole/login.html', {'form':form})
>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79

def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(Directeur.objects.filter(id=logged_user_id)) == 1:
            return Directeur.objects.get(id=logged_user_id)
<<<<<<< HEAD
=======
        elif len(Maitre.objects.filter(id=logged_user_id)) == 1:
            return Maitre.objects.get(id=logged_user_id)
>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79
        else:
            return None
    else:
        return None

def logout(request):
    del request.session['logged_user_id']
    return HttpResponseRedirect('/login')

def classe(request, classe_id):
<<<<<<< HEAD
    classe_choisie = get_object_or_404(Classe, pk=classe_id)
    liste_classes = Classe.objects.order_by('id')
    logged_user = Directeur.objects.get(id=request.session['logged_user_id'])
    try:
        liste_matieres = classe_choisie.matiere_set.all()
        print liste_matieres
        return render(request, 'Gestion_Ecole/classe.html',
            {
            'logged_user' : logged_user,
            'liste_matieres' : liste_matieres,
            'liste_classes' : liste_classes,
            'classe_choisie' : classe_choisie,
            })
    except:
        return render(request, 'Gestion_Ecole/welcome.html',
            {'logged_user' : logged_user, 'liste_classes' : liste_classes})
=======
    classe = get_object_or_404(Classe, pk=classe_id)
    try:
        matieres = Classe.objects.matiere_set.all()
        print('ok!!!')
        for matiere in matieres:
            print(matiere)
        return render(request, 'Gestion_Ecole/classe.html', {'matieres' : matieres})
    except:
        return render(request, 'Gestion_Ecole/welcome.html')
>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79