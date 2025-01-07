from fonction import *
from random import choice
from random import randint

############################################################################################################
# ──────────────────────────────────────────────────────────────
#                BOTS DEVINETTE
# ──────────────────────────────────────────────────────────────
############################################################################################################

def bot_choix_intervalle(difficulte : int) -> int :

    """
    Fonction pour faire choisir un intervalle par le bot.
    Args:
        difficulte (int): Le mode de jeu.
    Returns:
        int: L'intervalle de jeu.
    """
    intervalle : int
    intervalle = 0

    #Mode hasard
    if difficulte == 1 :
        intervalle = randint(1, 100)

    #Mode entre-deux
    if difficulte == 2 :
        intervalle = randint(1, 1000)

    #Mode dichotomie/complexe
    if difficulte == 3 :
        intervalle = randint(1, 10000)

    return intervalle

def bot_choix_nombremystere(intervalle : int) -> int :
    """
    Fonction pour faire choisir un nombre mystère par le bot.
    Args:
        intervalle (int): L'intervalle de jeu.
    Returns:
        int: Le nombre mystère.
    """
    nombremystere : int
    nombremystere = randint(1, intervalle)

    return nombremystere

def bot_devinnette(difficulte: int, intervalle: int, retour_jeu: int, nbr_prec: int, borne_min: int, borne_max: int) -> int:
    """
    Fonction pour le bot pour la devinette.
    Args:
        difficulte (int): La difficulté du bot.
        intervalle (int): L'intervalle initial de jeu.
        retour_jeu (int): Le retour du jeu (0 : plus grand, 1 : plus petit).
        nbr_prec (int): Le dernier nombre proposé par le bot.
        borne_min (int): La borne minimale de l'intervalle.
        borne_max (int): La borne maximale de l'intervalle.
    Returns:
        int: Le nombre donné par le bot.
    """
    from random import randint

    valeur_renvoye: int

    # Mode hasard
    if difficulte == 1:
        valeur_renvoye = randint(1, intervalle)
        print(f"Le nombre donné par l'IA est {valeur_renvoye}")
        return valeur_renvoye

    # Mode entre-deux
    elif difficulte == 2:
        if retour_jeu == 2:  # Si le joueur a répond que le nombre est plus petit
            borne_max = min(borne_max, nbr_prec - 1)
        elif retour_jeu == 1: # Si le joueur a répond que le nombre est plus grand
            borne_min = max(borne_min, nbr_prec + 1)

        valeur_renvoye = randint(borne_min, borne_max)
        print(f"Le nombre donné par l'IA est {valeur_renvoye} (intervalle: [{borne_min}, {borne_max}])")
        return valeur_renvoye

    # Mode difficulté maximale
    else:
        if retour_jeu == 2:  # Plus petit
            borne_max = min(borne_max, nbr_prec - 1)
        elif retour_jeu == 1:  # Plus grand
            borne_min = max(borne_min, nbr_prec + 1)

        # Stratégie : Choisir un nombre biaisé dans la partie la plus "prometteuse"
        inter = borne_max - borne_min + 1
        if inter <= 4:
            # Quand l'intervalle est petit, joue au hasard dans l'intervalle
            valeur_renvoye = randint(borne_min, borne_max)
        else:
            # Priorisation biaisée : choisir un tiers supérieur de l'intervalle
            tiers = inter // 3
            if retour_jeu == 0:  # Si plus grand, privilégier la borne supérieure
                valeur_renvoye = randint(borne_min + tiers * 2, borne_max)
            else:  # Si plus petit, privilégier la borne inférieure
                valeur_renvoye = randint(borne_min, borne_max - tiers)

        print(f"Le nombre donné par l'IA est {valeur_renvoye} (intervalle: [{borne_min}, {borne_max}])")
        return valeur_renvoye
        
