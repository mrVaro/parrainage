from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EtudiantAdmin(ImportExportModelAdmin):
    list_display = ['nom', 'prenoms', 'matricule', 'classe', 'parrain', 'filleul']
    
admin.site.register(Etudiant, EtudiantAdmin)
