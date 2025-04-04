# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:36:59 2025

@author: gerem
"""
import time,os
import pygame  

pygame.mixer.init()

#Implémentations des sons qui vont servir tous le long du jeu
son_sonnerie = pygame.mixer.Sound("sons/sonnerie_telephone.mp3")

son_raccrocher = pygame.mixer.Sound("sons/raccrocher.mp3")

son_policed1 = pygame.mixer.Sound("sons/Police_dialogue1.mp3")

son_policed2 = pygame.mixer.Sound("sons/Police_dialogue2.mp3")

son_policed3 = pygame.mixer.Sound("sons/Police_dialogue3.mp3")

son_policed4 = pygame.mixer.Sound("sons/Police_dialogue4.mp3")

#fontion qui lance les sons du jeu et qui permet d'instaurer un time.sleep de la durer du son 
def jouer_son(son):
    son.play()
    time.sleep(son.get_length())



def afficher_titre():
    print("/////-----MNEMOSYS-----/////")
    print("")
    print("")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def opening():
    clear()
    print("Un jeu fait par Lucile Lagier et Gérémy Gamarra")
    print("")
    print("Inspiré de Memento de Christopher Nolan")
    print("")
    print("")
    afficher_titre()
    username = str(input("Saisissez votre pseudo : ")).strip()
    print(f"Bienvenue {username}...")
    time.sleep(1)
    input("Taper ENTRER pour commencer à jouer.")      
    print("Le jeu commence...")
    time.sleep(1)
    introduction(username)

def introduction(username):
    clear()
    afficher_titre()
    input("*Vous venez de vous reveiller*")
    input("*Vous vous lever et vous allez pour vous habiller*") 
    input("*Le telephone sonne*")
    print("Telephone : << Dring Dring >>")
    jouer_son(son_sonnerie)
    input(f"{username} : << Oui, Allo ? >>")
    print("Police : << Bonjour, c'est la police au téléphone. >>")
    jouer_son(son_policed1)
    print("Police : << Nous sommes dans le regret de vous annoncer que nous suspendons momentanément l'enquête sur la mort de votre frère. >>")
    jouer_son(son_policed2)
    input(f"{username} : << Mais !! Qu'est ce que vous racontez ? >>")
    print("Police : << On comprend que cela est difficile à accepter, cependant nous sommes débordés. >>")
    jouer_son(son_policed3)
    print("Police : << Désolé. >>")
    jouer_son(son_policed4)
    input(f"{username} : << Attendez Monsieur !... >>")
    print("Telephone : << Tut tut >>")
    jouer_son(son_raccrocher)
    input(f"{username} : << Mon frère est mort ? Qu'est ce qui me raconte celui là ? >>")
    input("*Vous commencez à paniquer*")
    input(f"{username} : << Je suis quasiment sur qu'on s'est vu hier. >>")
    input(f"{username} : << Enfin... J'ai quelques flash-backs mais cela est assez flou. >>")
    input(f"{username} : << C'est comme si mes souvenirs étaient enfouis dans ma mémoire. >>")
    input(f"{username} : << Mais je suis incapable de me souvenir de ce qui s'est passé. >>")
    input("*Vous vous dites que vous allez surement trouver de l'aide dehors, en demandant aux autres villageois de Mnémosys*")
    #rencontre1(username)
    
"""def rencontre1(username):
    pass"""
     
opening()
