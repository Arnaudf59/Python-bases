import statistics
from random import shuffle

# Voici notre liste
joueurs_en_ligne = ["Arnaud", "Maud", "Christelle"]
# Afficher la liste
print(joueurs_en_ligne)
# Afficher la premiere valeur de la liste
print(joueurs_en_ligne[0])
# Afficher la derniere valeur de la liste
print(joueurs_en_ligne[len(joueurs_en_ligne) - 1])
# Afficher plusieurs valeurs dans une liste
print(joueurs_en_ligne[0:2])
# Modification de la valeur d'index 0 
joueurs_en_ligne[0] = "Arnette"
# Modification multiple
joueurs_en_ligne[0:2] = ["Arno", "Mod"]
# Insertion de la valeur Benard à l'index 1
joueurs_en_ligne.insert(1, "Bernard")
# Insertion d'une valeur en fin de ligne
joueurs_en_ligne.append("Floran")
# Insertion de plusieurs valeurs dans la liste
joueurs_en_ligne.extend(["Damien", "Tanguy"])
print(joueurs_en_ligne)

# Exemple d'utilisation: Le professeur des écoles

notes = [
    9, 10, 13,
    15, 4, 16
]
# On affiche la liste 
print(notes)
# On mélange notre liste
shuffle(notes)
# On raffiche la liste modifier
print(notes)

result = statistics.mean(notes)
print("La moyenne de l'élève est de: {}".format(result))

text = input("Entrer une chaine de la forme (email-pseudo-motdepasse)").split("-")
print(text)
print("Salut {}, ton email est {}, et ton mot de passe est {}".format(text[1], text[0], text[2]))