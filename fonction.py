from time import sleep
from typing import List
import pickle

##################################################################################################################
##################################################################################################################
##################################          FONCTION             #################################################
##################################           UTILES              #################################################
##################################################################################################################
##################################################################################################################

def effacer_console() :
    """
    Fonction pour effacer la console.

    Args: 
        None : None.
    Returns: 
        None : None.
    """
    print("\033c", end="")

#########################################################
#########################################################
#########################################################

def nombrelignehorizontale(nombre : int, longueur : int) :
    """
    Fonction pour afficher un nombre de lignes horizontales
    Args:
        nombre (int) : Nombre de lignes
        longueur (int) : Longueur de la ligne
    Returns:
        None : None
    """

    for i in range(nombre) :
        print("┊" + '-' * longueur + "┊")                             
        i += 1

#########################################################
#########################################################
#########################################################

def inputCustom(Texte: str, Type: type, Error: str,  min_val: float = -float('inf'), max_val: float = float('inf')):
    """
    Demande à l'utilisateur une valeur de type Type (int, float, str) et valide cette valeur.

    Args:
        Texte (str): Le message à afficher pour demander la saisie à l'utilisateur.
        Type (type): Le type de la valeur attendue (int, float, str).
        Error (str): Le message d'erreur à afficher en cas de saisie incorrecte.
        min_val (int/float): La valeur minimale acceptée (par défaut -infini).
        max_val (int/float): La valeur maximale acceptée (par défaut infini).
        

    Returns:
        value: La valeur saisie et validée par l'utilisateur.
    """
    value = None
    while True:
        try:
            value = Type(input(Texte))  # Conversion basée sur le type fourni
            # Vérification des bornes uniquement pour les types numériques
            if isinstance(value, (int, float)):
                if value < min_val or value > max_val:
                    print(f"\033[31m La valeur doit être comprise entre {min_val} et {max_val}.\033[0m")
                    continue
            return value
        except ValueError:
            print("\033[31m" +  Error + "\033[0m")


##################################################################################################################
##################################################################################################################
##################################          FONCTION             #################################################
##################################            POUR               #################################################
##################################          LES MENUS            #################################################
##################################################################################################################
##################################################################################################################

def lancement (jeux : str) :
    """
    Fonction pour lancer un jeu 
    Args:
        jeux (str) : Nom du jeu 
    Returns:
        None : None
    """

    if jeux == "devinette" :
        effacer_console()   
        nombrelignehorizontale(1, 55)
        print("\033[92m Lancement du jeu de la devinette \033[0m")
        nombrelignehorizontale(1, 55)
        from devinette import devinette
        devinette()

    if jeux == "allumette" :
        effacer_console()
        nombrelignehorizontale(1, 55)
        print("\033[92m Lancement du jeu des allumettes \033[0m")
        nombrelignehorizontale(1, 55)
        from allumette import allumette
        allumette()

    if jeux == "morpion" :
        effacer_console()
        nombrelignehorizontale(1, 55)
        print("\033[92m Lancement du jeu du morpion \033[0m")
        nombrelignehorizontale(1, 55)
        from morpion import morpionjouer
        morpionjouer()

    if jeux == "puissance4" :
        effacer_console()
        nombrelignehorizontale(1, 55)
        print("\033[92m Lancement du jeu du puissance 4 \033[0m")
        nombrelignehorizontale(1, 55)
        from puissance4Bonus import puissance4
        puissance4()

#########################################################
#########################################################
#########################################################

def switch(cas : list[str]) :
    """
    Fonction pour les switch 
    Args:
        cas (list[str]): Liste des cas possibles.
    Returns:
        None : None
    """
    for i in range(len(cas)) :
        print(str(i) + " : " + cas[i])

#########################################################
#########################################################
#########################################################

