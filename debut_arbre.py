import pygame  # Importer pygame pour gérer les sons
import random


class Noeud:
    def __init__(self,valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_choix(self, choix):
        self.enfants.append(choix)

    def afficher(self):
        print("User : quel est la personne que vous voulez voir ?")
        if self.enfants:
            print("les choix sont les suivants :")
            for enfant in (self.enfants):
                print(f"{self.enfants.index(enfant) + 1} : {enfant.valeur}")
            rep = int(input("Entrez le numero de la personne que vous voulez rencontrer :"))
            self.enfants[rep - 1].afficher()
        else:
            print("bruh")

def rencontre1(username):
    

racine=Noeud("Christopher")
print("bruh")

enfant1 = Noeud("facteur")
enfant2 = Noeud("boulanger")
enfant3 = Noeud("infirmiere")



petitenfant1 = Noeud("opticien")
petitenfant2 = Noeud("caissiere")
petitenfant3 = Noeud("vendeur_citron")

arrierepetitenfant1 = Noeud("leandre")
arrierepetitenfant2 = Noeud("samuel")


racine.enfants = [enfant1 , enfant2, enfant3]

enfant2.enfants = [petitenfant1, petitenfant2, petitenfant3]
petitenfant2.enfants = [arrierepetitenfant1, arrierepetitenfant2]

#input("*vous avez décidé d'aller voir les différentes personne de votre village afin dans apprendre plus sur ce qui c'est réellement passer cette soirée là*")

racine.afficher()
