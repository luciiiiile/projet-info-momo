# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:36:59 2025

@author: gerem
"""
import time,os
import pygame  

import debut_personnageP,debut_arbre

pygame.mixer.init()

#Implémentations des sons qui vont servir tous le long du jeu
son_sonnerie = pygame.mixer.Sound("sons/sonnerie_telephone.mp3")

son_raccrocher = pygame.mixer.Sound("sons/raccrocher.mp3")

son_policed1 = pygame.mixer.Sound("sons/Police_dialogue1.mp3")

son_policed2 = pygame.mixer.Sound("sons/Police_dialogue2.mp3")

son_policed3 = pygame.mixer.Sound("sons/Police_dialogue3.mp3")

son_policed4 = pygame.mixer.Sound("sons/Police_dialogue4.mp3")


class Jeu():
    def __init__(self,user : debut_personnageP.PersonnagePrincipal):
        self.user = user

    #fontion qui lance les sons du jeu et qui permet d'instaurer un time.sleep de la durer du son 
    def jouer_son(son):
        son.play()
        time.sleep(son.get_length())

    #fontion qui lance les sons du jeu 
    def jouer_son(self,son):
        son.play()
        time.sleep(son.get_length())

    def afficher_titre(self):
        print("/////-----MNEMOSYS-----/////")
        print("")
        print("")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def opening(self):
        self.clear()
        print("Un jeu fait par Lucile Lagier et Gérémy Gamarra")
        print("")
        print("Inspiré de Memento de Christopher Nolan")
        print("")
        print("")
        self.afficher_titre()
        self.user.nom = str(input("Saisissez votre pseudo : ")).strip()
        print(f"Bienvenue {self.user.nom}...")
        time.sleep(1)
        input("Taper ENTRER pour commencer à jouer.")      
        print("Le jeu commence...")
        time.sleep(1)
        self.introduction()

    def introduction(self):
        self.clear()
        self.afficher_titre()
        input("*Vous venez de vous reveiller*")
        input("*Vous vous lever et vous allez pour vous habiller*") 
        input("*Le telephone sonne*")
        print("Telephone : << Dring Dring >>")
        self.jouer_son(son_sonnerie)
        input(f"{self.user.nom} : << Oui, Allo ? >>")
        print("Police : << Bonjour, c'est la police au téléphone. >>")
        self.jouer_son(son_policed1)
        print("Police : << Nous sommes dans le regret de vous annoncer que nous suspendons momentanément l'enquête sur la mort de votre frère. >>")
        self.jouer_son(son_policed2)
        input(f"{self.user.nom} : << Mais !! Qu'est ce que vous racontez ? >>")
        print("Police : << On comprend que cela est difficile à accepter, cependant nous sommes débordés. >>")
        self.jouer_son(son_policed3)
        print("Police : << Désolé. >>")
        self.jouer_son(son_policed4)
        input(f"{self.user.nom} : << Attendez Monsieur !... >>")
        print("Telephone : << Tut tut >>")
        self.jouer_son(son_raccrocher)
        input(f"{self.user.nom} : << Mon frère est mort ? Qu'est ce qui me raconte celui là ? >>")
        input("*Vous commencez à paniquer*")
        input(f"{self.user.nom} : << Je suis quasiment sur qu'on s'est vu hier. >>")
        input(f"{self.user.nom} : << Enfin... J'ai quelques flash-backs mais cela est assez flou. >>")
        input(f"{self.user.nom} : << C'est comme si mes souvenirs étaient enfouis dans ma mémoire. >>")
        input(f"{self.user.nom} : << Mais je suis incapable de me souvenir de ce qui s'est passé. >>")
        input("*Vous vous dites que vous allez surement trouver de l'aide dehors, en demandant aux autres villageois de Mnémosys*")
        choix1 = self.user.noeudCourant.afficher()
        Noeud2 = self.user.noeudCourant.enfants[choix1-1]
        print(Noeud2.villageois)

    def visit(noeud):
        pass
    #methode qui visite un noeud, afficher nom noeud ?vafficher souveneir ,afficher 
