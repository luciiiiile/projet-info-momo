class Villageois():
    def __init__(self,nom):
        self.nom = nom
        souvenirs = [] #collection of Souvenir instance
    
    def donnerSouvenir(self):
        if self.souvenirs:
            return self.souvenirs[0]
