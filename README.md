# Python-bases

## Installation
Installer python sur le site ``www.python.org``

Installer les extensions visual studio ``python``

## Premier fichier
Créer un fichier ``HelloWorld.py``

dans le ficher mettre:
```py
print("Hello world")
```
Pour l'excuter soit cliquer sur le triangle en au à droite du fichier

Soit dans un terminal faire
```shell
python .\HelloWorld.py
```

## Commenter le code

Pour commenter le code, il suffit de mettre un # devant le code que l'on veut commenter
```py
# print("Hello world")
```
## Les Variables

il existe plusieurs type de variable.

-   Les chaine de carractère:
```py
# Création d'un variable string
    username = "Arnaud"
    print(username)
```
resultat:
```shell
Arnaud
```
-   Les Entiers:
```py
# Création d'une variavle int
    age = 30
    print(age)
```
resultat:
```shell
30
```
-   Les Floats:
```py
# Création d'une variavle float
    portfeuille = 125.7
    print(portfeuille)
```
resultat:
```shell
125.7
```
-   Les Floats:
```py
# Création d'une variavle booleen
    is_happy = True
    print(is_happy)
```
resultat:
```shell
True
```

Il est possible aussi d'afficher plusieurs variables dans le même ``print``
```py
print(username, age, portfeuille, is_happy)
```
Resultat:
```shell
Arnaud 30 125.7 True
```
On peut evidement modifier la valeur d'une variable
```py
age = 30
print(age)
age = 31
print(age)
```
Resultat:
```shell
30
31
```
On peut modifier une variable avec une opération
```py
age = age + 1
```
Resultat:
```shell
32
```
On peut utiliser les variable pour en faire un phrase
```py
print("Salut " + username)
```
resultat:
```shell
Salut Arnaud
```
Attention, on ne peux pas concaténer un entier, de ce fait, on peux pas faire:
```py
print("Salut " + username + ", vous avez " + age + " ans")
```
Cela nous renverra une erreur, pour le faire il faux transformer la variable ``age`` en chaine de caractère
```py
print("Salut " + username + ", vous avez " + str(age) + " ans")
```
resultat:
```shell
Salut Arnaud, vous avez 30 ans
```
## Premier programme (Le calcul de moyenne)
Tout d'abord, il va falloir demander à l'utilisateur d'entrer des note, pour cela, on utilise la methode ``input()``
```py
note1 = input("Entrer la premiere note")
```
La méthode input renvoi une chaine de caractère, le problème c'est que pour calculer une moyenne, il nous faut des nombres, pour cela, il faut modiifer la chaine récupérer en entier. Pour cela, on utilise la methode ``int()``
```py
# Récupérer une premiere variable
note1 = int(input("Entrer la premiere note"))
```
Une fois que l'on a recupéré les variables notes, il faut calculer la moyenne:
```py
result = (note1 + note2 + note3) /3
```
Puis on l'affiche, pour cela , il ne faut pas oublier de modifier la variable ``result`` en **chaîne de caractère**
```py
print("La moyenne est de:" + str(result))
```
On peut afficher la variable sans la transformer en chaine, pour cela, au lieu de faire une concaténation avec un ``+``, on peut la faire avec une ``,``
```py
print("La moyenne est de:", result)
```
résultat:
```shell
La moyenne est de: 10
```

---
**``Faire l'exercie n°1``**

---

## Les conditions

### premiere condition
Une condition permet d'envoyer un résultat en fonction du resultat obtenu

Ici, nous allons créer un porte feuille et un produit à acheter
```py
portemonnaie = int(input("De combien d'argent disposez-vous?"))
prix_produit = 900
```
On va ensuite créer une condition pour savoir si l'on peut acheter ce produit

Pour cela, il faut d'abord créer notre condition, on commence pour cela par créer notre ``if`` afin de vérifier si notre condition est bonne ou pas
```py
if prix_produit <= portemonnaie:
    print("Vous achetez ce produit")
```
Ensuite, il faut créer la condition si jamais la conditions n'est pas vérifié, pour cela on utilise le mot ``else``
```py
else:
    print("Vous ne pouvez pas acheter ce produit")
```
On peut aussi, si jamais on achete le produit, recalculer la variable ``portefeuille``

On peut utiliser la methode **``format``** pour insérer une valeur dans notre chaine de caractère
```py
portemonnaie -= prix_produit
print("Vous disposez désormé de: {}€".format(portemonnaie))
```
Il est aussi posible de faire un multi-condition, pour cela, on utilise le mot clé ``and`` pour dire que les deux condition doivent être vrai pour suivre les instructions, ou le mot clé ``or`` pour dire que l'une des deux conditions doit être vrai pour poursuivre les instructions 

