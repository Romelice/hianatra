from django import  forms
from pav.models import * 

class portfolioForm(forms.Form):
    nom=forms.CharField(max_length=500,required=False)
    prenom=forms.CharField(max_length=500,required=False)
    email=forms.EmailField(required=False,)
    phone=forms.IntegerField(required=False)
    adresse=forms.CharField(required=False)