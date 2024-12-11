from fonction import *
from time import sleep
from random import randint

def plateau(grille: list[list[str]]) -> None:
    """
    Affiche le plateau de jeu avec des lignes et colonnes numérotées.
    Chaque case est reliée à une grille.
    :param grille: Liste de listes représentant le plateau de jeu
    """
    effacer_console()
    print("    1   2   3   4   5   6   7")  # En-tête des colonnes
    print("  +" + "   +" * 7)  # Ligne supérieure

    for i, ligne in enumerate(grille):  # Parcourt chaque ligne de la grille
        print(f"{i + 1} |" + "|".join(f" {case} " for case in ligne) + "|")  # Affiche les cases
        print("  +" + "---+" * 7)  # Ligne de séparation

    

############################################################
############################################################
############################################################

def verif_plein (grille: list[list[str]]) -> bool:
    """ 
    Vérifie si la grille est pleine.
    Args:
        grille (list[list[str]]): Grille de jeu.
    Returns:
        bool : True si la grille est pleine, False sinon.
    """

    for ligne in grille:  # Parcourt chaque ligne de la grille
        if " " in ligne:  # S'il reste une case vide
            return False  # La grille n'est pas pleine
    return True  # La grille est pleine

############################################################
############################################################
############################################################

def verif_victoire(grille: list[list[str]], joueur: str) -> bool:
    """
    Vérifie si un joueur a gagné.
    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Joueur actuel.
    Returns:
        bool : True si un joueur a gagné, False sinon.
    """

    for i in range(6):  # Parcourt les lignes
        for j in range(7):  # Parcourt les colonnes
            if grille[i][j] == joueur:  # Si la case contient le jeton du joueur
                if j + 3 < 7 and grille[i][j + 1] == grille[i][j + 2] == grille[i][j + 3] == joueur:  # Vérifie l'horizontale
                    return True
                if i + 3 < 6:
                    if grille[i + 1][j] == grille[i + 2][j] == grille[i + 3][j] == joueur:  # Vérifie la verticale
                        return True
                    if j + 3 < 7 and grille[i + 1][j + 1] == grille[i + 2][j + 2] == grille[i + 3][j + 3] == joueur:  # Vérifie la diagonale droite
                        return True
                    if j - 3 >= 0 and grille[i + 1][j - 1] == grille[i + 2][j - 2] == grille[i + 3][j - 3] == joueur:  # Vérifie la diagonale gauche
                        return True
    return False

############################################################
############################################################
############################################################

def colonne_pleine(grille: list[list[str]], colonne: int) -> bool:
    """
    Vérifie si une colonne est pleine.
    Args:
        grille (list[list[str]]): Grille de jeu.
        colonne (int): Colonne choisie par le joueur.
    Returns:
        bool : True si la colonne est pleine, False sinon.
    """

    if  " " in grille[0][colonne]:
        return False
    else:
        return True


############################################################
############################################################
############################################################

def occurencejouer(grille: list[list[str]], joueur: str, colonne: int) -> None:
    """
    Joue un coup.
    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Joueur actuel.
        colonne (int): Colonne choisie par le joueur.
    Returns:
        None : None
    """
    
    case_placee = False  # Variable pour savoir si un jeton a été placé
    
    for i in range(5, -1, -1):  # Parcourt les lignes de la colonne choisie
        if grille[i][colonne] == " " and not case_placee:  # Si la case est vide et qu'un jeton n'a pas encore été placé
            grille[i][colonne] = joueur  # Place le jeton du joueur
            case_placee = True  # On marque qu'un jeton a été placé
    
    # La boucle se termine sans le besoin de `break`, car `case_placee` gère l'arrêt du placement.

############################################################
############################################################
############################################################

def bot_puissance4(grille: list[list[str]], joueur: str, difficulte: int) -> int:
    """
    Fonction qui permet à l'IA de choisir une colonne pour jouer.
    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Joueur actuel.
        difficulte (int): Difficulté de l'IA.
    Returns:
        int : Colonne choisie par l'IA.
    """
    colonne : int
    colonne = 1  # Colonne par défaut

    # Difficulté hasard
    if difficulte == 0:
        colonne = randint(1, 7)  # Choix aléatoire de la colonne
        print(f"L'IA a choisi la colonne {colonne}.")

    return colonne