exemple and: 
```py
if prix_produit <= portemonnaie and prix_produit < 1000:
    print("Vous achetez ce produit")
```
exemple or: 
```py
if prix_produit <= portemonnaie or prix_produit < 1000:
    print("Vous achetez ce produit")
```
Il est posiible de simplifier les conditions en utilisant les conditions ternaire:
```py
text = ("L'achat est possible", "L'achat est impossible")[prix_produit <= portemonnaie]
print(text)
```
### Condition pour la verif d'un password
Pour cela, nous allons créer deux variables
```py
password = input("Entrer votre mot de passe:")
password_length = len(password)
```
la methode ``len()`` permet de savoir le nombre de caractère d'une variable

On peut donc vérifier si le password posséde bien le nombre de caractère minimun requis
```py
if password_length <= 8:
    print("Mot de passe trop court")
else:
    print("Mot de passe moyen")
```
On peut aussi rajouter une condition intermédiaire pour rajouter une condition en plus
```py
if password_length <= 8:
    print("Mot de passe trop court")
elif password_length > 8 and password_length <= 12:
    print("Mot de passe moyen")
else:
    print("Mot de passe parfait")
```
---
Faire l'exercice 2

---
## Les listes
### Création d'une listes
On va Créer une liste qui va stocker des pseudos pour simuler un jeu en ligne:

Pour créer une liste on mets nos valeurs dans des crochets ``[]``
```py
joueurs_en_ligne = ["Arnaud", "Maud", "Christelle"]
print(joueurs_en_ligne)
```
resultats: 
```shell
['Arnaud', 'Maud', 'Christelle']
```
On peut trouver une valeur précise grace à l'indice 

Attention, l'indice d'un tableau comme à **``0``**
```py
print(joueurs_en_ligne[0])
```
resultat:
```shell
Arnaud
```
On peut trouver la derniere valeur de la liste:
```py
print(joueurs_en_ligne[len(joueurs_en_ligne) - 1])
```
resultat:
```shell
Christelle
```
On peut aussi selectionner une partie de la liste
```py
print(joueurs_en_ligne[0:2])
```
resultat
```shell
['Arnaud', 'Maud']
```
On peut aussi créer une liste d'une autre méthode, grâce à la methode ``split()`` 
```py
text = input("Entrer une chaine de la forme (email-pseudo-motdepasse").split("-")
print(text)
print("Salut {}, ton email est {}, et ton mot de passe est {}".format(text[1], text[0], text[2]))
```
resultat:
```shell
['arnaud.fourmault@gmail.com', 'arnaudf59', 'arnaud276600']
Salut Arnaudf59, ton email est arnaud.fourmault@gmail.com, et ton mot de passe est arnaud276600
```
### Modifier une liste
On peut modifier une valeur d'une liste comme pour une variable
```py
joueurs_en_ligne[0] = "Arnette"
```
Modification multiple
```py
joueurs_en_ligne[0:2] = ["Arno", "Mod"]
```
resultat:
```shell
['Arno', 'Mod', 'Christelle']
```
On peut rajouter **``une``** valeur en fin de liste
```py
joueurs_en_ligne.append("Floran")
```
resultat:
```shell
['Arno', 'Mod', 'Christelle', 'Floran']
```
Ou rajouter **``plusieurs``** valeurs en fin de liste
```py
joueurs_en_ligne.extend(["Damien", "Tanguy"])
```
resultat:
```shell
['Arno', 'Mod', 'Christelle', 'Damien', 'Tanguy']
```
On peut aussi ajouter une valeur à la liste à un endroit choisi
```py
joueurs_en_ligne.insert(1, "Bernard")
```
Le ``1`` correspond à l'index de la liste ou l'on veux inserer la valeur ``Bernard``

#### Supprimer une valeur dans une liste
Pour retirer une valeur dans une liste il y a trois posibilités
1. Methode 1
```py
del joueurs_en_ligne[1]
```
2. Methode 2 (similaire à la méthode 1)
```py
joueurs_en_ligne.pop(1)
```
3;  Methode 3 (modification par le nom)
```py
joueurs_en_ligne.remove("Arnaud")
```
#### Supprimer toutes la liste
La encore, il y a deux methodes:
1. Methode 1
```py
del joueurs_en_ligne[:]
```
2. Methode 2
```py
joueurs_en_ligne.clear()
```
## Les modules
En python, on peut importer des modules pour nous permettre d'utiliser des fonnctions pour nous faciliter la vie

Pour importer un module, il faut au debut du fichier, l'importer:
```py
import NomDuModule
```
On peut aussi, seulement importer une seule function d'un module, pour cela on l'importe de cette façon
```py
from NomDuModule import NomFunction
```
1. Exemple de module, le module ``statistics`` qui permet de faire des calcul, comme la moyenne
```py
import statistics

notes = [
    9, 10, 13,
    15, 4, 16
]
result = statistics.mean(notes)
print("La moyenne de l'élève est de: {}".format(result))
```
2. Autre exemple de module pratique, le module ``random`` et sa fonction shuffle()

D'abord, on l'importe:
```py
from random import shuffle
```
Puis on peut l'utiliser
```py
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
```
resultat:
```shell
[9, 10, 13, 15, 4, 16]
[15, 9, 10, 16, 13, 4]
```
---
Faire l'exercice n°3

---




