from debut_arbre import *
import debut_code,debut_personnageP

User = debut_personnageP.PersonnagePrincipal("User")
racine = Noeud(User.nom)

User.noeudCourant = racine

enfant1 = Noeud("facteur",racine)
enfant2 = Noeud("boulanger",racine)
enfant3 = Noeud("infirmiere",racine)

petitenfant1 = Noeud("opticien",enfant2)
petitenfant2 = Noeud("caissiere",enfant2)
petitenfant3 = Noeud("vendeur_citron",enfant2)

arrierepetitenfant1 = Noeud("leandre",petitenfant2)
arrierepetitenfant2 = Noeud("samuel",petitenfant2)

# racine.enfants = [enfant1 , enfant2, enfant3]

# enfant2.enfants = [petitenfant1, petitenfant2, petitenfant3]
# petitenfant2.enfants = [arrierepetitenfant1, arrierepetitenfant2]

jeu = debut_code.Jeu(User)
print("caca")
jeu.opening()