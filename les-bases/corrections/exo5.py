from random import randint

nombre = randint(1, 1000)

jeu = True

while jeu:
    utilisateur_prix = int(input("Veuillez entrer un prix:"))
    if nombre == utilisateur_prix:
        print("C'est gagné !, le prix était bien de {}€".format(utilisateur_prix))
        jeu = False
    elif nombre > utilisateur_prix:
        print("C'est plus !")
    else:
        print("C'est moins !")