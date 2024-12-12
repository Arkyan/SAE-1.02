from fonction import *
from time import sleep
from random import randint

def afficher_jeu() -> None : 
    """
    Fonction pour afficher la partie
    Args:
        None : None
    Returns:
        None : None
    """
    nombrelignehorizontale(1, 55)
    print("\033[92m Vous êtes dans une partie de morpion \033[0m")
    nombrelignehorizontale(1, 55)

def taille_morpion() -> list[list[str]] :
    """
    Fonction pour choisir la taille du morpion
    Args:
        None : None
    Returns:
        list[list[str]]: La matrice du morpion.
    """

    mat : list[list[str]]
    i : int
    j: int
    val : str
    n : int
    mat = list([])
    n = int(inputCustom("De quelle taille doit être votre morpion sachant qu'il sera de dimension n*n : ", int, "La valeur doit être un entier", 3, 10))
    for i in range(0, n) :
        i = i
        ligne : list[str]
        ligne = list()
        for j in range(0, n) :
            j = j
            val = " "
            ligne.append(val)
        mat.append(ligne)

    nombrelignehorizontale(1, 55)
    print("Voici le morpion sur lequel vous allez jouer.")
    return mat

############################################################################################################
############################################################################################################
############################################################################################################

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

############################################################################################################
############################################################################################################
############################################################################################################

def jeu_morpion1(mat : list[list[str]], joueur : str) -> list[list[str]] :
    """
    Fonction pour jouer au jeu du morpion
    Args:
        mat (list[list[str]]): La matrice du morpion.
        joueur (str): Le nom du joueur.
    Returns:
        list[list[str]]: La matrice du morpion.
    """
    
    morpion_ligne_x : int
    morpion_colonne_x : int
    print(f"\033[0;36m{joueur}\033[0m, sélectionner la case dans laquelle vous jouez (X) : ")
    morpion_ligne_x = int(inputCustom("Choisir ligne : ", int, "La valeur doit être un entier", 1, len(mat)))
    while morpion_ligne_x > len(mat) :
        morpion_ligne_x = int(inputCustom("Sélectionner la ligne dans l'intervalle de l'aire de jeu : ", int, "La valeur doit être un entier", 1, len(mat)))
    morpion_colonne_x = int(inputCustom("Choisir colonne : ", int, "La valeur doit être un entier", 1, len(mat)))
    while morpion_colonne_x > len(mat) :
        morpion_colonne_x = int(inputCustom("Sélectionner la colonne dans l'intervalle de l'aire de jeu : ", int, "La valeur doit être un entier", 1, len(mat)))
    morpion_colonne_x -= 1
    morpion_ligne_x -= 1
    if not(deja_pris(mat, morpion_ligne_x, morpion_colonne_x)) :
        mat[morpion_ligne_x][morpion_colonne_x] = "X"
    else:
        print()
        print("Case déjà prise, sélectionnez en une autre")
        jeu_morpion1(mat, joueur)
    print()
    nombrelignehorizontale(1, 55)
    print()
    return mat

############################################################################################################
############################################################################################################
############################################################################################################

def jeu_morpion2(mat : list[list[str]], joueur : str) -> list[list[str]] :
    """
    Fonction pour jouer au jeu du morpion
    Args:
        mat (list[list[str]]): La matrice du morpion.
        joueur (str): Le nom du joueur.
    Returns:
        list[list[str]]: La matrice du morpion.
    """
    
    morpion_ligne_o : int
    morpion_colonne_o : int
    print(f"\033[0;36m{joueur}\033[0m, sélectionner la case dans laquelle vous jouez (O) :")
    morpion_ligne_o = int(inputCustom("Choisir ligne : ", int, "La valeur doit être un entier", 1, len(mat)))
    while morpion_ligne_o > len(mat) :
        morpion_ligne_o = int(inputCustom("Sélectionner la ligne dans l'intervalle de l'aire de jeu : ", int, "La valeur doit être un entier", 1, len(mat)))
    morpion_colonne_o = int(inputCustom("Choisir colonne : ", int, "La valeur doit être un entier", 1, len(mat)))
    while morpion_colonne_o > len(mat) :
        morpion_colonne_o = int(inputCustom("Sélectionner la colonne dans l'intervalle de l'aire de jeu : ", int, "La valeur doit être un entier", 1, len(mat)))
    morpion_colonne_o -= 1
    morpion_ligne_o -= 1
    if not(deja_pris(mat, morpion_ligne_o, morpion_colonne_o)) :
        mat[morpion_ligne_o][morpion_colonne_o] = "O"
    else:
        print()
        print("Case déjà prise, sélectionnez en une autre")
        jeu_morpion2(mat, joueur)
    print()
    nombrelignehorizontale(1, 55)
    print()
    return mat
    
