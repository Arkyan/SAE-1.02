from fonction import *

def main () :
    choix : int
    menu("main")
    menu("jeux")
    choix = int(inputCustom("Votre choix 1 / 2 / 3 / 4 / 5 / 6 : ", int, "La valeur doit être un entier", 1, 6))
    
    if choix == 1 : 
        lancement("devinette")
        
    if choix == 2 :
        lancement("allumette")
        
    if choix == 3 :
        lancement("morpion")

    if choix == 4 :
        lancement("puissance4")

    if choix == 5 :
        afficher_scores_total()

    if choix == 6 :
        menu("quitter")

##########################
# Lancement du programme #
##########################
if __name__ == "__main__":
    effacer_console()
    main()