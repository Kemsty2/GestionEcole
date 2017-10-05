
from Gestion_Ecole.models import Directeur, Maitre, Personne
from django.forms.models import ModelForm
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required = True)
    mot_de_passe = forms.CharField(label='Mot de Passe', widget = forms.PasswordInput, required = True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        mot_de_passe = cleaned_data.get("mot_de_passe")

        if email and mot_de_passe:
            result = Personne.objects.filter(Mot_De_Passe= mot_de_passe, Email = email)

            if(len(result) != 1):
                raise forms.ValidationError("Adresse de courriel ou mot de passe errone(e).")

        return cleaned_data


class RegisterForm(forms.ModelForm):
    class meta:
        model = Maitre
        exclude = ('Actif',)
