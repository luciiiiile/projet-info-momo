from debut_arbre import *
import debut_code,debut_personnageP
from debut_pile import pile

User = debut_personnageP.PersonnagePrincipal("User")
main = Villageois(User.nom,"<< Faut que j'arrete de tourner en rond chez moi... >>")
racine = Noeud(main)

User.noeudCourant = racine

pile1 = pile()

pile1.ajout_souvenir("Mon troisième me sert à voler")
pile1.ajout_souvenir("Mon deuxième est le phénomène de remplacement de la peau chez le serpent")
pile1.ajout_souvenir("Mon premier est un déterminant possessif")

User.pile = pile1

facteur = Villageois("facteur","La dernière fois que j'ai vu ton frère, il avait une baguette dans la main.")
boulanger = Villageois("boulanger","Super, tu es sur la piste. Ton souvenir se dépile.")
sage_femme = Villageois("sage_femme","Il n'avait pas un colis à récupérer par hasard ?")

enfant1 = Noeud(facteur,racine)
enfant2 = Noeud(boulanger,racine)
enfant3 = Noeud(sage_femme,racine)

opticien = Villageois("opticien","Je lui ai parlé vers midi, il devait aller chercher des citrons.")
caissiere = Villageois("caissière","Bravo, encore un souvenir dépilé.")
vendeur_c = Villageois("vendeur_citron","Je l'ai aperçu faire son essence à côté du supermarché.")

petitenfant1 = Noeud(opticien,enfant2)
petitenfant2 = Noeud(caissiere,enfant2)
petitenfant3 = Noeud(vendeur_c,enfant2)

leandre = Villageois("leandre","Pas loin du tout.Je te débloque ton dernier souvenir.")
samuel = Villageois("samuel","Bah, ta belle soeur a accouché ! Tu ne t'en souviens pas ?")

arrierepetitenfant1 = Noeud(leandre,petitenfant2)
arrierepetitenfant2 = Noeud(samuel,petitenfant2)

liste_villageois = [facteur,boulanger,sage_femme,opticien,caissiere,vendeur_c,leandre,samuel]

jeu = debut_code.Jeu(User,liste_villageois)
jeu.init_balade(User.noeudCourant)
'''jeu.opening()'''