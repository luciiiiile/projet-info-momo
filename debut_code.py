import time,os
import pygame 
import questionary 

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
    def __init__(self,user : debut_personnageP.PersonnagePrincipal,liste_villageois):
        self.user = user
        self.liste_villageois = liste_villageois

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

    def init_balade(self,noeud):
        self.presentation_noeud(noeud)
        self.balade(noeud)

    def presentation_noeud(self,noeud):
        '''if noeud.villageois != 'racine':
            input(f"{noeud.villageois.nom} : {noeud.villageois.souvenir}")'''
        input(f"{noeud.villageois.nom} : {noeud.villageois.souvenir}")

        if noeud.villageois.nom in ['boulanger','caissière','leandre']:
            if noeud.villageois.nom == 'boulanger' and len(self.user.souvenir) == 0:
                self.user.souvenir.append(self.user.pile.depiler())
            if noeud.villageois.nom == 'caissière' and len(self.user.souvenir) == 1:
                self.user.souvenir.append(self.user.pile.depiler())
            if noeud.villageois.nom == 'leandre' and len(self.user.souvenir) == 2:
                self.user.souvenir.append(self.user.pile.depiler())
        

    def balade(self,noeud):
        courant = noeud

        while True:

            choix = questionary.select("Tu peux :",choices = ['Soupçonner une personne','Aller parler aux gens','Voir ta mémoire']).ask()
            
            if choix == 'Soupçonner une personne':
                tueur = questionary.select("Avez vous un suspect en tête ?", choices = [v.nom for v in self.liste_villageois] + ['Aucun']).ask()
                if tueur == "samuel":
                    print("Tu as trouvé le tueur ! Bravo !")
                    break
                else:
                    print("Ce n'était pas la bonne personne...")
                               
            if choix == 'Aller parler aux gens':
                
                if not courant.parent:
                    newNoeud = questionary.select("Tu peux aller voir :",choices = [enfant for enfant in courant.enfants.keys()]).ask()
                    futur = noeud.enfants[newNoeud]

                if courant.parent:   
                    liste_enfant_noeud = [enfant for enfant in courant.enfants.keys()]
                    liste_p = [courant.parent.villageois.nom]

                    newNoeud = questionary.select("Tu peux aller voir :",choices = liste_p + liste_enfant_noeud ).ask() 
                    if newNoeud in liste_enfant_noeud:
                        futur = courant.enfants[newNoeud]
                    else:
                        futur = courant.parent
                courant = futur
                self.presentation_noeud(courant)
                        
            
            if choix == 'Voir ta mémoire':
                if self.user.souvenir:
                    print(self.user.souvenir)
                else:
                    print("Ta mémoire est vide")


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
        self.balade(self.user.noeudCourant)
