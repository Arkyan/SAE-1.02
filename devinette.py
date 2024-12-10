from fonction import *
from time import sleep
from random import randint
import getpass

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

    if mode_jeu == 0 :
        intervalle = randint(1, 100)
    if mode_jeu == 1 :
        intervalle = randint(1, 1000)
    if mode_jeu == 2 :
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
############################################################




############################################################
############################################################
############################################################

def devinette():
    """
    Fonction pour jouer au jeu de la devinette \n
    Paramètres : None \n
    Retourne : None
    """

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

    gagner = False
    Sicompteur : str
    compteur : int
    compteur_max : int
    compteur = 0
    compteur_max = 0

    #Proposition réinitialisation des scores
    reinitialiser_scores_binaire("devinette")

    mode_jeu = choix_mode_jeu()
    if mode_jeu == 0 :
        print("Vous avez choisi le mode Joueur contre Joueur")
        difficulte = 0
    else :
        difficulte = choix_difficulte()
    
    # Assigner les joueurs aléatoirement
    j = randint(1, 2)

    #Choix des joueurs
    #Mode Joueur contre Joueur
    if mode_jeu == 0 :
        # Liste des joueurs
        listej = listejoueur("devinette", mode_jeu)
    
        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]
    
    #Mode Joueur contre IA
    elif mode_jeu == 1 :
        # Liste des joueurs
        listej = listejoueur("devinette", mode_jeu)

        if j == 1 :
            joueur1 = listej[0]
            joueur2 = listej[1]
        else :
            joueur1 = listej[1]
            joueur2 = listej[0]

    #Mode IA contre IA
    elif mode_jeu == 2 :
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
    while gagner==False:
        si_IA = siIA(listej)

######################################
        #Mode Joueur contre Joueur
        if si_IA == 0 or (si_IA == 1 and joueur1 != "IA1") :
            intervalle = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, Choisissez l'intervalle de jeu entre 1 et n : ", int, "La valeur doit être un entier", 1, 100))
            nbrmystere = saisie_nombremystere(intervalle, joueur1)
            print("\033[F\033[K", end="") #Efface la ligne précédente pour ne pas afficher le nombre mystère
            print(f"\033[0;36m{joueur1}\033[0m a choisi le nombre à deviner c'est à \033[0;36m{joueur2}\033[0m de jouer ! \n") 

            sleep(3)
            effacer_console()
            # Le joueur 2 fait une supposition
            nbrdevine = int(inputCustom(f"\033[0;36m{joueur2}\033[0m, quel est le nombre ? ", int, "La valeur doit être un entier", 1, intervalle))
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

######################################
        #Mode Joueur contre IA
        elif si_IA == 1 and joueur1 == "IA1" :
            intervalle = bot_choix_intervalle(difficulte)
            nbrmystere = bot_choix_nombremystere(intervalle)

        elif si_IA == 1 and joueur2 == "IA1" :
            intervalle = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, Choisissez l'intervalle de jeu entre 1 et n : ", int, "La valeur doit être un entier", 1, 100))
            nbrmystere = saisie_nombremystere(intervalle, joueur1)         

######################################
        #Mode IA contre IA
        elif si_IA == 2 :
            intervalle = bot_choix_intervalle(difficulte)
            nbrmystere = bot_choix_nombremystere(intervalle)

        #Mode par défaut en cas de problème
        else :
            intervalle = 100
            nbrmystere = 1
            print("Si on est rentré ici c'est qu'il y a un problème ")

    afficher_scores_final("devinette")
    quitterjeux("devinette")