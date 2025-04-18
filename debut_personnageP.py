class PersonnagePrincipal():
    def __init__(self, nom):
        self.nom = nom
        self.noeudCourant = 0 #Noeud instance
        self.pile = [] #liste qui est debout
        self.souvenir = [] #liste qui est debout
    
    def parlerAvecVillageois(self):
        #Villageois in parameter, return a Souvenir
        pass
    
    def depilerSouvenir(self):
        souv = self.pile.pop()
        self.souvenir.append(souv)

    def trouverMeurtrier(self):
        #Meurtrier in parameter, return Void
        pass

    def deplacerVersNoeud(self):
        #Noeud in parameter, return Void
        pass