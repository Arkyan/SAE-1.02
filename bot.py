from random import randint
from morpion import *
from puissance4Bonus import *
from allumette import *
from devinette import *



##################################################################################################################
##################################################################################################################
##################################          DIFFICULTE          ##################################################
##################################            BOT               ##################################################
##################################          DEVINETTE           ##################################################
##################################################################################################################
##################################################################################################################
def bot_devinnette(difficulte : int, intervalle : int, retour_jeu : int, nbr_prec : int) -> int:
    """
    Fonction pour le bot pour la devinette.
    Args:
        intervalle (int): L'intervalle de jeu.
    Returns:
        int: Le nombre mystère.
    """
    back_game : int
    if difficulte == 0 :
        back_game = randint(1, intervalle)
        return back_game

    elif difficulte == 1 :
        if retour_jeu == -1 :
            back_game = randint(1, intervalle)
            return back_game
        elif retour_jeu == 0 :
            back_game = randint(nbr_prec, intervalle)
            return back_game
        else :
            back_game = randint(1, nbr_prec)
            return back_game
    else :
        if retour_jeu == -1 :
            back_game = intervalle // 2
            return back_game
        elif retour_jeu == 0 :
            back_game = (nbr_prec // 2) + nbr_prec
            return back_game
        else :
            back_game = nbr_prec // 2
            return back_game
        
def bot_reponse_intervalle_devinette(nbr_devine : int, nbr_reponse : int) -> int:
    """
    Fonction pour la réponse du bot en mode 'HASARD' pour la devinette.
    Args:
        nbr_devine (int): Le nombre deviné par le joueur.
    Returns:
        int: La réponse du bot.
    """
    if nbr_devine < nbr_reponse :
        return 0
    elif nbr_devine > nbr_reponse :
        return 1
    else :
        return 2
    
    
##################################################################################################################
##################################################################################################################
##################################          DIFFICULTE          ##################################################
##################################            BOT               ##################################################
##################################          ALLUMETTE           ##################################################
##################################################################################################################
##################################################################################################################
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
        return randint(1, 3)
    elif difficulte == 1 :
        n : int
        n = randint(1, 7)
        if n < 4 :
            return randint(1, 3)
        else :
            for i in range(1, 5) :
                if nbr_allumette_restante - 1 == 4*i :
                    nbr_allumettes_prise = nbr_allumette_restante - 1
                    return nbr_allumettes_prise
                elif nbr_allumette_restante - 2 == 4*i :
                    nbr_allumettes_prise = nbr_allumette_restante - 2
                    return nbr_allumettes_prise
                elif nbr_allumette_restante - 3 == 4*i :
                    nbr_allumettes_prise = nbr_allumette_restante - 3
                    return nbr_allumettes_prise
                else :
                    return randint(1, 3)
    else :
        for i in range(1, 5) :
            if nbr_allumette_restante - 1 == 4*i :
                nbr_allumettes_prise = nbr_allumette_restante - 1
                return nbr_allumettes_prise
            elif nbr_allumette_restante - 2 == 4*i :
                nbr_allumettes_prise = nbr_allumette_restante - 2
                return nbr_allumettes_prise
            elif nbr_allumette_restante - 3 == 4*i :
                nbr_allumettes_prise = nbr_allumette_restante - 3
                return nbr_allumettes_prise
            else :
                return randint(1, 3)
    return nbr_allumettes_prise
    
##################################################################################################################
##################################################################################################################
##################################          DIFFICULTE          ##################################################
##################################            BOT               ##################################################
##################################          MORPION             ##################################################
##################################################################################################################
##################################################################################################################
def bot_morpion(difficulte : int, grille : list[list[str]]) -> list[int] :
    """
    Fonction pour le bot pour le jeu du morpion.
    Args:
        difficulte (int): La difficulté du bot.
        grille (list[list[str]]): La grille de jeu.
    Returns:
        list[int]: Les coordonnées du bot.
    """
    i : int
    j : int
    n : int
    coord : list[int]
    coord = [0, 0]
    if difficulte == 0 :
        while deja_pris(grille, coord[0], coord[1]) :
            coord[0] = randint(0, 2)
            coord[1] = randint(0, 2)
        return coord
    elif difficulte == 1 :
        n = randint(0, 8)
        if n < 4 :
            for i in range(0, 3) :
                for j in range(0, 3) :
                    if grille[i][j] == " " :
                        coord[0] = i
                        coord[1] = j
                        return coord
        else :
            #Regarde si le bot peut gagner au prochain tour
            for i in range(0, len(grille)):
                for j in range(0, len(grille)):
                    if grille[i][j] == " ":
                        grille[i][j] = "O"
                        if check_victory(grille, "O"):
                            coord[0] = i
                            coord[1] = j
                            grille[i][j] = " "
                            return coord
                        grille[i][j] = " "

            #Regarde si l'adversaire peut gagner au prochain tour et l'en empeche
            for i in range(0, len(grille)):
                for j in range(0, len(grille)):
                    if grille[i][j] == " ":
                        grille[i][j] = "X"
                        if check_victory(grille, "X"):
                            coord[0] = i
                            coord[1] = j
                            grille[i][j] = " "
                            return coord
                        grille[i][j] = " "

            #Si rien de tout cela n'est possible, le bot joue sur la premiere case vide
            for i in range(0, 3):
                for j in range(0, 3):
                    if grille[i][j] == " ":
                        coord[0] = i
                        coord[1] = j
                        return coord
    else:
        #Regarde si le bot peut gagner au prochain tour
        for i in range(0, len(grille)):
            for j in range(0, len(grille)):
                if grille[i][j] == " ":
                    grille[i][j] = "O"
                    if check_victory(grille, "O"):
                        coord[0] = i
                        coord[1] = j
                        grille[i][j] = " "
                        return coord
                    grille[i][j] = " "
        
        #Regarde si l'adversaire peut gagner au prochain tour et l'en empeche
        for i in range(0, len(grille)):
            for j in range(0, len(grille)):
                if grille[i][j] == " ":
                    grille[i][j] = "X"
                    if check_victory(grille, "X"):
                        coord[0] = i
                        coord[1] = j
                        grille[i][j] = " "
                        return coord
                    grille[i][j] = " "
        
        #Si rien de tout cela n'est possible, le bot joue sur la premiere case vide
        for i in range(0, 3):
            for j in range(0, 3):
                if grille[i][j] == " ":
                    coord[0] = i
                    coord[1] = j
                    return coord
    return coord

def check_victory(grille : list[list[str]], joueur : str) -> bool:
    """
    Fonction pour vérifier si un joueur a gagné.
    Args:
        grille (list[list[str]]): La grille de jeu.
        joueur (str): Le joueur à vérifier.
    Returns:
        bool: Si le joueur a gagné.
    """
    i : int
    j : int
    #Lignes
    for i in range(0, 3):
        if grille[i][0] == joueur and grille[i][1] == joueur and grille[i][2] == joueur:
            return True
    #Colonnes
    for j in range(0, 3):
        if grille[0][j] == joueur and grille[1][j] == joueur and grille[2][j] == joueur:
            return True
    #Diagonales
    if grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur:
        return True
    if grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur:
        return True
    return False

##################################################################################################################
##################################################################################################################
##################################          DIFFICULTE          ##################################################
##################################            BOT               ##################################################
##################################          PUISSANCE 4         ##################################################
##################################################################################################################
##################################################################################################################