def bot_reponse_intervalle_devinette(nbr_devine : int, nbr_reponse : int) -> int:
    """
    Fonction pour la réponse du bot pour la devinette.
    Args:
        nbr_devine (int): Le nombre deviné.
        nbr_reponse (int): Le nombre mystère.
    Returns:
        int: La réponse du bot.
    """
    if nbr_devine < nbr_reponse :
        return 0
    elif nbr_devine > nbr_reponse :
        return 1
    else :
        return 2
    
############################################################################################################    
# ──────────────────────────────────────────────────────────────
#                BOT ALLUMETTES
# ──────────────────────────────────────────────────────────────
############################################################################################################

def bot_allumette(difficulte : int, nbr_allumette_restante : int) -> int :
    """
    Fonction pour le bot pour le jeu des allumettes.
    Args:
        difficulte (int): La difficulté du bot.
        nbr_allumette_restante (int): Le nombre d'allumettes restantes.
    Returns:
        int: Le nombre d'allumettes à retirer.
    """
    nbr_allumettes_prise = 0

    # Difficulté hasard (facile)
    if difficulte == 1:
        nbr_allumettes_prise = randint(1, 3)
        print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
        return nbr_allumettes_prise
    
    # Difficulté entre-deux (intermédiaire)
    elif difficulte == 2:
        # Le bot prend parfois des décisions optimales, mais parfois il joue de manière aléatoire.
        if randint(1, 10) <= 6:  # 60% de chance de jouer de manière optimale
            # Stratégie partiellement optimale : amener l'adversaire dans une position perdante
            nbr_allumettes_prise = (nbr_allumette_restante - 1) % 4
            if nbr_allumettes_prise == 0:
                # Si le bot ne peut pas appliquer la stratégie optimale, il joue au hasard
                nbr_allumettes_prise = randint(1, 3)
        else:
            # 40% de chance de jouer au hasard (pour ajouter un peu de variabilité)
            nbr_allumettes_prise = randint(1, 3)
        
        print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
        return nbr_allumettes_prise

    # Difficulté maximum (imbattable)
    else:
        # Stratégie optimale (imbattable) : Toujours amener l'adversaire dans une position perdante.
        if nbr_allumette_restante % 4 == 1:
            # Si on est déjà dans une position perdante, on joue au hasard
            nbr_allumettes_prise = randint(1, 3) if nbr_allumette_restante > 3 else nbr_allumette_restante
        else:
            # Calculer le nombre d'allumettes à prendre pour laisser un multiple de 4 + 1
            nbr_allumettes_prise = (nbr_allumette_restante - 1) % 4
            if nbr_allumettes_prise == 0:
                nbr_allumettes_prise = randint(1, 3)  # Si ce n'est pas possible, choisir au hasard

        print(f"L'IA a pris {nbr_allumettes_prise} allumettes")
        return nbr_allumettes_prise

############################################################################################################
# ──────────────────────────────────────────────────────────────
#                BOT MORPION
# ──────────────────────────────────────────────────────────────
############################################################################################################

