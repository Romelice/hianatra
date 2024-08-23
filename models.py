from django.db import models

# Create your models here.
class produit(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=1000)
 
class  categories(models.Model):
   name=models.CharField(max_length=200) 
   email=models.EmailField(default=True)
   
class commande(models.Model):
    name=models.CharField( max_length=50)
    image=models.ImageField(upload_to="file")
    
class PortfolioProduit(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='produits',blank=True,null=True)
class PortfolioService(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='services',blank=True,null=True)
    
class PortfolioExperts(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='experts',blank=True,null=True)    
    
    
class Reservations (models.Model):
    nom =models.CharField(max_length=200)
    prenom=models.CharField(max_length=500)
    email=models.EmailField(default=True)
    adresse=models.CharField(max_length=300, null=True,default=True)