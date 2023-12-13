#Jules Catelain
#tp3
#13 décembre 2023
#inspirée des informations donnés sur classroom

#point de départ

import random

niveau_de_vie = 20
force_adversaire = 0
numero_adversaire = 0
nombre_victoire = 0
nombre_defaite = 0
victoires_consécutives = 0
numero_combat = 0
choix = 0
while choix != 4:


    force_adversaire = random.randint (1, 5)
    choix = int(input("Que veut tu faire, 1- combattre l'ennemi, 2-contourer l'aversaire et aller ouvrire une autre porte,"
          " 3- afficher les regles du jeu ou 4- Quitter la partie."))
    #combattre adversaire
    if choix == 1:
        print("Tu combat le monstre")
        de = random.randint (1, 6)
        if force_adversaire<de:
            niveau_de_vie = niveau_de_vie+force_adversaire
            nombre_victoire +=1
            victoires_consécutives+=1
            numero_adversaire +=1
            numero_combat +=1
        else:
            niveau_de_vie = niveau_de_vie-force_adversaire
            nombre_defaite +=1
            victoires_consecutives = 0
            numero_adversaire +=1
            numero_combat += 1

    elif choix == 2:
        print("Tu choisi de fuir et de prendre une autre porte")