############################################################
############################################################
############################################################

#Initialisation du jeu
def puissance4() -> None:
    """
    Jeu Puissance 4.
    Args:
        None : None
    Returns:
        None : None
    """

    grille = [[" " for _ in range(7)] for _ in range(6)]  # Grille de jeu
    victoire = False  # Indique si une victoire a eu lieu
    plein = False  # Indique si la grille est pleine

    # Réinitialisation des scores
    reinitialiser_scores_binaire("puissance4")

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
        listej = listejoueur("morpion", mode_jeu)
    
        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
            signe1 = "\033[33m■\033[0m" # Couleur jaune 🟡
            signe2 = "\033[31m■\033[0m" # Couleur rouge 🔴
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]
            signe1 = "\033[31m■\033[0m" # Couleur rouge 🔴
            signe2 = "\033[33m■\033[0m" # Couleur jaune 🟡
    
    #Mode Joueur contre IA
    elif mode_jeu == 1 :
        # Liste des joueurs
        listej = listejoueur("morpion", mode_jeu)

        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
            signe1 = "\033[33m■\033[0m" # Couleur jaune 🟡
            signe2 = "\033[31m■\033[0m" # Couleur rouge 🔴
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]
            signe1 = "\033[31m■\033[0m" # Couleur rouge 🔴
            signe2 = "\033[33m■\033[0m" # Couleur jaune 🟡

    #Mode IA contre IA
    elif mode_jeu == 2 :
        listej = listejoueur("morpion", mode_jeu)

        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
            signe1 = "\033[33m■\033[0m" # Couleur jaune 🟡
            signe2 = "\033[31m■\033[0m" # Couleur rouge 🔴
        else :  
            joueur1 = listej[1]
            joueur2 = listej[0]
            signe1 = "\033[31m■\033[0m" # Couleur rouge 🔴
            signe2 = "\033[33m■\033[0m" # Couleur jaune 🟡
    
    else :
        #Nom par défaut si problème
        print("Pas normal si nous sommes ici")
        listej = ["Joueur 1", "Joueur 2"]
        joueur1 = listej[0]
        joueur2 = listej[1]
        signe1 = "\033[33m■\033[0m" # Couleur jaune 🟡
        signe2 = "\033[31m■\033[0m" # Couleur rouge 🔴

    print(f"{joueur1} jouera avec les {signe1} et {joueur2} jouera avec les {signe2}")
    sleep(3)
    effacer_console()

    # Alternance des joueurs / Commence avec le joueur 1 sachant que l'assignation a été faite aléatoirement
    joueur_actuel = joueur1
    signe_actuel =  signe1  

# ──────────────────────────────────────────────────────────────
#                BOUCLE PRINCIPALE DU JEU
# ──────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────
#                MODE JOUEUR CONTRE JOUEUR
# ──────────────────────────────────────────────────────────────
    if mode_jeu == 0 :
        while not victoire and not plein:
            plateau(grille)  # Affiche la grille
            print(f"{joueur_actuel} ({signe_actuel}), c'est à vous de jouer !")  # Affiche le joueur actuel
            colonne = int(inputCustom(f"{joueur_actuel} ({signe_actuel}), choisissez une colonne entre 1 et 7 : ",int,"La valeur doit être un entier",1, 7)) - 1  # Demande au joueur de choisir une colonne

            # Vérifie si la case est prise
            while colonne_pleine(grille, colonne):
                nombrelignehorizontale(1, 55)
                print("La colonne est pleine. Veuillez en choisir une autre.")
                colonne = int(inputCustom(f"{joueur_actuel} ({signe_actuel}), choisissez une colonne entre 1 et 7 : ",int,"La valeur doit être un entier",1, 7)) - 1

            # Joue le coup
            occurencejouer(grille, signe_actuel, colonne)

            # Vérifie la victoire ou si la grille est pleine
            victoire = verif_victoire(grille, signe_actuel)
            plein = verif_plein(grille)

            # Affiche le résultat si le jeu est terminé
            if victoire:
                plateau(grille)
                print(f"Félicitations {joueur_actuel} ({signe_actuel}) ! Vous avez gagné ! 🎉")
                enregistrer_score_binaire("puissance4", joueur_actuel, 1)

            elif plein:
                plateau(grille)
                print("Match nul ! La grille est pleine.")

            # Change de joueur
            if joueur_actuel == joueur1:
                joueur_actuel, signe_actuel = joueur2, signe2
            else:
                joueur_actuel, signe_actuel = joueur1, signe1