def bot_morpion(difficulte : int, grille : list[list[str]], jeu : int) -> list[list[str]] :
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
    
    if difficulte == 1 :
        if jeu == 1 :
            coord[0] = randint(0, 2)
            coord[1] = randint(0, 2)
            while deja_pris(grille, coord[0], coord[1]) :
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
            grille[coord[0]][coord[1]] = "O"
            print("Le bot a joué en ", coord[0], coord[1])
            return grille
        else :
            coord[0] = randint(0, 2)
            coord[1] = randint(0, 2)
            while deja_pris(grille, coord[0], coord[1]) :
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
            grille[coord[0]][coord[1]] = "X"
            print("Le bot a joué en ", coord[0], coord[1])
            return grille
        
    elif difficulte == 2 :
        n = randint(0, 8)
        if n < 2 :
            if jeu == 1 :
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
                while deja_pris(grille, coord[0], coord[1]) :
                    coord[0] = randint(0, 2)
                    coord[1] = randint(0, 2)
                grille[coord[0]][coord[1]] = "O"
                print("Le bot a joué en ", coord[0], coord[1])
                return grille
            else :
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
                while deja_pris(grille, coord[0], coord[1]) :
                    coord[0] = randint(0, 2)
                    coord[1] = randint(0, 2)
                grille[coord[0]][coord[1]] = "X"
                print("Le bot a joué en ", coord[0], coord[1])
                return grille
        else :
            if jeu == 1 :
                #Regarde si le bot peut gagner au prochain tour
                for i in range(0, len(grille)):
                    for j in range(0, len(grille)):
                        if grille[i][j] == " ":
                            grille[i][j] = "O"
                            if check_victory(grille, "O"):
                                grille[i][j] = "O"
                                print("Le bot a joué en ", i,j)
                                return grille
                            grille[i][j] = " "

                #Regarde si l'adversaire peut gagner au prochain tour et l'en empeche
                for i in range(0, len(grille)):
                    for j in range(0, len(grille)):
                        if grille[i][j] == " ":
                            grille[i][j] = "X"
                            if check_victory(grille, "X"):
                                grille[i][j] = "O"
                                print("Le bot a joué en ", i,j)
                                return grille
                            grille[i][j] = " "

                #Si rien de tout cela n'est possible, le bot joue sur la premiere case vide
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
                while deja_pris(grille, coord[0], coord[1]) :
                    coord[0] = randint(0, 2)
                    coord[1] = randint(0, 2)
                grille[coord[0]][coord[1]] = "O"
                return grille
            else :
                #Regarde si le bot peut gagner au prochain tour
                for i in range(0, len(grille)):
                    for j in range(0, len(grille)):
                        if grille[i][j] == " ":
                            grille[i][j] = "X"
                            if check_victory(grille, "X"):
                                grille[i][j] = "X"
                                print("Le bot a joué en ", i,j)
                                return grille
                            grille[i][j] = " "

                #Regarde si l'adversaire peut gagner au prochain tour et l'en empeche
                for i in range(0, len(grille)):
                    for j in range(0, len(grille)):
                        if grille[i][j] == " ":
                            grille[i][j] = "O"
                            if check_victory(grille, "O"):
                                grille[i][j] = "X"
                                print("Le bot a joué en ", i,j)
                                return grille
                            grille[i][j] = " "

                #Si rien de tout cela n'est possible, le bot joue sur la premiere case vide
                while deja_pris(grille, coord[0], coord[1]) :
                    coord[0] = randint(0, 2)
                    coord[1] = randint(0, 2)
                grille[coord[0]][coord[1]] = "X"
                return grille
    else:
        if jeu == 1 :
            #Regarde si le bot peut gagner au prochain tour
            for i in range(0, len(grille)):
                for j in range(0, len(grille)):
                    if grille[i][j] == " ":
                        grille[i][j] = "O"
                        if check_victory(grille, "O"):
                            grille[i][j] = "O"
                            print("Le bot a joué en ", i,j)
                            return grille
                        grille[i][j] = " "

            #Regarde si l'adversaire peut gagner au prochain tour et l'en empeche
            for i in range(0, len(grille)):
                for j in range(0, len(grille)):
                    if grille[i][j] == " ":
                        grille[i][j] = "X"
                        if check_victory(grille, "X"):
                            grille[i][j] = "O"
                            print("Le bot a joué en ", i,j)
                            return grille
                        grille[i][j] = " "

            #Si rien de tout cela n'est possible, le bot joue sur la premiere case vide
            coord[0] = randint(0, 2)
            coord[1] = randint(0, 2)
            while deja_pris(grille, coord[0], coord[1]) :
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
            grille[coord[0]][coord[1]] = "O"
            return grille
        
        else :
            #Regarde si le bot peut gagner au prochain tour
            for i in range(0, len(grille)):
                for j in range(0, len(grille)):
                    if grille[i][j] == " ":
                        grille[i][j] = "X"
                        if check_victory(grille, "X"):
                            grille[i][j] = "X"
                            print("Le bot a joué en ", i,j)
                            return grille
                        grille[i][j] = " "

            #Regarde si l'adversaire peut gagner au prochain tour et l'en empeche
            for i in range(0, len(grille)):
                for j in range(0, len(grille)):
                    if grille[i][j] == " ":
                        grille[i][j] = "O"
                        if check_victory(grille, "O"):
                            grille[i][j] = "X"
                            print("Le bot a joué en ", i,j)
                            return grille
                        grille[i][j] = " "

            #Si rien de tout ça est possible, le bot joue sur une case aléatoire
            coord[0] = randint(0, 2)
            coord[1] = randint(0, 2)
            while deja_pris(grille, coord[0], coord[1]) :
                coord[0] = randint(0, 2)
                coord[1] = randint(0, 2)
            grille[coord[0]][coord[1]] = "X"
            print(coord[0], coord[1])
            return grille  
               
