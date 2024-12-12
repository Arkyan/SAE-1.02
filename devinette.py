from fonction import *
from time import sleep
from random import randint
import getpass
from typing import List

def saisie_nombremystere(intervalle: int, joueuractuel : str) -> int:
    """
    Fonction pour saisir le nombre mystère avec une saisie cachée.
    Args:
        intervalle (int): L'intervalle de jeu.
    Returns:
        int: Le nombre mystère.
    """
    nombremystere = None
    while nombremystere is None:
        saisie = getpass.getpass(f"\033[0;36m{joueuractuel}\033[0m, Saisissez le nombre mystère : ")
        
        # Vérifie si la saisie est un nombre entier et dans l'intervalle valide
        if saisie.isdigit():
            nombremystere = int(saisie)
            if 1 <= nombremystere <= intervalle:
                print("Le nombre mystère a bien été enregistré.")
            else:
                print(f"Le nombre doit être compris entre 1 et {intervalle}.")
                # Si la saisie est invalide ou en dehors de l'intervalle, on redemande
                nombremystere = None
        else:
            print("Veuillez entrer un nombre entier valide.")
            # Si la saisie est invalide ou en dehors de l'intervalle, on redemande
            nombremystere = None
        
    return nombremystere


############################################################
def bot_choix_intervalle(mode_jeu : int) -> int :

    """
    Fonction pour choisir l'intervalle de jeu pour le bot
    Args:
        mode_jeu (int): Le mode de jeu.
    Returns:
        int: L'intervalle de jeu.
    """
    intervalle : int
    intervalle = 0

    #Mode hasard
    if mode_jeu == 1 :
        intervalle = randint(1, 100)

    #Mode entre-deux
    if mode_jeu == 2 :
        intervalle = randint(1, 1000)

    #Mode dichotomie/complexe
    if mode_jeu == 3 :
        intervalle = randint(1, 10000)

    return intervalle