def menu (cas : str) :
    """
    Fonction pour les menus
    Args:
        cas (str) : Nom du cas
    Returns:
        None : None
    """

    listejeux = ["Le jeux des devinettes.", "Le jeu des allumettes.", "Le jeu du morpion.","Le jeu du puissance 4.","Afficher les scores totaux.","Quitter les mini-jeux."]
    listedevinette = ["Plus grand", "Plus petit", "C'est gagné !"]

    if cas == "main" :
        print("Bienvenue dans le HUB, ici vous pouvez choisir ce que vous voulez faire parmis les choix suivants : ")

    if cas == "jeux" :
        switch(listejeux)

    if cas == "devinette" :
        switch(listedevinette)

    if cas == "quitter" :
        print(" \033[33m Êtes-vous sûr de quitter les mini-jeux ? \033[0m")
        x = inputCustom(" \033[33m 0 : Oui / 1 : Non --> \033[0m", int, "La valeur doit être un entier", 0, 1)

        if x == 0 :
            print("Merci d'avoir joué, à bientôt !")
            sleep(2)
            effacer_console()
            exit()
            
        else :
            from main import main
            main()

#########################################################
#########################################################
#########################################################

def quitterjeux(jeux : str) :
    """
    Fonction pour quitter un jeu
    Args:
        jeux (str) : Nom du jeu
    Returns:
        None : None
    """

    choix : int 

    # Demander si le joueur veut quitter
    print("\033[33m Voulez-vous vraiment quitter ? \033[0m")
    choix = int(inputCustom("\033[33m 0 : Oui / 1 : Non --> \033[0m", int, "La valeur doit être un entier", 0, 1))

    # Si le joueur veut quitter
    if choix == 0 :
        print("Merci d'avoir joué, à bientôt !")
        print("Retour au menu principal")

        effacer_console()
        nombrelignehorizontale(1, 55)
        print("\033[92m Arrivée au menu principal \033[0m")
        nombrelignehorizontale(1, 55)
        from main import main
        main()
    
    # Si le joueur veut relancer une partie
    if choix == 1 :
        print("Relancer une partie !")

        if jeux == "devinette" :
            effacer_console()   
            nombrelignehorizontale(1, 55)
            print("\033[92m Lancement d'une nouvelle partie de devinette \033[0m")
            nombrelignehorizontale(1, 55)
            from devinette import devinette
            devinette()

        if jeux == "allumette" :
            effacer_console()
            nombrelignehorizontale(1, 55)
            print("\033[92m Lancement d'une nouvelle partie de allumette \033[0m")
            nombrelignehorizontale(1, 55)
            from allumette import allumette
            allumette()

        if jeux == "morpion" :
            effacer_console()
            nombrelignehorizontale(1, 55)
            print("\033[92m Lancement d'une nouvelle partie de morpion \033[0m")
            nombrelignehorizontale(1, 55)
            from morpion import morpionjouer
            morpionjouer()

        if jeux == "puissance4" :
            effacer_console()
            nombrelignehorizontale(1, 55)
            print("\033[92m Lancement d'une nouvelle partie de puissance 4 \033[0m")
            nombrelignehorizontale(1, 55)
            from puissance4Bonus import puissance4
            puissance4()

        if jeux == "main" :
            effacer_console()
            afficher_scores_total()

##################################################################################################################
##################################################################################################################
##################################          GESTION             ##################################################
##################################            DES               ##################################################
##################################          SCORES              ##################################################
##################################################################################################################
##################################################################################################################

def listejoueur(jeux: str) -> List[str]:
    """
    Fonction pour créer une liste de joueurs pour un jeu donné.
    Args:
        jeux (str): Nom du jeu
    Returns:
        List[str]: Liste des noms des joueurs
    """

    compteur: int = 0
    joueurs: List[str] = []

    print("\033[33mVous devez d'abord rentrer les noms des joueurs : \033[0m")
    print("Saisissez le nom des deux joueurs : ")

    # Collecter les noms des joueurs
    while compteur < 2:
        nom = str(inputCustom(f"Entrez le nom du joueur {compteur + 1} : ", str, "Le nom doit être une chaîne de caractères."))

        while nom == "":  # Vérifier si le nom est vide
            print("\033[33mErreur : le nom du joueur ne peut pas être vide. Veuillez réessayer.\033[0m")
            nom = str(inputCustom(f"Entrez le nom du joueur {compteur + 1} : ", str, "Le nom doit être une chaîne de caractères."))
        
        # Normalisation du nom : enlever les espaces, mettre en minuscules et capitaliser
        nom_normalise = nom.strip().capitalize()
        
        joueurs.append(nom_normalise)
        compteur += 1        

    # Enregistrer les joueurs et leur score initial (0) dans le fichier
    for joueur in joueurs:
        enregistrer_score_binaire(jeux, joueur, 0)

    return joueurs  # Retourner directement la liste des joueurs