############################################################################################################

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

############################################################################################################

def deja_pris(mat : list[list[str]], l : int, c : int) -> bool :
    """
    Fonction pour vérifier si une case est déjà prise
    
    Args:
        mat (list[list[str]]): La matrice du morpion.
        l (int) : La ligne
        c (int) : La colonne
    Returns:
        bool : True si la case est déjà prise, False sinon
    """

    cond : bool
    cond = False
    if mat[l][c] == "X" or mat[l][c] == "O" :
        cond = True
    return cond

############################################################################################################
# ──────────────────────────────────────────────────────────────
#                BOT PUISSANCE 4
# ──────────────────────────────────────────────────────────────
############################################################################################################

def colonnes_possibles(grille: list[list[str]]) -> list[int]:
    """
    Retourne les colonnes où il est possible de jouer.
    Args:
        grille (list[list[str]]): Grille de jeu.
    Returns:
        list[int] : Liste des colonnes où il est possible de jouer.
    """
    colonnes : list[int] 
    colonnes = []
    for colonne in range(7):
        if not colonne_pleine(grille, colonne):
            colonnes.append(colonne)
    return colonnes

############################################################

def bot_puissance4(grille: list[list[str]], signe_actuel : str, difficulte: int) -> int:
    """
    Fonction qui permet à l'IA de choisir une colonne pour jouer.
    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Joueur actuel.
        difficulte (int): Difficulté de l'IA.
    Returns:
        int : Colonne choisie par l'IA.
    """
    def colonne_valide(grille: list[list[str]], colonne: int) -> bool:
        """Vérifie si une colonne n'est pas pleine."""
        return grille[0][colonne] == " "

    if signe_actuel == "\033[33m■\033[0m" :
        adversaire = "\033[31m■\033[0m"
    else:
        adversaire = "\033[33m■\033[0m"

    # Mode aléatoire
    if difficulte == 1:
        colonnes_disponibles = [col for col in range(7) if colonne_valide(grille, col)]
        if colonnes_disponibles:
            colonne = choice(colonnes_disponibles)
            print(f"L'IA ({signe_actuel}) choisit la colonne {colonne+1}")
            return colonne
        print("Toutes les colonnes sont pleines !")
        return -1


    # Difficulté 1 : IA défensive/offensive simple
    if difficulte == 2:

        # Vérifier si l'IA peut gagner avec verif_victoire_potentielle
        for colonne in range(7):
            if verif_victoire_potentielle(grille, signe_actuel, colonne):
                print(f"L'IA ({signe_actuel}) joue ici pour gagner la colonne {colonne+1}")
                return colonne
            
        # Vérifier si le joueur peut gagner avec verif_victoire_potentielle
        for colonne in range(7):
            if verif_victoire_potentielle(grille, adversaire, colonne):
                print(f"L'IA ({signe_actuel}) bloque la colonne {colonne+1}")
                return colonne
        
        # Sinon, choisir une colonne aléatoire parmi les valides
        colonnes_disponibles = [col for col in range(7) if colonne_valide(grille, col)]
        if colonnes_disponibles:
            colonne = choice(colonnes_disponibles)
            print(f"L'IA ({signe_actuel}) choisit aléaoirement la colonne {colonne+1}")
            return colonne
        
        # Si aucune colonne n'est valide
        print("Toutes les colonnes sont pleines !")
        return -1
    
    # Difficulté 3 : IA imbattable
    return -1


