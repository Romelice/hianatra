from django.shortcuts import render

# Create your views here.
from.models import*
from .forms import *


def homeView(request):
    return render(request, "portfolio/cv.html")

# Create your views here.
def  VueBoutiqueView(request):
        produits = produit.objects.all()
        categorie = categories.objects.all()
        commandes_recentes = commande.objects.all()
        context={
            'produit':produits,
             'categories':categorie,
             'commande':commandes_recentes
        }
        return render(request,"./portfolio/boutique.html",context)

def  portfolioView(request):
        pdt = PortfolioProduit.objects.all()
        pts= PortfolioService.objects.all()
        pte = PortfolioExperts.objects.all()
        context={
            'portfolioProduit':pdt,
             'portfolioservice':pts,
             'porfolioexperts':pte,
        }
        return render(request,"portfolio/portfolio.html",context)

def PortfoliocreateView(request):
    message=''
    if request.method=="POST":
        data=request.POST
        nom=data.get('nom')
        prenom=data.get('prenom')
        email=data.get('email')
        adresse=data.get('adresse')
        Reservations.objects.create(nom=nom,prenom=prenom,email=email,adresse=adresse)
        message='Votre reservation a eté bien enregistré'
    return render(request,"portfolio/portfoliocreate.html",{'message':message})

def PortfolioformView(request):
    form=portfolioForm(request.POST )
    message=''
    if form.is_valid():
        data=form.changed_data
        Reservations.objects.create(data)

        message='le produit a été bien enregistré'
       
    return render(request,"portfolio/portfolioForm.html",context={'form':form,'message':message})