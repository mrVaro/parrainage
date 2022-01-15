from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EtudiantAdmin(ImportExportModelAdmin):
    list_display = ['nom', 'prenoms', 'matricule', 'classe', 'sexe']
    
class ParrainageAdmin(ImportExportModelAdmin):
    list_display = ['MatParrain', 'MatFilleul']
    
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Parrainage, ParrainageAdmin)