############################################################

def simulationcoups(grille: list[list[str]], joueur: str, colonne: int) -> list[list[str]]:
    """
    Simule un coup pour l'IA.
    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Joueur actuel.
        colonne (int): Colonne choisie par l'IA.
    Returns:
        list[list[str]] : Grille de jeu après le coup simulé.
    """
    grille_copie = [ligne.copy() for ligne in grille]  # Copie de la grille
    case_placee = False  # Variable pour savoir si un jeton a été placé

    for i in range(5, -1, -1):  # Parcourt les lignes de la colonne choisie
        if grille_copie[i][colonne] == " " and not case_placee:  # Si la case est vide et qu'un jeton n'a pas encore été placé
            grille_copie[i][colonne] = joueur  # Place le jeton du joueur
            case_placee = True  # On marque qu'un jeton a été placé

    return grille_copie

############################################################

def verif_victoire(grille: list[list[str]], signe_actuel : str) -> bool:
    """
    Vérifie si un joueur a gagné en ayant un alignement de 4 jetons.

    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Jeton du joueur ("X" ou "O").
    """
    # Vérification horizontale
    for i in range(6):  # 6 lignes
        for j in range(4):  # Jusqu'à la 4e colonne
            if (
                grille[i][j] == grille[i][j + 1] == grille[i][j + 2] == grille[i][j + 3] == signe_actuel
            ):
                return True

    # Vérification verticale
    for i in range(3):  # Jusqu'à la 3e ligne
        for j in range(7):  # 7 colonnes
            if (
                grille[i][j] == grille[i + 1][j] == grille[i + 2][j] == grille[i + 3][j] == signe_actuel
            ):
                return True

    # Vérification diagonale montante (\)
    for i in range(3):  # Jusqu'à la 3e ligne
        for j in range(4):  # Jusqu'à la 4e colonne
            if (
                grille[i][j] == grille[i + 1][j + 1] == grille[i + 2][j + 2] == grille[i + 3][j + 3] == signe_actuel
            ):
                return True

    # Vérification diagonale descendante (/)
    for i in range(3, 6):  # À partir de la 3e ligne
        for j in range(4):  # Jusqu'à la 4e colonne
            if (
                grille[i][j] == grille[i - 1][j + 1] == grille[i - 2][j + 2] == grille[i - 3][j + 3] == signe_actuel
            ):
                return True

    return False


def verif_victoire_potentielle(grille: list[list[str]], signe_actuel : str, colonne: int) -> bool:
    """
    Vérifie si un joueur peut gagner en jouant dans une colonne donnée.
    Args:
        grille (list[list[str]]): Grille de jeu.
        joueur (str): Jeton du joueur ("X" ou "O").
        colonne (int): Colonne dans laquelle le joueur joue hypothétiquement.
    Returns:
        bool: True si jouer dans cette colonne mène à une victoire, sinon False.
    """
    if not (0 <= colonne < 7):  # Vérifie que la colonne est valide
        return False

    # Trouver la première ligne vide dans cette colonne
    for ligne in range(5, -1, -1):  # Parcourt les lignes de bas en haut
        if grille[ligne][colonne] == " ":  # Si la case est vide
            # Simuler le coup
            grille[ligne][colonne] = signe_actuel
            victoire = verif_victoire(grille, signe_actuel)  # Vérifie la victoire
            # Annuler le coup
            grille[ligne][colonne] = " "
            return victoire

    return False  # Si la colonne est pleine

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
    
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################