def bot_choix_nombremystere(intervalle : int) -> int :
    """
    Fonction pour choisir le nombre mystère pour le bot
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
        if retour_jeu == 1:  # Plus petit
            borne_max = min(borne_max, nbr_prec - 1)
        elif retour_jeu == 0:  # Plus grand
            borne_min = max(borne_min, nbr_prec + 1)

        valeur_renvoye = randint(borne_min, borne_max)
        print(f"Le nombre donné par l'IA est {valeur_renvoye} (intervalle: [{borne_min}, {borne_max}])")
        return valeur_renvoye

    # Mode difficulté maximale
    else:
        if retour_jeu == 1:  # Plus petit
            borne_max = min(borne_max, nbr_prec - 1)
        elif retour_jeu == 0:  # Plus grand
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
    
##################################################################################################################
##################################################################################################################
##################################             DÉBUT             #################################################
##################################              DU               #################################################
##################################             JEU               #################################################
##################################################################################################################
##################################################################################################################

def devinette():
    """
    Fonction pour jouer au jeu de la devinette \n
    Paramètres : None \n
    Retourne : None
    """

    #Initialisation des variables
    intervalle: int
    nbrmystere: int
    j: int
    joueur1: str
    joueur2: str
    listej: list[str]
    gagner: bool

    mode_jeu : int 
    difficulte : int
    si_IA : int

    borne_min : int
    borne_max : int

    listecoup : List[int] 
    listecoup = []

    gagner = False
    Sicompteur : str
    compteur : int
    compteur_max : int
    compteur = 0
    compteur_max = 0

    #Proposition réinitialisation des scores
    reinitialiser_scores_binaire("devinette")

    #Choix du mode de jeu ainsi que de la difficulté
    mode_jeu = choix_mode_jeu()
    if mode_jeu == 1 :
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
    if mode_jeu == 1 :
        # Liste des joueurs
        listej = listejoueur("devinette", mode_jeu)
    
        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]
    
    #Mode Joueur contre IA
    elif mode_jeu == 2 :
        # Liste des joueurs
        listej = listejoueur("devinette", mode_jeu)

        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]

    #Mode IA contre IA
    elif mode_jeu == 3 :
        listej = listejoueur("devinette", mode_jeu)

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

############################################################

    #Effacement de la console avec un sleep pour laisser le temps de lire
    sleep(3)
    effacer_console()
    nombrelignehorizontale(1, 55)
    print("\033[92m Lancement du jeu de la devinette \033[0m")
    nombrelignehorizontale(1, 55)

    #Choix du compteur
    print("Si vous rentrez autre chose que 'Oui', le compteur sera désactivé.")
    Sicompteur = str(inputCustom("Voulez-vous choisir le nombre de tours ? (Oui/Non) : ", str, "La valeur doit être un caractère")).capitalize() 
    if Sicompteur == "Oui" :
        compteur_max = int(inputCustom("Choisissez le nombre de tours : ", int, "La valeur doit être un entier", 1, 50))
    else :
        compteur_max = 1500000000000000000 #Nombre très grand pour ne pas arrêter le jeu

############################################################
############################################################
############################################################

    #Début de la boucle de jeu
    si_IA = siIA(listej)

# ──────────────────────────────────────────────────────────────
#                     MODE JOUEUR CONTRE JOUEUR
# ──────────────────────────────────────────────────────────────
    if si_IA == 0 :
        intervalle = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, Choisissez l'intervalle de jeu entre 1 et n : ", int, "La valeur doit être un entier", 1, 100))
        nbrmystere = saisie_nombremystere(intervalle, joueur1)
        print("\033[F\033[K", end="") #Efface la ligne précédente pour ne pas afficher le nombre mystère
        print(f"\033[0;36m{joueur1}\033[0m a choisi le nombre à deviner c'est à \033[0;36m{joueur2}\033[0m de jouer ! \n") 
        while not gagner :
            sleep(3)
            effacer_console()

            # Le joueur 2 fait une supposition
            nbrdevine = int(inputCustom(f"\033[0;36m{joueur2}\033[0m, quel est le nombre ? ", int, "La valeur doit être un entier", 1, intervalle))
            listecoup.append(nbrdevine)
            menu("devinette")
            valeur = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, votre choix 0 / 1 / 2 : ", int, "La valeur doit être un 0, 1 ou 2", 0, 2))
            print("\033[F\033[K", end="")

            # Le joueur 1 répond
            if valeur == 2 and nbrdevine != nbrmystere :
                print(f"Vous ne pouvez pas dire que le nombre est trouvé si ce n'est pas le bon nombre !")
                while valeur == 2 and nbrdevine != nbrmystere :
                    valeur = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, votre choix 0 / 1 / 2 : ", int, "La valeur doit être un 0, 1 ou 2", 0, 2))

            if valeur == 0:
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus grand\033[0m")
            if valeur == 1:
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus petit\033[0m")

            # Si le nombre n'a pas été trouvé en compteur_max tours
            if Sicompteur == "Oui" :
                compteur += 1
            if compteur == compteur_max :
                effacer_console()
                print(f"Le nombre à deviner était {nbrmystere} !")
                print(f"Le nombre n'a pas été trouvé en {compteur_max} tours !")
                print(f"Bravo à {joueur1} pour avoir caché le nombre !\n")
                gagner = True
                enregistrer_score_binaire("devinette", joueur1, 1)

            # Si le joueur 2 trouve le bon nombre
            if valeur == 2 and nbrdevine == nbrmystere :
                effacer_console()
                print(f"Bravo {joueur2}, vous avez trouvé le nombre à deviner ! Le nombre à deviner était bien {nbrmystere} !")
                gagner = True
                enregistrer_score_binaire("devinette", joueur2, 1)


# ──────────────────────────────────────────────────────────────
#                MODE IA CONTRE JOUEUR
# ──────────────────────────────────────────────────────────────
    elif si_IA == 1 and joueur1 == "IA1" :

        intervalle = bot_choix_intervalle(difficulte)
        nbrmystere = bot_choix_nombremystere(intervalle)
        print(f"\033[0;36m{joueur1}\033[0m a choisi le nombre à deviner c'est à \033[0;36m{joueur2}\033[0m de jouer ! \n")

        while not gagner :
            sleep(3)
            effacer_console()

            # Le joueur 2 fait une supposition
            print(f"L'intervalle de jeu est de 1 à {intervalle}")
            print(f"TEMPORAIRE : Le nombre mystère est {nbrmystere}")
            nbrdevine = int(inputCustom(f"\033[0;36m{joueur2}\033[0m, quel est le nombre ? ", int, "La valeur doit être un entier", 1, intervalle))
            listecoup.append(nbrdevine)
            valeur = bot_reponse_intervalle_devinette(nbrdevine, nbrmystere)

            if valeur == 0:
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus grand\033[0m")
            if valeur == 1:
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus petit\033[0m")

            # Si le nombre n'a pas été trouvé en compteur_max tours
            if Sicompteur == "Oui" :
                compteur += 1
            if compteur == compteur_max :
                effacer_console()
                print(f"Le nombre à deviner était {nbrmystere} !")
                print(f"Le nombre n'a pas été trouvé en {compteur_max} tours !")
                print(f"Bravo à {joueur1} pour avoir caché le nombre !\n")
                print(f"Pas de score pour l'IA")
            
            # Si le joueur 2 trouve le bon nombre
            if valeur == 2 and nbrdevine == nbrmystere :
                effacer_console()
                print(f"Bravo {joueur2}, vous avez trouvé le nombre à deviner ! Le nombre à deviner était bien {nbrmystere} !")
                gagner = True
                enregistrer_score_binaire("devinette", joueur2, 1)
 
# ──────────────────────────────────────────────────────────────
#            MODE JOUEUR CONTRE IA 
# ──────────────────────────────────────────────────────────────
    elif si_IA == 1 and joueur2 == "IA1" :
        intervalle = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, Choisissez l'intervalle de jeu entre 1 et n : ", int, "La valeur doit être un entier", 1, 100))
        nbrmystere = saisie_nombremystere(intervalle, joueur1)
        print(f"\033[0;36m{joueur1}\033[0m a choisi le nombre à deviner c'est à \033[0;36m{joueur2}\033[0m de jouer ! \n")

        #Initialisation des variables
        valeur = -1
        nbrdevine = -1
        borne_min = 1
        borne_max = intervalle

        while not gagner :  
            sleep(3)
            effacer_console()

            # Le joueur 2 fait une supposition
            nbrdevine = bot_devinnette(difficulte, intervalle, valeur, nbrdevine, borne_min, borne_max)

            listecoup.append(nbrdevine)
            menu("devinette")
            valeur = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, votre choix 0 / 1 / 2 : ", int, "La valeur doit être un 0, 1 ou 2", 0, 2))

            # Le joueur 1 répond
            if valeur == 2 and nbrdevine != nbrmystere:
                print(f"Vous ne pouvez pas dire que le nombre est trouvé si ce n'est pas le bon nombre !")
                while valeur == 2 and nbrdevine != nbrmystere:
                    valeur = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, votre choix 0 / 1 / 2 : ", int, "La valeur doit être un 0, 1 ou 2", 0, 2))
            if valeur == 0:  # Plus grand
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus grand\033[0m")
                borne_min = max(borne_min, nbrdevine + 1)  # Mise à jour de la borne minimale
            if valeur == 1:  # Plus petit
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus petit\033[0m")
                borne_max = min(borne_max, nbrdevine - 1)  # Mise à jour de la borne maximale
            
            # Si le nombre n'a pas été trouvé en compteur_max tours
            if Sicompteur == "Oui" :
                compteur += 1
            if compteur == compteur_max :
                effacer_console()
                print(f"Le nombre à deviner était {nbrmystere} !")
                print(f"Le nombre n'a pas été trouvé en {compteur_max} tours !")
                print(f"Bravo à {joueur1} pour avoir caché le nombre !\n")
                gagner = True
                enregistrer_score_binaire("devinette", joueur1, 1)
                
            # Si le joueur 2 trouve le bon nombre
            if valeur == 2 and nbrdevine == nbrmystere :
                effacer_console()
                print(f"Bravo {joueur2}, vous avez trouvé le nombre à deviner ! Le nombre à deviner était bien {nbrmystere} !")
                gagner = True
                print("Pas de score pour l'IA")

# ──────────────────────────────────────────────────────────────
#                MODE IA CONTRE IA
# ──────────────────────────────────────────────────────────────
    #Mode IA contre IA
    elif si_IA == 2 :
        intervalle = bot_choix_intervalle(difficulte)
        nbrmystere = bot_choix_nombremystere(intervalle)
        print(f"\033[0;36m{joueur1}\033[0m a choisi le nombre à deviner c'est à \033[0;36m{joueur2}\033[0m de jouer ! \n")

        #Initialisation des variables
        valeur = -1
        nbrdevine = -1
        borne_min = 1
        borne_max = intervalle

        while not gagner :
            effacer_console()

            # Le joueur 2 fait une supposition
            nbrdevine = bot_devinnette(difficulte, intervalle, valeur, nbrdevine, borne_min, borne_max)

            listecoup.append(nbrdevine)
            valeur = bot_reponse_intervalle_devinette(nbrdevine, nbrmystere)

            # Le joueur 1 répond
            if valeur == 2 and nbrdevine != nbrmystere:
                print(f"Vous ne pouvez pas dire que le nombre est trouvé si ce n'est pas le bon nombre !")
                while valeur == 2 and nbrdevine != nbrmystere:
                    valeur = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, votre choix 0 / 1 / 2 : ", int, "La valeur doit être un 0, 1 ou 2", 0, 2))
            if valeur == 0:  # Plus grand
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus grand\033[0m")
                borne_min = max(borne_min, nbrdevine + 1)  # Mise à jour de la borne minimale
            if valeur == 1:  # Plus petit
                print(f"Le nombre à deviner n'est pas {nbrdevine} !\033[1m\033[31m Il est plus petit\033[0m")
                borne_max = min(borne_max, nbrdevine - 1)  # Mise à jour de la borne maximale

            # Si le nombre n'a pas été trouvé en compteur_max tours
            if Sicompteur == "Oui" :
                compteur += 1
                print(f"Tour n°{compteur}")

            if compteur == compteur_max :
                effacer_console()
                print(f"Le nombre à deviner était {nbrmystere} !")
                print(f"Le nombre n'a pas été trouvé en {compteur_max} tours !")
                print(f"Bravo à {joueur1} pour avoir caché le nombre !\n")
                print(f"Pas de score pour l'IA")
                gagner = True

            # Si le joueur 2 trouve le bon nombre
            if valeur == 2 and nbrdevine == nbrmystere :
                effacer_console()
                print(f"Bravo {joueur2}, vous avez trouvé le nombre à deviner ! Le nombre à deviner était bien {nbrmystere} !")
                gagner = True
                print("Pas de score pour l'IA")

    #Mode par défaut en cas de problème
    else :
        intervalle = 100
        nbrmystere = 1
        print("Si on est rentré ici c'est qu'il y a un problème ")

# ──────────────────────────────────────────────────────────────
#                FIN DIFFÉRENTS MODES DE JEU
# ──────────────────────────────────────────────────────────────

    #Affichage des coups
    print()
    for i in range(len(listecoup)) :
        print(f"Tour n°{i+1} : {listecoup[i]}")
    print()

    #Affichage des scores
    afficher_scores_final("devinette")

    #Proposition de quitter le jeu
    quitterjeux("devinette")