############################################################################################################
############################################################################################################
############################################################################################################

def afficher_morpion(mat: list[list[str]]) -> list[list[str]]:
    """
    Fonction pour afficher le morpion avec numérotation des lignes et colonnes (à partir de 1).
    
    Args:
        mat (list[list[str]]): La matrice du morpion.
    
    Returns:
        list[list[str]]: La matrice du morpion.
    """

    GREEN = "\033[92m"  # Code ANSI pour la couleur verte
    RESET = "\033[0m"   # Réinitialisation des couleurs
    BLUE = "\033[94m"   # Code ANSI pour la couleur bleue
    RED = "\033[91m"    # Code ANSI pour la couleur rouge

    # Afficher les indices des colonnes (1 à len(mat))
    print("   ", end="")
    for col in range(1, len(mat) + 1):
        print(f" {GREEN}{col}{RESET} ", end="")
        if col < len(mat):
            print(" ", end="")
    print("\n", end="   " + "--- " * len(mat) + "\n")
    
    # Afficher la matrice avec les indices des lignes (1 à len(mat))
    for j in range(len(mat)):
        print(f" {GREEN}{j + 1}{RESET} ", end="")  # Indice de ligne
        for k in range(len(mat)):
            if mat[j][k] == "X":
                print(f" {RED}{mat[j][k]}{RESET} ", end="")
            elif mat[j][k] == "O":
                print(f" {BLUE}{mat[j][k]}{RESET} ", end="")
            else:
                print(f" {mat[j][k]} ", end="")
            if k < len(mat) - 1:
                print("|", end="")
        if j < len(mat) - 1:
            print("\n", end="   " + "---|" * (len(mat) - 1) + "---\n")
    print()
    print()
    return mat

############################################################################################################
############################################################################################################
############################################################################################################

def morpion_plein(mat : list[list[str]]) -> bool:
    """
    Fonction pour vérifier si le morpion est plein ou non

    Args:
        mat (list[list[str]]): La matrice du morpion.    

    Returns:
        bool : True si le morpion est plein, False sinon
    """

    est_plein : bool
    est_plein = True
    for i in range(len(mat)) :
        for j in range(len(mat)) :
            if mat[i][j] == " " :
                est_plein = False
    return est_plein

############################################################################################################
############################################################################################################
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
############################################################################################################
############################################################################################################
    
def morpion() -> None :
    cond_vic1 : bool
    cond_vic2 : bool
    cond_vic1 = False
    cond_vic2 = False
    compteur : int
    compt_j : int
    n_ligne_col : int
    n_ligne_col = 0
    compteur = 0
    compt_j = 1
    j : int
    listej : list[str]
    listej = []

    #Proposition réinitialisation des scores
    reinitialiser_scores_binaire("morpion")

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

    #Effacement de la console avec un sleep pour laisser le temps de lire
    sleep(3)
    effacer_console()
    nombrelignehorizontale(1, 55)
    print("\033[92m Lancement du jeu du morpion \033[0m")
    nombrelignehorizontale(1, 55)

    #Affichage des joueurs
    print()
    print(f"{joueur1} vous jouerez : X ")
    print(f"{joueur2} vous jouerez : O ")
    print()

    #Choix de la taille du morpion
    mat = taille_morpion()
    afficher_morpion(mat)
    nombrelignehorizontale(1, 55)


