from django.db import models

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=50)
    matricule = models.CharField(max_length=20)
    classe = models.CharField(max_length=20)
    sexe = models.CharField(max_length = 1)
    parrain = models.ForeignKey('Etudiant', on_delete = models.SET_NULL, blank = True, null = True)
    filleul = models.OneToOneField('Etudiant', on_delete = models.SET_NULL, blank = True,  null = True, related_name="Filleul")
    
    