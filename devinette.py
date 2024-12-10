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
    gagner = False
    Sicompteur : str
    compteur : int
    compteur_max : int
    compteur = 0
    compteur_max = 0

    #Proposition réinitialisation des scores
    reinitialiser_scores_binaire("devinette")

    # Liste des joueurs
    listej = listejoueur("devinette")

    # Vérification si la liste contient bien deux joueurs
    if len(listej) < 2:
        print("Erreur : il doit y avoir exactement 2 joueurs.")
        return
    
    #Effacement de la console avec un sleep pour laisser le temps de lire
    sleep(3)
    effacer_console()
    nombrelignehorizontale(1, 55)
    print("\033[92m Lancement du jeu de la devinette \033[0m")
    nombrelignehorizontale(1, 55)

    # Assigner les joueurs aléatoirement
    j = randint(1, 2)

    if j == 1 :
        joueur1 = listej[0]
        joueur2 = listej[1]
    else :
        joueur1 = listej[1]
        joueur2 = listej[0]

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

    #Début du jeu
    intervalle = int(inputCustom(f"\033[0;36m{joueur1}\033[0m, Choisissez l'intervalle de jeu entre 1 et n : ", int, "La valeur doit être un entier", 1, 100))
    nbrmystere = saisie_nombremystere(intervalle, joueur1)
    print("\033[F\033[K", end="") #Efface la ligne précédente pour ne pas afficher le nombre mystère
    print(f"\033[0;36m{joueur1}\033[0m a choisi le nombre à deviner c'est à \033[0;36m{joueur2}\033[0m de jouer ! \n") 

    while gagner==False:
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

    
    afficher_scores_final("devinette")
    quitterjeux("devinette")