import random
ordi = ["Caillou","Papier","Couteau"]
print("Bienvenue dans cette partie de Caillou ,Papier ,Couteau !")

#On définis la fonction
def jeux():
    #se reinitialisent si placé à l'intérieur de la boucle
    point_ordi = 0
    point_joueur = 0
    
    while True:
        
        choix_ordi=random.choice(ordi)
        #menu d'option + scores
        print("1.Caillou")
        print("2.Papier")
        print("3.Couteau")
        print("4.Quitter")
        print(f"Score joueur : {point_joueur}  Score Ordi : {point_ordi} ")
        choix = input("Entrez votre choix (1-4): ")
            
        if choix == "1" and choix_ordi =="Caillou":
            print(f"Votre choix : Caillou \nl'ordinateur : Caillou \nIl y a donc égalité")
        elif choix == "1" and choix_ordi =="Papier":
            print(f"Votre choix : Caillou \nl'ordinateur : Papier \n'Vous perdez'")
            point_ordi += 1
        elif choix == "1" and choix_ordi =="Couteau":
            print(f"Votre choix : Caillou \nl'ordinateur : Couteau \nVous gagnez")
            point_joueur += 1

        elif choix == "2" and choix_ordi =="Caillou":
            print(f"Votre choix : Papier \nl'ordinateur : Caillou \nVous gagnez")
            point_joueur += 1
        elif choix == "2" and choix_ordi =="Papier":
            print(f"Votre choix : Papier \nl'ordinateur : Papier \nIl y a donc égalité")
        elif choix == "2" and choix_ordi =="Couteau":
            print(f"Votre choix : Papier \nl'ordinateur : Couteau \nVous perdez")
            point_ordi += 1

        elif choix == "3" and choix_ordi =="Caillou":
            print(f"Votre choix : Couteau \nl'ordinateur : Caillou \nVous perdez")
            point_ordi += 1
        elif choix == "3" and choix_ordi =="Papier":
            print(f"Votre choix : Couteau \nl'ordinateur : Papier \nVous gagnez")
            point_joueur += 1
        elif choix == "3" and choix_ordi =="Couteau":
            print(f"Votre choix : Couteau \nl'ordinateur : Couteau \nIl y a donc égalité")

        elif choix == "4":
            print("Ce fut un plaisir de jouer avec vous. Au revoir!")
            break
        else:
            print("Choix invalide, veuillez entrer un numéro entre 1 et 4.")

#On appelle la fonction pour l'activer
jeux()