########################################################
########################################################
########################################################

def lire_scores_par_joueur_binaire(nom_jeu: str) -> List[str]:
    """
    Fonction pour lire les scores depuis un fichier binaire.
    Args:
        nom_jeu (str): Nom du jeu
    Returns:
        List[str]: Liste des scores sous forme de chaîne (nom_joueur:score)
    """
    nom_fichier = f'./score/{nom_jeu}.bin'
    try:
        with open(nom_fichier, 'rb') as fichier:
            return pickle.load(fichier)
    except (FileNotFoundError, EOFError):
        # Retourne une liste vide si le fichier n'existe pas ou est vide
        return []
    
########################################################
########################################################
########################################################

def est_un_nombre(val: str) -> bool:
    """
    Fonction pour vérifier si une chaîne de caractères est un nombre.
    Args:
        val (str): Chaîne de caractères à vérifier
    Returns:
        bool: True si la chaîne est un nombre, False sinon
    """
    try:
        int(val)
        return True
    except ValueError:
        return False

########################################################
########################################################
########################################################

def enregistrer_score_binaire(nom_jeu: str, nom_joueur: str, nouveau_score: int) -> None:
    """
    Fonction pour enregistrer un nouveau score pour un joueur dans un fichier binaire.
    Args:
        nom_jeu (str): Nom du jeu
        nom_joueur (str): Nom du joueur
        nouveau_score (int): Score à ajouter
    Returns:
        None
    """
    nom_fichier = f'./score/{nom_jeu}.bin'

    # Lire les scores existants
    scores_liste = lire_scores_par_joueur_binaire(nom_jeu)

    # Traiter et valider les données existantes
    scores_valides : List[str]
    scores_valides = []

    joueur_trouve = False

    for joueur_score in scores_liste:
        if ':' not in joueur_score:
            print(f"Entrée ignorée (format invalide) : {joueur_score}")
            continue
        joueur, score_str = joueur_score.split(':', 1)
        if not joueur or not score_str or not est_un_nombre(score_str):
            print(f"Entrée ignorée (format invalide) : {joueur_score}")
            continue
        if joueur == nom_joueur:
            # Mettre à jour le score pour le joueur trouvé
            score = int(score_str) + nouveau_score
            scores_valides.append(f"{joueur}:{score}")
            joueur_trouve = True
        else:
            scores_valides.append(joueur_score)

    # Ajouter un nouveau joueur s'il n'est pas trouvé
    if not joueur_trouve:
        scores_valides.append(f"{nom_joueur}:{nouveau_score}")

    # Écrire tous les scores mis à jour dans le fichier binaire
    with open(nom_fichier, 'wb') as fichier:
        pickle.dump(scores_valides, fichier)

    print(f'Score de {nouveau_score} ajouté pour le joueur {nom_joueur} dans le fichier {nom_fichier}.')


########################################################
########################################################
########################################################


def afficher_scores_final(nom_jeu: str) -> None:
    """
    Fonction pour afficher les scores finaux des joueurs d'un jeu.
    Affiche les scores dans un format clair et lisible et détermine le(s) gagnant(s) en fonction
    du score le plus proche de 0 si le jeu est "allumette", sinon le(s) gagnant(s) a/ont le score le plus élevé.

    Args:
        nom_jeu (str): Nom du jeu
    Returns:
        None : None
    """

    # Initialisation des variables
    gagnants: List[str] = []  # Liste pour stocker les gagnants
    score_max: int = -1       # Valeur de départ pour le jeu normal (score le plus élevé)
    score_proche_0: int = 1000 # Valeur de départ pour le jeu "allumette" (score le plus proche de 0)

    # Lire les scores depuis le fichier binaire
    scores_liste: List[str] = lire_scores_par_joueur_binaire(nom_jeu)
    
    if not scores_liste:
        print(f"Aucun score n'est disponible pour le jeu {nom_jeu}.")
        return
    
    print("\n\033[1m--- Scores finaux ---\033[0m")
    
    # Affichage des scores
    for joueur_score in scores_liste:
        joueur, score_str = joueur_score.split(':')
        score = int(score_str)
        print(f"{joueur}: \033[1m{score}\033[0m points")
        
        # Si le jeu est "allumette", on cherche le score le plus proche de 0
        if nom_jeu == "allumette":
            # Nouveau gagnant si score plus proche de 0
            if abs(score) < abs(score_proche_0):
                gagnants = [joueur]
                score_proche_0 = score
            # Ajouter à la liste si égalité avec le score le plus proche de 0
            elif abs(score) == abs(score_proche_0):
                gagnants.append(joueur)
        else:
            # Sinon, on cherche le score le plus élevé
            if score > score_max:
                gagnants = [joueur]
                score_max = score
            elif score == score_max:
                gagnants.append(joueur)
    
    # Vérification que des gagnants ont été déterminés
    if not gagnants:
        print(f"Erreur : Aucun gagnant n'a été déterminé.")
        return

    # Affichage du/des gagnants et de leur score
    if nom_jeu == "allumette":
        gagnants_str = ", ".join(gagnants)
        print(f"\nLe(s) gagnant(s) pour le jeu des allumettes est/sont \033[1m{gagnants_str}\033[0m avec \033[1m{score_proche_0}\033[0m points (proximité à 0)!")
    else:
        gagnants_str = ", ".join(gagnants)
        print(f"\nLe(s) gagnant(s) pour le jeu {nom_jeu} est/sont \033[1m{gagnants_str}\033[0m avec \033[1m{score_max}\033[0m points!")

    print("\033[1m--- Fin des scores ---\033[0m \n")