# ──────────────────────────────────────────────────────────────
#                DÉROULEMENT DU JEU
# ──────────────────────────────────────────────────────────────

    #MODE JOUEUR CONTRE JOUEUR
    if mode_jeu == 0 :
        while ((cond_vic1 == False) and (cond_vic2 == False) and (not(morpion_plein(mat)))) : 
            #le joueur 1 joue
            if compt_j == 1 :

                jeu_morpion1(mat, joueur1)
                effacer_console()
                afficher_jeu()
                afficher_morpion(mat)


                #Vérifie si une colonne est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[i][n_ligne_col] == 'X' :
                            #Incrémente le compteur servant à vérifier si la colonne est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic1 = True
                    #Incrémente le numéro de la colonne
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine colonne
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification
                n_ligne_col = 0


                #Vérifie si une ligne est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[n_ligne_col][i] == 'X' :
                            #Incrémente le compteur servant à vérifier si la ligne est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic1 = True
                    #Incrémente le numéro de la ligne
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine ligne
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification
                n_ligne_col = 0


                #Vérifie si la diagonale principale est remplie 
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[i][i] == 'X':
                            #Incrémente le compteur servant à vérifier si la diagonale principale est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic1 = True
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine diagonale principale
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification
                n_ligne_col = 0


                #Vérifie si la diagonale opposée est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[i][-i-1] == 'X' :
                            #Incrémente le compteur servant à vérifier si la diagonale opposée est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic1 = True
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine diagonale opposée
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification(qui sera pour le joueur 2)
                n_ligne_col = 0


                #Changement de joueur
                compt_j = 2

            else :
                #le joueur 2 joue
                jeu_morpion2(mat, joueur2)
                effacer_console()
                afficher_jeu()
                afficher_morpion(mat)


                #Vérifie si une colonne est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[i][n_ligne_col] == 'O' :
                            #Incrémente le compteur servant à vérifier si la colonne est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic2 = True
                    #Incrémente le numéro de la colonne
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine colonne
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification
                n_ligne_col = 0


                #Vérifie si une ligne est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[n_ligne_col][i] == 'O' :
                            #Incrémente le compteur servant à vérifier si la ligne est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic2 = True
                    #Incrémente le numéro de la ligne
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine ligne
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification
                n_ligne_col = 0


                #Vérifie si la diagonale principale est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[i][i] == 'O' :
                            #Incrémente le compteur servant à vérifier si la diagonale principale est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic2 = True
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine diagonale principale
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification
                n_ligne_col = 0


                #Vérifie si la diagonale opposée est remplie
                while n_ligne_col < len(mat) :
                    for i in range(len(mat)) :
                        if mat[i][-i-1] == 'O' :
                            #Incrémente le compteur servant à vérifier si la diagonale opposée est remplie complètement
                            compteur = compteur + 1
                            if compteur == len(mat) :
                                cond_vic2 = True
                    n_ligne_col = n_ligne_col + 1
                    #Réinitialise le compteur pour la prochaine diagonale opposée
                    compteur = 0
                #Réinitialise la variable pour la prochaine vérification(qui sera pour le joueur 1)
                n_ligne_col = 0

                #Changement de joueur
                compt_j = 1
            
            
        #Test des valeurs booléennes pour un possible gagnant
        if cond_vic1 :
            print(f"{joueur1} a gagné")
            enregistrer_score_binaire("morpion", joueur1, 1)

        elif cond_vic2 :
            print(f"{joueur2} a gagné")
            enregistrer_score_binaire("morpion", joueur2, 1)

        #Si le morpion est plein et qu'il n'y a pas de gagnant
        else :
            print("Match nul")

    #MODE JOUEUR CONTRE IA
    elif mode_jeu == 1 :
        abababa

    #MODE IA CONTRE IA
    elif mode_jeu == 2 :
        abababa


    #Affichage de fin
    afficher_scores_final("morpion")
    quitterjeux("morpion")