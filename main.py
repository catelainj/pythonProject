#Jules Catelain
#tp3
#30 octobre 2023

#import
import random

#def pour appeler le jeu
def joue():
    #definir les variables
    vies = 20
    victoires = 0
    defaites = 0
    adversaires = 0
    wins_in_a_row = 0

    #definir while pour que le jeu stop a zero vies
    while vies > 0:
        #random vie de adversaire
        ennemy_strengh = random.randint(1, 5)
        print(f"Tu tombe contre un ennemie de niveau : {ennemy_strengh}")

        print("Tu fais quoi mtn?")
        print("1- Tu le bat?")
        print("2- Évite tu le combat?")
        print("3- afficher les règles du jeu")
        print("4- quitter la partie")

        choix = input("entre ton choix : ")

        #choix 1
        if choix == "1":
            score = random.randint(1, 6)
            print("\nLancer dé :", score)

            #victoire
            if score > ennemy_strengh:
                print("Ennemie #", adversaires)
                print("Force du ennemie:", ennemy_strengh)
                print("vie du user:", vies)
                print("combat", adversaires, ":", victoires, "contre", defaites)
                print("\nLancer dé :", score)
                vies += ennemy_strengh
                victoires += 1
                adversaires += 1
                wins_in_a_row += 1
                print("Last battle = dub")
                print("vie du user:", vies)
                print("victoires consecutives:", wins_in_a_row)

            #défaite
            else:
                print("ennemei #", adversaires)
                print("force de l'ennemie:", ennemy_strengh)
                print("vie du user:", vies)
                print("combat", adversaires, ":", victoires, "contre", defaites)
                print("Lancer dé:", score)
                vies -= adversaires
                defaites += 1
                wins_in_a_row = 0
                print("vie du user, vies")

        #choix 2
        elif choix == "2":
            vies -= 1
            print("tu evite la fight. tu perd un point de vie pour avoir peur")
            print("vie du user:", vies)

        #choix 3
        elif choix == "3":
            print("\nPour gagner un combat, la valeur du dé doit etre meilleure que la force de l'ennemie")
            print("Quand ca arrive, la vie du user est augmenté avec la force du ennemie")
            print("Tu perd la fight' quand la valeur du dé est inférieur a la force de l'ennemie")
            print("\nGame ovr quand la vie du user est a 0")
            print("\nLe user peut eviter une fight mais perd un point de vie si il le fait.\n\n")

        #choix 4
        elif choix == "4":
            print("\nGame over")
            break

    print(f"Game over, ta battue {victoires} monstre(s).")
    joue()

#Démarer le jeu
joue()














