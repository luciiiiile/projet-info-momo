import pygame  # Importer pygame pour gérer les sons
import random
from typing import Self
import questionary


from debut_villageois import Villageois

class Noeud:
    def __init__(self,villageois: str, parent : Self = None ):
        self.villageois= villageois 
        self.enfants = []
        self.parent = parent 
        if parent != None :
            parent.ajouter_choix(self) 

    def ajouter_choix(self, choix):
        self.enfants.append(choix)

    def afficher(self):
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