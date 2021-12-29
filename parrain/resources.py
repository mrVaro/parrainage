from import_export import resources
from .models import *

class EtudiantResource(resources.ModelResource):
    class meta:
        model = Etudiant