import pygame  # Importer pygame pour gérer les sons
import random
from typing import Self
import questionary


from debut_villageois import Villageois

class Noeud:
    def __init__(self,villageois, parent : Self = None ):
        self.villageois = villageois 
        self.enfants = {}
        self.parent = parent 
        if self.parent != None :
            self.parent.ajouter_noeud(self) 

    def ajouter_noeud(self, noeud):
        self.enfants[noeud.villageois.nom] = noeud

    def afficher(self):
        

        #print(f"{self.villageois.nom} : {self.villageois.souvenir}")

        choix = questionary.select("Où souhaites-tu aller ensuite ?",choices = [enfant for enfant in self.enfants.keys()]).ask()
        

        return choix
        '''
        if self.enfants:
            print("Les choix sont les suivants :")
            if self.parent:
                print(f"0 : {self.parent.villageois}")
            for enfant in (self.enfants):
                print(f"{self.enfants.index(enfant) + 1} : {enfant.villageois.nom}")
            rep = int(float(input("Entrez le numero de la personne que vous voulez rencontrer :")))
            return rep
        else:
            print("bruh")
        '''