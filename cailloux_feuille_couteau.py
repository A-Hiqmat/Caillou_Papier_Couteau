#importation du module random pour les décisions de l'Ordinateur
import random
ordi = ["Caillou","Papier","Couteau"]

#Intro
print("Bienvenue dans cette partie de Caillou, Papier, Couteau !")

#La partie ne commence que si le joeur indique un nombre de manche valable
nbr_tour = ""
while nbr_tour == "" :
    try:
        nbr_tour = int(input("Combien de parties souhaitez-vous jouer ? : "))
    except ValueError:
        print("Veuillez entrer un nombre valide !")

#On définis la fonction
def jeux():
    #se reinitialisent si placé à l'intérieur de la boucle
    point_ordi = 0
    point_joueur = 0
    
    #Ajout d'une boucle for qui éxecute autant de fois le nombre de manches indiqué par le joueur
    for i in range (nbr_tour):
        choix_ordi=random.choice(ordi)
                
        #Menu d'option + Scores + Compteur de tour
        print(f"Manche {i+1} sur {nbr_tour} ")
        print("1.Caillou")
        print("2.Papier")
        print("3.Couteau")
        print("4.Quitter")
        print(f"Score joueur : {point_joueur}  Score Ordi : {point_ordi} ")

        #Sort de la boucle uniquement si le choix est valide (cela evite que le nbr_tour accepte toute sorte de tentatives même celle en str)
        while True:
            choix = input("Entrez votre choix (1-4): ")
            if choix in ["1", "2", "3", "4"]:
                break
            else:
                print("Choix invalide, veuillez entrer un numéro entre 1 et 4.")

        if choix == "1" and choix_ordi =="Caillou":
            print(f"Votre choix : Caillou \nl'ordinateur : Caillou \nIl y a donc égalité")
        elif choix == "1" and choix_ordi =="Papier":
            print(f"Votre choix : Caillou \nl'ordinateur : Papier \nVous perdez")
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
            print(f"Scores finaux  joueur : {point_joueur}  Ordi : {point_ordi} ")
            return

    #Verdict et Scores finaux
    print(f"Vous venez de completer votre dernière partie en jouant {nbr_tour} manches") 
    if point_joueur < point_ordi :
        print("Malheureusement, vous avez gagné moins de manche que l'ordinateur")
        print(f"Score joueur : {point_joueur}  Score Ordi : {point_ordi} ")
    elif point_joueur > point_ordi :
        print("Félicitation, vous avez gagné plus de manche que l'ordinateur")
        print(f"Score joueur : {point_joueur}  Score Ordi : {point_ordi} ")
    elif point_joueur == point_ordi :
        print("Incroyable ,il y a une égalité parfaite !")

#On appelle la fonction pour l'activer
jeux()