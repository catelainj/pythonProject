#Jules Catelain
#tp3
#12 décembre 2023

#inspirée des informations donnés sur le document classroom
import random
niveau_de_vie = 20
force_de_adversaire = 0
numéro_adversaire = 0
victoires_consecutives = 0
nombre_combat = 0
nombre_victoire = 0
nombre_défaite = 0
choix = None
while choix != '4':

#point  de départ
    numéro_adversaire +=1
    force_de_adversaire = random.randint(5, 10)
    if victoires_consecutives == 3:
        force_de_adversaire = random.randint(1,15)
        print('boss')
    print("la force de l'aversaire est de", force_de_adversaire)
    print("Tu as le choix entre 1- combatttre l'adversaire, 2- contourner l'adversaire et prendre une porte, "
      "3- afficher les règles du jeu ou 4- quitter la partie")
    choix = input("Quel choix prend-tu?")
    if choix == "1":
        print("Adversaire:", numéro_adversaire, '')
        de = random.randint(1,6) + random.randint(1,6)
        if de < force_de_adversaire:
            print('defaite')
            nombre_défaite +=1
            niveau_de_vie = niveau_de_vie - force_de_adversaire
            victoires_consecutives = 0
            print('ton niveau de vie est de', niveau_de_vie)
            print('ton niveau de victoires conscutives est de', victoires_consecutives)


        else:
            print("Victoire!")
            nombre_victoire += 1
            niveau_de_vie = 20
            victoires_consecutives +=1
            print('ton niveau de vie est de', niveau_de_vie)
            print('ton niveau de victoires conscutives est de', victoires_consecutives)

    elif choix == "2":
        print("yu décide de éviter le combat, tu perd un point de vie")
        niveau_de_vie -=1
        print('Ton niveau de vie est maintenant', niveau_de_vie)


    elif choix == "3":
        print("Voici les règles du jeu: Un, pour réussire un combat, la valeur de la force de ladversaire doi être inférieur a la valeur de dé")
        print("Dans ce cas, la vie de lusager est augmenté de la force de adversaire")
        print("Une défaite a lieu au contraire des rèegles de la victoire mensionné précedement")
        print("Dans la cas d'une défaite, la vie de l'usager est soustrait de la force de L'adversaire.")
        print("Tu peux combattre ou éviter chaque adversaire, mais si tu l'évite, tu perd un point de vie")

    #elif choix == 4:

print('terminé')






