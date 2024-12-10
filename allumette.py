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

def bot_allumette(difficulte : int, nbr_allumette_restante : int) -> int :
    """
    Fonction pour le bot pour le jeu des allumettes.
    Args:
        difficulte (int): La difficulté du bot.
    Returns:
        int: Le nombre d'allumettes à retirer.
    """
    i : int
    nbr_allumettes_prise : int
    nbr_allumettes_prise = 0

    if difficulte == 0 :
        nbr_allumettes_prise = randint(1, 3)
        print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
        return nbr_allumettes_prise
    
    elif difficulte == 1 :
        n : int
        n = randint(1, 7)
        if n < 4 :
            nbr_allumettes_prise = randint(1, 3)
            print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
            return nbr_allumettes_prise
        else :
            for i in range(1, 5) :
                if nbr_allumette_restante - 1 == 4*i :
                    nbr_allumettes_prise = nbr_allumette_restante - 1
                    print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                    return nbr_allumettes_prise
                elif nbr_allumette_restante - 2 == 4*i :
                    nbr_allumettes_prise = nbr_allumette_restante - 2
                    print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                    return nbr_allumettes_prise
                elif nbr_allumette_restante - 3 == 4*i :
                    nbr_allumettes_prise = nbr_allumette_restante - 3
                    print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                    return nbr_allumettes_prise
                else :
                    nbr_allumettes_prise = randint(1, 3)
                    print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                    return nbr_allumettes_prise
    else :
        for i in range(1, 5) :
            if nbr_allumette_restante - 1 == 4*i :
                nbr_allumettes_prise = nbr_allumette_restante - 1
                print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                return nbr_allumettes_prise
            elif nbr_allumette_restante - 2 == 4*i :
                nbr_allumettes_prise = nbr_allumette_restante - 2
                print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                return nbr_allumettes_prise
            elif nbr_allumette_restante - 3 == 4*i :
                nbr_allumettes_prise = nbr_allumette_restante - 3
                print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                return nbr_allumettes_prise
            else :
                nbr_allumettes_prise = randint(1, 3)
                print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
                return nbr_allumettes_prise
    print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
    return nbr_allumettes_prise

####################################################################################################

def allumette():
    """
    Fonction pour jouer au jeu des allumettes \n
    Paramètres : None \n
    Retourne : None
    """

    ResteAllumette : int
    allumetteprise : int
    joueur1 : str
    joueur2 : str
    joueur_actuel : str

    ResteAllumette = 20

    # Proposition réinitialisation des scores
    reinitialiser_scores_binaire("allumette")

    #Choix du mode de jeu ainsi que de la difficulté
    mode_jeu = choix_mode_jeu()
    if mode_jeu == 0 :
        print("Vous avez choisi le mode Joueur contre Joueur")
        difficulte = 0
    else :
        difficulte = choix_difficulte()
    

# ──────────────────────────────────────────────────────────────
#                ASSIGNATION DES JOUEURS AU HASARD
# ──────────────────────────────────────────────────────────────
    j = randint(1, 2)

    #Choix des joueurs
    #Mode Joueur contre Joueur
    if mode_jeu == 0 :
        # Liste des joueurs
        listej = listejoueur("allumette", mode_jeu)
    
        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]
    
    #Mode Joueur contre IA
    elif mode_jeu == 1 :
        # Liste des joueurs
        listej = listejoueur("allumette", mode_jeu)

        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]

    #Mode IA contre IA
    elif mode_jeu == 2 :
        listej = listejoueur("allumette", mode_jeu)

        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :  
            joueur1 = listej[1]
            joueur2 = listej[0]
    
    else :
        #Nom par défaut si problème
        print("Pas normal si nous sommes ici")
        listej = ["Joueur 1", "Joueur 2"]
        joueur1 = listej[0]
        joueur2 = listej[1]

    # Effacement de la console avec un sleep pour laisser le temps de lire
    sleep(3)
    effacer_console()
    nombrelignehorizontale(1, 55)
    print("\033[92m Lancement du jeu des allumettes \033[0m")
    nombrelignehorizontale(1, 55)
    
    joueur_actuel = joueur1
