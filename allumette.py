from fonction import *
from time import sleep
from random import randint

def affichage_Partie_Allumette(ResteAllumette : int, joueur_actuel : str) -> None:
    """
    Fonction pour afficher le nombre d'allumettes restantes et le joueur qui doit jouer \n
    Paramètres : ResteAllumette (int), joueur_actuel (str) \n
    Retourne : None
    """

    effacer_console()
    nombrelignehorizontale(1, 55)
    print("\033[92m Vous êtes dans une partie d'allumettes \033[0m")
    nombrelignehorizontale(1, 55)
    print(f"\033[92mIl reste {ResteAllumette} allumettes.\033[0m")
    print(f"C'est au tour de \033[0;36m{joueur_actuel}\033[0m de jouer.")

####################################################################################################

def allumette():
    """
    Fonction pour jouer au jeu des allumettes \n
    Paramètres : None \n
    Retourne : None
    """

    ResteAllumette : int
    allumetteprise : int
    choixjoueurs : int
    joueur1 : str
    joueur2 : str
    joueur_actuel : str

    ResteAllumette = 20

    # Proposition réinitialisation des scores
    reinitialiser_scores_binaire("allumette")

    # Liste des joueurs
    listej = listejoueur("allumette")

    # Vérification si la liste contient bien deux joueurs
    if len(listej) < 2:
        print("Erreur : il doit y avoir exactement 2 joueurs.")
        return
    
    # Effacement de la console avec un sleep pour laisser le temps de lire
    sleep(3)
    effacer_console()
    nombrelignehorizontale(1, 55)
    print("\033[92m Lancement du jeu des allumettes \033[0m")
    nombrelignehorizontale(1, 55)

    # Assigner les joueurs aléatoirement
    choixjoueurs = randint(1, 2)

    if choixjoueurs == 1 :
        joueur1 = listej[0]
        joueur2 = listej[1]
    else :
        joueur1 = listej[1]
        joueur2 = listej[0] 
    
    # Déterminer qui commence, ici joueur1 commence en se basant sur le choixjoueurs qui est aléatoire
    joueur_actuel = joueur1   


    #Début du jeu
    while ResteAllumette > 0:

        # Afficher le nombre d'allumettes restantes et le joueur qui doit jouer
        affichage_Partie_Allumette(ResteAllumette, joueur_actuel)

        # Demander combien d'allumettes prendre
        allumetteprise = int(inputCustom(f"\033[0;36m{joueur_actuel}\033[0m : Combien d'allumettes voulez-vous prendre ? ", int, "La valeur doit être un entier", 1, 3))

        # Vérification que le joueur ne prend pas plus d'allumettes que celles restantes
        while allumetteprise > ResteAllumette:
            affichage_Partie_Allumette(ResteAllumette, joueur_actuel)
            print("Vous ne pouvez pas prendre plus d'allumettes qu'il n'en reste !")
            allumetteprise = int(inputCustom(f"\033[0;36m{joueur_actuel}\033[0m : Combien d'allumettes voulez-vous prendre ? ", int, "La valeur doit être un entier", 1, 3))

        # Vérifier si le joueur qui va jouer prend la dernière allumette
        if allumetteprise == ResteAllumette :  # Si le joueur prend toutes les allumettes restantes, il perd
            effacer_console()
            print(f"\033[31m{joueur_actuel}, vous avez perdu car vous avez pris la dernière allumette ! \033[0m")
            nombrelignehorizontale(1, 20)
            enregistrer_score_binaire("allumette", joueur_actuel, -1)  # Enregistrer le score du perdant

        ResteAllumette = ResteAllumette - allumetteprise

        # Alterner les joueurs
        if joueur_actuel == joueur1:
            joueur_actuel = joueur2
        else:
            joueur_actuel = joueur1

    afficher_scores_final("allumette")
    
    quitterjeux("allumette")