# ──────────────────────────────────────────────────────────────
#                MODE JOUEUR CONTRE IA
# ──────────────────────────────────────────────────────────────

    elif mode_jeu == 1 :
        while not victoire and not plein:
            plateau(grille)

            if joueur_actuel == "IA1":
                print(f"{joueur_actuel} ({signe_actuel}), c'est à vous de jouer !")  # Affiche le joueur actuel
                colonne = bot_puissance4(grille, joueur_actuel, difficulte)
            else:
                print(f"{joueur_actuel} ({signe_actuel}), c'est à vous de jouer !")  # Affiche le joueur actuel
                colonne = int(inputCustom(f"{joueur_actuel} ({signe_actuel}), choisissez une colonne entre 1 et 7 : ",int,"La valeur doit être un entier",1, 7)) - 1

            # Vérifie si la case est prise
            while colonne_pleine(grille, colonne):
                nombrelignehorizontale(1, 55)
                print("La colonne est pleine. Veuillez en choisir une autre.")
                if joueur_actuel == "IA1":
                    colonne = bot_puissance4(grille, joueur_actuel, difficulte)
                else:
                    colonne = int(inputCustom(f"{joueur_actuel} ({signe_actuel}), choisissez une colonne entre 1 et 7 : ",int,"La valeur doit être un entier",1, 7)) - 1

            # Joue le coup
            occurencejouer(grille, signe_actuel, colonne)

            # Vérifie la victoire ou si la grille est pleine
            victoire = verif_victoire(grille, signe_actuel)
            plein = verif_plein(grille)

            # Affiche le résultat si le jeu est terminé
            if victoire and joueur_actuel != "IA1":
                plateau(grille)
                print(f"Félicitations {joueur_actuel} ({signe_actuel}) ! Vous avez gagné ! 🎉")
                enregistrer_score_binaire("puissance4", joueur_actuel, 1)

            elif victoire and joueur_actuel == "IA1":
                plateau(grille)
                print(f"Bien joué {joueur_actuel} ({signe_actuel}) ! Vous avez gagné ! 🎉")
                print("Pas de score pour l'IA")

            elif plein:
                plateau(grille)
                print("Match nul ! La grille est pleine.")

            # Change de joueur
            if joueur_actuel == joueur1:
                joueur_actuel, signe_actuel = joueur2, signe2
            else:
                joueur_actuel, signe_actuel = joueur1, signe1

            
# ──────────────────────────────────────────────────────────────
#                MODE IA CONTRE IA
# ──────────────────────────────────────────────────────────────
    elif mode_jeu == 2 :
        while not victoire and not plein:
            sleep(1)
            plateau(grille)

            print(f"{joueur_actuel} ({signe_actuel}), c'est à vous de jouer !")  # Affiche le joueur actuel
            colonne = bot_puissance4(grille, joueur_actuel, difficulte)

            # Vérifie si la case est prise
            while colonne_pleine(grille, colonne):
                print("La colonne est pleine. Veuillez en choisir une autre.")
                colonne = bot_puissance4(grille, joueur_actuel, difficulte)

            # Joue le coup
            occurencejouer(grille, signe_actuel, colonne)

            # Vérifie la victoire ou si la grille est pleine
            victoire = verif_victoire(grille, signe_actuel)
            plein = verif_plein(grille)

            # Affiche le résultat si le jeu est terminé
            if victoire:
                plateau(grille)
                print(f"Félicitations {joueur_actuel} ({signe_actuel}) ! Vous avez gagné ! 🎉")
                print("Pas de score pour l'IA")

            elif plein:
                plateau(grille)
                print("Match nul ! La grille est pleine.")

            # Change de joueur
            if joueur_actuel == joueur1:
                joueur_actuel, signe_actuel = joueur2, signe2
            else:
                joueur_actuel, signe_actuel = joueur1, signe1

# ──────────────────────────────────────────────────────────────
#                AFFICHAGE FINAL
# ──────────────────────────────────────────────────────────────
    afficher_scores_final("puissance4")
    quitterjeux("puissance4")