# ──────────────────────────────────────────────────────────────
#                     MODE JOUEUR CONTRE JOUEUR
# ──────────────────────────────────────────────────────────────
    if mode_jeu == 0 :
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
                if joueur_actuel != "IA1" :
                    enregistrer_score_binaire("allumette", joueur_actuel, -1)
                else :
                    print("Pas de score pour les IA")

            ResteAllumette = ResteAllumette - allumetteprise

            # Alterner les joueurs
            if joueur_actuel == joueur1:
                joueur_actuel = joueur2
            else:
                joueur_actuel = joueur1

# ──────────────────────────────────────────────────────────────
#                MODE JOUEUR CONTRE IA
# ──────────────────────────────────────────────────────────────
    elif mode_jeu == 1 :
        while ResteAllumette > 0:

            # Afficher le nombre d'allumettes restantes et le joueur qui doit jouer
            affichage_Partie_Allumette(ResteAllumette, joueur_actuel)

            if joueur_actuel == "IA1" :
                sleep(2)
                allumetteprise = bot_allumette(difficulte, ResteAllumette)
                sleep(2)
            else :
                allumetteprise = int(inputCustom(f"\033[0;36m{joueur_actuel}\033[0m : Combien d'allumettes voulez-vous prendre ? ", int, "La valeur doit être un entier", 1, 3))

            # Vérification que le joueur ne prend pas plus d'allumettes que celles restantes
            while allumetteprise > ResteAllumette:
                affichage_Partie_Allumette(ResteAllumette, joueur_actuel)
                print("Vous ne pouvez pas prendre plus d'allumettes qu'il n'en reste !")

                if joueur_actuel == "IA1" :
                    sleep(1)
                    allumetteprise = bot_allumette(difficulte, ResteAllumette)
                    sleep(1)
                else :
                    allumetteprise = int(inputCustom(f"\033[0;36m{joueur_actuel}\033[0m : Combien d'allumettes voulez-vous prendre ? ", int, "La valeur doit être un entier", 1, 3))

            # Vérifier si le joueur qui va jouer prend la dernière allumette
            if allumetteprise == ResteAllumette :
                effacer_console()
                print(f"\033[31m{joueur_actuel}, vous avez perdu car vous avez pris la dernière allumette ! \033[0m")
                nombrelignehorizontale(1, 20)
                if joueur_actuel != "IA1" :
                    enregistrer_score_binaire("allumette", joueur_actuel, -1)
                else :
                    print("Pas de score pour les IA")

            ResteAllumette = ResteAllumette - allumetteprise

            # Alterner les joueurs
            if joueur_actuel == joueur1:
                joueur_actuel = joueur2
            else:
                joueur_actuel = joueur1

# ──────────────────────────────────────────────────────────────
#                MODE IA CONTRE IA
# ──────────────────────────────────────────────────────────────
    elif mode_jeu == 2 :
        while ResteAllumette > 0:

            # Afficher le nombre d'allumettes restantes et le joueur qui doit jouer
            affichage_Partie_Allumette(ResteAllumette, joueur_actuel)

            sleep(1)
            allumetteprise = bot_allumette(difficulte, ResteAllumette)
            sleep(1)

            # Vérification que le joueur ne prend pas plus d'allumettes que celles restantes
            while allumetteprise > ResteAllumette:
                affichage_Partie_Allumette(ResteAllumette, joueur_actuel)
                print("Vous ne pouvez pas prendre plus d'allumettes qu'il n'en reste !")
                sleep(1)
                allumetteprise = bot_allumette(difficulte, ResteAllumette)
                sleep(1)

            # Vérifier si le joueur qui va jouer prend la dernière allumette
            if allumetteprise == ResteAllumette :
                effacer_console()
                print(f"\033[31m{joueur_actuel}, vous avez perdu car vous avez pris la dernière allumette ! \033[0m")
                nombrelignehorizontale(1, 20)
                print("Pas de score pour les IA")
            
            ResteAllumette = ResteAllumette - allumetteprise
    
            # Alterner les joueurs
            if joueur_actuel == joueur1:
                joueur_actuel = joueur2
            else:
                joueur_actuel = joueur1

    afficher_scores_final("allumette")
    quitterjeux("allumette")