########################################################
########################################################
########################################################

def reinitialiser_scores_binaire(nom_jeu: str) -> None:
    """
    Fonction pour réinitialiser les scores des joueurs d'un jeu dans un fichier binaire.

    Args:
        nom_jeu (str): Nom du jeu
    Returns:
        None : None
    """

    nom_fichier: str
    nom_fichier = f'./score/{nom_jeu}.bin' # Nom du fichier binaire
    choix: int

    print(f"\033[33m Voulez-vous réinitialiser les scores pour le jeu {nom_jeu} ? \033[0m")
    choix = int(inputCustom("\033[33m 0 : Oui / 1 : Non --> \033[0m", int, "La valeur doit être un entier", 0, 1))

    if choix == 0: 
        print(f"Réinitialisation des scores pour le jeu {nom_jeu}...")

        try:
            # Ouvrir le fichier en mode binaire et y écrire une liste vide
            with open(nom_fichier, 'wb') as fichier:
                pickle.dump([], fichier)  # Écrire une liste vide pour réinitialiser les scores

            effacer_console()

            print(f'Les scores pour le jeu {nom_jeu} ont été réinitialisés. \n')
        except FileNotFoundError:
            print(f'Le fichier pour le jeu {nom_jeu} est introuvable.')
    
    if choix == 1:
        print("Lancement du jeu...")

########################################################
########################################################
########################################################

def afficher_scores_total() -> None:
    """
    Fonction pour afficher les scores finaux de tous les jeux disponibles, un par un.
    Affiche les scores dans un format clair et lisible et détermine les gagnants pour chaque jeu.
    
    Args:
        None
    
    Returns:
        None : None
    """

    # Liste des jeux disponibles (noms des jeux pour lesquels il existe des fichiers binaires de scores)
    jeux_disponibles = ['allumette', 'devinette', 'morpion', 'puissance4']

    if not jeux_disponibles:
        print("Aucun jeu n'est disponible.")
        return

    # Afficher les scores pour chaque jeu avec une séparation claire
    for nom_jeu in jeux_disponibles:
        print("=" * 50)  # Séparation entre les jeux
        print(f"\033[1m\033[92mScores pour le jeu {nom_jeu}\033[0m")  # Titre en vert
        print("=" * 50)
        try:
            afficher_scores_final(nom_jeu)  # Fonction à définir ou à importer
        except FileNotFoundError:
            print(f"⚠️ Fichier de scores introuvable pour le jeu {nom_jeu}.")
        except Exception as e:
            print(f"⚠️ Une erreur s'est produite pour le jeu {nom_jeu} : {e}")
        
        # Message de fin des scores pour le jeu
        print("=" * 50)
        print(f"\033[1m\033[91mFin des scores pour le jeu {nom_jeu}\033[0m")  # Message en rouge
        print("=" * 50)

    quitterjeux("main")

##################################################################################################################
##################################################################################################################
##################################                          ######################################################
##################################          FIN             ######################################################
##################################                          ######################################################
##################################################################################################################
##################################################################################################################