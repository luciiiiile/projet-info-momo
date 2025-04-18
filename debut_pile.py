class pile():
    def __init__(self):
        self.souvenirs=[]
    
    def ajout_souvenir(self,souvenir):
        self.souvenirs.append(souvenir)
    
    def depiler(self):
        if self.souvenirs:
            return self.souvenirs.pop()
