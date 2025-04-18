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