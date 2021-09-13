import os
import random

# Insertion
etudiants_liste = ["Arnaud", "Maud", "Thomas", "Floran", "Yannick", "Manu", "Juliette"]

with open('etudiants.txt', 'w+') as file:
    for etudiant in etudiants_liste:
        file.write(etudiant + "\n")
    file.close()
    
# Lecture de fichier
# Création
repas_liste = ["kebab", "mcdo", "japonais", "chinois", "thai", "poulet frites", "crepes", "omelette", "kfc", "tacos"]

with open('repas.txt', 'w+') as file:
    for repas in repas_liste:
        file.write(repas + "\n")
    file.close()
# Fin de création
# Lecture du fichier
if os.path.exists("repas.txt"):
    with open("repas.txt", "r+") as file:
        repas_liste =file.readlines()
        repas_choix = random.choice(repas_liste)
        print("Je vous propose aujourd'hui comme repas :", repas_choix)
        file.close()
else:
    print("Le document n'existe pas ! Attention !")