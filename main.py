#Jules Catelain
#tp3
#12 décembre 2023

#inspirée des informations donnés sur le document classroom
#On montre les variables
import random
niveau_de_vie = 20
force_de_adversaire = 0
numéro_adversaire = 0
victoires_consecutives = 0
nombre_combat = 0
nombre_victoire = 0
nombre_défaite = 0
choix = None
#tant que tu choisis pas de quitter, le jeu continue
while choix != '4':

#point  de départ
    numéro_adversaire +=1
    force_de_adversaire = random.randint(3, 7)
# Le choix un représente les actions si tu as trois victoires consécutives (combat de boss)
    if victoires_consecutives == 3:
        force_de_adversaire = random.randint(1,10)
        print('tu encontre un boss grace tu suite de victoire, sa force est de', force_de_adversaire)
        print("la force de l'aversaire est de", force_de_adversaire)
    print("Tu as le choix entre 1- combatttre l'adversaire, 2- contourner l'adversaire et prendre une porte, "
      "3- afficher les règles du jeu ou 4- quitter la partie")
    choix = input("Quel choix prend-tu?")


#le choix 1 montre les evénements si tu choisi de combattre l'adversaire
    if choix == "1":
        print("Adversaire:", numéro_adversaire, '')
        de = random.randint(1,6) + random.randint(1,6) #On lance deux dés pour avoir un combat plus difficile


        #evénements en cas de défaite
        if de < force_de_adversaire:
            print('defaite')
            nombre_défaite +=1
            niveau_de_vie = niveau_de_vie - force_de_adversaire
            victoires_consecutives = 0
            print('ton niveau de vie est de', niveau_de_vie)
            print('ton niveau de victoires conscutives est de', victoires_consecutives)

        #évenments en cas de victoire
        else:
            print("Victoire!")
            nombre_victoire += 1
            niveau_de_vie = niveau_de_vie + force_de_adversaire
            victoires_consecutives +=1
            print('ton niveau de vie est de', niveau_de_vie)
            print('ton niveau de victoires conscutives est de', victoires_consecutives)


#le choix 2 montres les évenements si tu choisi de éviter l'adversaire et de prendre la porte
    elif choix == "2":
        print("yu décide de éviter le combat, tu perd un point de vie")
        niveau_de_vie -=1
        print('Ton niveau de vie est maintenant', niveau_de_vie)

#description de règles du jeu
    elif choix == "3":
        print("Voici les règles du jeu: Un, pour réussire un combat, la valeur de la force de ladversaire doi être inférieur a la valeur de dé")
        print("Dans ce cas, la vie de lusager est augmenté de la force de adversaire")
        print("Une défaite a lieu au contraire des rèegles de la victoire mensionné précedement")
        print("Dans la cas d'une défaite, la vie de l'usager est soustrait de la force de L'adversaire.")
        print("Tu peux combattre ou éviter chaque adversaire, mais si tu l'évite, tu perd un point de vie")

    
#Quitter la partie
print('terminé')






