class pile():
    def __init__(self):
        self.souvenirs=[]
    
    def ajout_souvenir(self,souvenir):
        self.souvenirs.append(souvenir)
    
    def depiler(self):
        if self.souvenirs:
            self.souvenirs.pop()

pile1=pile()
pile1.ajout_souvenir("Le tueur est Samuel")

print(pile1.souvenirs)