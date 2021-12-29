from django.shortcuts import render
#from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import static
import pandas as pd
import random
from .models import *
from .resources import EtudiantResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from datetime  import date

def s_upload(request):
    '''if request.method == 'POST':
        Etud_res = EtudiantResource
        dataset = Dataset()
        new_etud1 = request.FILES['myfile1']
        new_etud2 = request.FILES['myfile2']
        if not new_etud1.name.endswith('xlsx'):
            messages.info(request, 'Faux fichier')
            return render(request, 'upload.html')
        
        imported_data1 = dataset.load(new_etud1.read(), format='xlsx')
        imported_data2 = dataset.load(new_etud2.read(), format='xlsx')
        
        today = date.today()

        # ici on cherche a avoir la date courante afin de determiner les 
        # etudiant ayant repris la L1 et ceux qui sont nouveaux
        # cette distinction de fati su la base des deux premiere lettres du matricule

        CurrentYear = today.strftime("%Y")
        TwolastLetterThisYear = CurrentYear[-2:]



        licence1 = []
        licence2 = []

        # SRIT

        licence1SRIT = []
        licence2SRIT = []

        # SIGL 

        licence1SIGL = []
        licence2SIGL = []

        # TWIN

        licence1TWIN = []
        licence2TWIN = []

        # RTEL

        licence1RTEL = []
        licence2RTEL = []



        ## Ici on fait la liste globale des etudiants de la licence 1
        for i in range(2, len(imported_data1)):
            
            
            personne = {
                "Matricule" : imported_data1.values[i,1],
                "Nom" : imported_data1.values[i,2] + " " + imported_data1.values[i,3],
                "Genre" : imported_data1.values[i,4],
                "Classe" : imported_data1.values[i,5]
            }
            
            # idYearMat représente l'identifiant en terme d'année du matricule de l'étudiant en question
            
            idYearMat = personne.get('Matricule')[0:2]
            
            if(int(idYearMat) >=  int(TwolastLetterThisYear) ):
                #print(personne.get('Matricule'))
                
                # Remplissage de la liste des licences 1
                
                
                if(personne.get('Classe').find("RTEL") != -1):
                    
                    licence1RTEL.append(personne)
                    
                elif(personne.get('Classe').find("SIGL") != -1):
                    
                    licence1SIGL.append(personne)
                    
                elif(personne.get('Classe').find("TWIN") != -1):
                    
                    licence1TWIN.append(personne)
                
                else:
                    
                    licence1SRIT.append(personne)
                
                

        ## Ici on fait la liste globale des etudiants de la licence 2

        for i in range(2, len(imported_data2)):
            
            
            personne = {
                "Matricule" : imported_data2.values[i,1],
                "Nom" : imported_data2.values[i,2] + " " + imported_data2.values[i,3],
                "Genre" : imported_data2.values[i,4],
                "Classe" : imported_data2.values[i,5]
            }
            
            # idYearMat représente l'identifiant en terme d'année du matricule de l'étudiant en question
            
            idYearMat = personne.get('Matricule')[0:2]
            goodL2StartMatId =  int(TwolastLetterThisYear) - 1
            if(int(idYearMat) == goodL2StartMatId ):
                #print(personne.get('Matricule'))
                
                # Remplissage de la liste des licences 1
                
                #licence2.append(personne)
                
                if(personne.get('Classe').find("RTEL") != -1):
                    
                    licence2RTEL.append(personne)
                    
                elif(personne.get('Classe').find("SIGL") != -1):
                    
                    licence2SIGL.append(personne)
                    
                elif(personne.get('Classe').find("TWIN") != -1):
                    
                    licence2TWIN.append(personne)
                
                else:
                    
                    licence2SRIT.append(personne)
            
        #print(licence2)


        # partie SRIT

            
            nbL1SRIT = len(licence1SRIT)
            nbL2SRIT = len(licence2SRIT)




        ## Code de parrainage 

            print("\n")
            print("\n")
            print("  srit           (Matricule , nom )  LICENCE 2  ====>   (Matricule , nom )   LICENCE 1 ")

            print("\n")

            i=0


            while(i < min(nbL1SRIT, nbL2SRIT) ):
                
                random.shuffle(licence1SRIT)
                random.shuffle(licence2SRIT)
                
                if(i+1 < 10) :
                    print( "0{}".format(i+1),"| ",  licence2SRIT[0].get('Matricule') ,": " , licence2SRIT[0].get('Nom') , " ====> ",  licence1SRIT[0].get('Matricule') ,": ", licence1SRIT[0].get('Nom'))
                else :
                    print( i+1,"| ",  licence2SRIT[0].get('Matricule') ,": " , licence2SRIT[0].get('Nom') , " ====> ",  licence1SRIT[0].get('Matricule') ,": ", licence1SRIT[0].get('Nom'))
                    
                    
                i += 1
                licence1SRIT.pop(0)
                licence2SRIT.pop(0)
                

            if(len(licence1SRIT)>0):
                
                i = 0
                
                while (i < len(licence1SRIT)) :
                    #print(licence1SRIT[i])
                    licence1.append(licence1SRIT[i])
                    i += 1
                    
            if(len(licence2SRIT) > 0 ):
                
                i = 0
                
                while (i < len(licence2SRIT)) :
                    #print(licence2SRIT[i])
                    licence2.append(licence2SRIT[i])
                    i += 1




            # PARTIE SIGL


                
            nbL1SIGL = len(licence1SIGL)
            nbL2SIGL = len(licence2SIGL)




            ## Code de parrainage 

            print("\n")
            print("\n")
            print("  SIGL           (Matricule , nom )  LICENCE 2  ====>   (Matricule , nom )   LICENCE 1 ")

            print("\n")

            i=0


            while(i < min(nbL1SIGL, nbL2SIGL) ):
                
                random.shuffle(licence1SIGL)
                random.shuffle(licence2SIGL)
                
                if(i+1 < 10) :
                    print( "0{}".format(i+1),"| ",  licence2SIGL[0].get('Matricule') ,": " , licence2SIGL[0].get('Nom') , " ====> ",  licence1SIGL[0].get('Matricule') ,": ", licence1SIGL[0].get('Nom'))
                else :
                    print( i+1,"| ",  licence2SIGL[0].get('Matricule') ,": " , licence2SIGL[0].get('Nom') , " ====> ",  licence1SIGL[0].get('Matricule') ,": ", licence1SIGL[0].get('Nom'))
                    
                    
                i += 1
                licence1SIGL.pop(0)
                licence2SIGL.pop(0)
                

            if(len(licence1SIGL)>0):
                
                i = 0
                
                while (i < len(licence1SIGL)) :
                    #print(licence1SIGL[i])
                    licence1.append(licence1SIGL[i])
                    i += 1
                    
            if(len(licence2SIGL) > 0 ):
                
                i = 0
                
                while (i < len(licence2SIGL)) :
                    #print(licence2SIGL[i])
                    licence2.append(licence2SIGL[i])
                    i += 1


            print("\n ")
            print("\n")


            ################ PARTIE RTEL


                
            nbL1RTEL = len(licence1RTEL)
            nbL2RTEL = len(licence2RTEL)




            ## Code de parrainage 

            print("\n")
            print("\n")
            print("  RTEL           (Matricule , nom )  LICENCE 2  ====>   (Matricule , nom )   LICENCE 1 ")

            print("\n")

            i=0


            while(i < min(nbL1RTEL, nbL2RTEL) ):
                
                random.shuffle(licence1RTEL)
                random.shuffle(licence2RTEL)
                
                if(i+1 < 10) :
                    print( "0{}".format(i+1),"| ",  licence2RTEL[0].get('Matricule') ,": " , licence2RTEL[0].get('Nom') , " ====> ",  licence1RTEL[0].get('Matricule') ,": ", licence1RTEL[0].get('Nom'))
                else :
                    print( i+1,"| ",  licence2RTEL[0].get('Matricule') ,": " , licence2RTEL[0].get('Nom') , " ====> ",  licence1RTEL[0].get('Matricule') ,": ", licence1RTEL[0].get('Nom'))
                    
                    
                i += 1
                licence1RTEL.pop(0)
                licence2RTEL.pop(0)
                

            if(len(licence1RTEL)>0):
                
                i = 0
                
                while (i < len(licence1RTEL)) :
                    #print(licence1RTEL[i])
                    licence1.append(licence1RTEL[i])
                    i += 1
                    
            if(len(licence2RTEL) > 0 ):
                
                i = 0
                
                while (i < len(licence2RTEL)) :
                    #print(licence2RTEL[i])
                    licence2.append(licence2RTEL[i])
                    i += 1



            ############### PARTIE TWIN


                
            nbL1TWIN = len(licence1TWIN)
            nbL2TWIN = len(licence2TWIN)




            ## Code de parrainage 

            print("\n")
            print("\n")
            print("  TWIN           (Matricule , nom )  LICENCE 2  ====>   (Matricule , nom )   LICENCE 1 ")

            print("\n")

            i=0


            while(i < min(nbL1TWIN, nbL2TWIN) ):
                
                random.shuffle(licence1TWIN)
                random.shuffle(licence2TWIN)
                
                if(i+1 < 10) :
                    print( "0{}".format(i+1),"| ",  licence2TWIN[0].get('Matricule') ,": " , licence2TWIN[0].get('Nom') , " ====> ",  licence1TWIN[0].get('Matricule') ,": ", licence1TWIN[0].get('Nom'))
                else :
                    print( i+1,"| ",  licence2TWIN[0].get('Matricule') ,": " , licence2TWIN[0].get('Nom') , " ====> ",  licence1TWIN[0].get('Matricule') ,": ", licence1TWIN[0].get('Nom'))
                    
                    
                i += 1
                licence1TWIN.pop(0)
                licence2TWIN.pop(0)
                

            if(len(licence1TWIN)>0):
                
                i = 0
                
                while (i < len(licence1TWIN)) :
                    #print(licence1TWIN[i])
                    licence1.append(licence1TWIN[i])
                    i += 1
                    
            if(len(licence2TWIN) > 0 ):
                
                i = 0
                
                while (i < len(licence2TWIN)) :
                    #print(licence2TWIN[i])
                    licence2.append(licence2TWIN[i])
                    i += 1



            
            nbL1 = len(licence1)
            nbL2 = len(licence2)

            ## si le nombre de L1 depasse celui des l2 completer la liste des Licence 2

            if(nbL1 > nbL2):
                
                nbRestant = nbL1 - nbL2
                
                if nbL2 == 0:   
                    
                    TableauAleatoir = random.sample( range(0, len(imported_data2)), nbRestant)
                    
                    for i in TableauAleatoir:
                        
                        personne = {
                                "Matricule" : imported_data2.values[i,1],
                                "Nom" : imported_data2.values[i,2] + " " + imported_data2.values[i,3],
                                "Genre" : imported_data2.values[i,4],
                                "Classe" : imported_data2.values[i,5]
                            }
                        licence2.append(personne)
                        
                        


            ## Code de parrainage 

            print("\n")
            print("\n")
            print(" RESTANT            (Matricule , nom )  LICENCE 2  ====>   (Matricule , nom )   LICENCE 1 ")

            print("\n")

            i=0


            while(i < nbL1):
                
                random.shuffle(licence1)
                random.shuffle(licence2)
                
                if(i+1 < 10) :
                    print( "0{}".format(i+1),"| ",  licence2[0].get('Matricule') ,": " , licence2[0].get('Nom') , " ====> ",  licence1[0].get('Matricule') ,": ", licence1[0].get('Nom'))
                else :
                    print( i+1,"| ",  licence2[0].get('Matricule') ,": " , licence2[0].get('Nom') , " ====> ",  licence1[0].get('Matricule') ,": ", licence1[0].get('Nom'))
                    
                    
                i += 1
                licence1.pop(0)
                licence2.pop(0)


            

            ### elle n'est pas encore bien définie il faudra la poffiner

            def ParrainageFiliere(filiere , imported_data1, imported_data2):
                
                Level1 = []
                Level2 = []
                
                for i in range(2, len(imported_data1)):
                    
                    personne = {
                        "Matricule" : imported_data1.values[i,1],
                        "Nom" : imported_data1.values[i,2] + " " + imported_data1.values[i,3],
                        "Genre" : imported_data1.values[i,4],
                        "Classe" : imported_data1.values[i,5]
                    }
                    
                    # idYearMat représente l'identifiant en terme d'année du matricule de l'étudiant en question
                    
                    idYearMat = personne.get('Matricule')[0:2]
                    
                    if(int(idYearMat) >=  int(TwolastLetterThisYear) ):
                        #print(personne.get('Matricule'))
                        
                        # Remplissage de la liste des licences 1
                        
                        if(personne.get('Classe').find(filiere) != -1):
                            
                            Level1.append(personne)
                        
                        
                        

                ## Ici on fait la liste globale des etudiants de la licence 2
                
                for i in range(2, len(imported_data2)):
                    
                    
                    personne = {
                        "Matricule" : imported_data2.values[i,1],
                        "Nom" : imported_data2.values[i,2] + " " + imported_data2.values[i,3],
                        "Genre" : imported_data2.values[i,4],
                        "Classe" : imported_data2.values[i,5]
                    }
                    
                    # idYearMat représente l'identifiant en terme d'année du matricule de l'étudiant en question
                    
                    idYearMat = personne.get('Matricule')[0:2]
                    goodL2StartMatId =  int(TwolastLetterThisYear) - 1
                    if(int(idYearMat) == goodL2StartMatId ):
                        #print(personne.get('Matricule'))
                        
                        # Remplissage de la liste des licences 1
                        
                        #licence2.append(personne)
                        
                        if(personne.get('Classe').find(filiere)!= -1):
                            
                            Level2 .append(personne)
                                

                nbL1 = len(Level1)
                nbL2 = len(Level2)
                
                
                i=0
                
                
                while(i < min(nbL1, nbL2) ):
                    
                    random.shuffle(licence1RTEL)
                    random.shuffle(licence2RTEL)
                    
                    if(i+1 < 10) :
                        print( "0{}".format(i+1),"| ",  licence2RTEL[0].get('Matricule') ,": " , licence2RTEL[0].get('Nom') , " ====> ",  licence1RTEL[0].get('Matricule') ,": ", licence1RTEL[0].get('Nom'))
                    else :
                        print( i+1,"| ",  licence2RTEL[0].get('Matricule') ,": " , licence2RTEL[0].get('Nom') , " ====> ",  licence1RTEL[0].get('Matricule') ,": ", licence1RTEL[0].get('Nom'))
                        
                        
                    i += 1
                    licence1RTEL.pop(0)
                    licence2RTEL.pop(0)
                    
                
                if(len(licence1RTEL)>0):
                    
                    i = 0
                    
                    while (i < len(licence1RTEL)) :
                        #print(licence1RTEL[i])
                        licence1.append(licence1RTEL[i])
                        i += 1
                        
                if(len(licence2RTEL) > 0 ):
                    
                    i = 0
                    
                    while (i < len(licence2RTEL)) :
                        #print(licence2RTEL[i])
                        licence2.append(licence2RTEL[i])
                        i += 1

    return render(request, 'upload.html')


def home(request):
    '''
    
    return render(request, 'home.html')
