from django.db import models

# Create your models here.

class Etudiant(models.Model):
    matricule = models.CharField(max_length=20)
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=50)
    sexe = models.CharField(max_length = 1)
    classe = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True)
    
    
class Parrainage(models.Model):
    MatParrain = models.CharField(max_length=30, null=True, blank=True)   
    MatFilleul = models.CharField(max_length=30, null=True, blank=True)  
    

"""
parrain = models.ForeignKey('Etudiant', on_delete = models.SET_NULL, blank = True, null = True)
filleul = models.OneToOneField('Etudiant', on_delete = models.SET_NULL, blank = True,  null = True, related_name="Filleul")   
"""