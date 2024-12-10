from fonction import *
from devinette import devinette
from allumette import allumette
from morpion import morpionjouer
from puissance4Bonus import puissance4

def main () :
    choix : int
    menu("main")
    menu("jeux")
    choix = int(inputCustom("Votre choix 0 / 1 / 2 / 3 / 4 / 5 : ", int, "La valeur doit être un entier", 0, 5))
    
    if choix == 0 : 
        lancement("devinette")
        devinette()
        
    if choix == 1 :
        lancement("allumette")
        allumette()
        
    if choix == 2 :
        lancement("morpion")
        morpionjouer()

    if choix == 3 :
        lancement("puissance4")
        puissance4()

    if choix == 4 :
        afficher_scores_total()

    if choix == 5 :
        menu("quitter")

##########################
# Lancement du programme #
##########################
if __name__ == "__main__":
    effacer_console()
    main()