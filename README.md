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
On peut aussi commenter un bloc de code:
```py
"""
def bienvenue():
    print("Bienvenue")
    result = 5 + 6
    print("Le resultat est de :", result)
    
    
bienvenue()
"""
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
``Faire l'exercice 2``

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
``Faire l'exercice n°3``

---
## Les boucles
### La boucle for
``La boucle for`` permet de faire une instruction d'une valeur de départ jusqu'à une valeur d'arrivée:
```py
for NomDeVariable in range(ParametreDebut,ParametreFin):
    print(NomDeVariable)
```
On utilise le mot clé ``for`` pour lancé la boucle suivi du ``NomDeVariable`` que l'on implémente

Ensuite il nous faut le mot clé ``in`` suivi de la methode ``range(ParametreDebut,ParametreFin)`` pour endiqué l'interval dans lequel on implémente la variable.

Exemple :
```py
for i in range(1,5):
    print("Vous êtes le client n°", i)
```
Resultat:
```shell
Vous êtes le client n° 1
Vous êtes le client n° 2
Vous êtes le client n° 3
Vous êtes le client n° 4
```
Attention, le ``ParametreFin`` est exclus est n'est pas pris en compte

### La boucle for each
La boucle ``for each`` est une boucle ``for`` qui va fonctionner sur une liste

D'abord il nous faut donc une liste, ici dans notre cas, une liste de email
```py
emails = ["arnaud.fourmault@gmail.com", "arnaudf59@hotmail.fr", "arnaud.dev@gmail.com"]
``` 
Et grâce à la boucle ``for each``,on va pour faire plusieurs instruction en fonction du nombre d'entrée dans la liste
```py
for email in emails:
    print("Email envoyé à: ", email)
```
Resultat:
```shell
Email envoyé à:  arnaud.fourmault@gmail.com
Email envoyé à:  arnaudf59@hotmail.fr
Email envoyé à:  arnaud.dev@gmail.com
```

*il est possible de combiner des boucles et des conditions.*

Reprenons notre exemple d'email, mais au lieu d'envoyer un email à chaque valeur de la liste, on decide d'envoyer un mail qu'à certaines adresses, pour celà, on peut créer une liste des email non séléctionner 
```py
# Liste d'email
emails = ["arnaud.fourmault@gmail.com", "arnaudf59@hotmail.fr", "arnaud.dev@gmail.com", "arnaud.taf@gmail.com"]
# liste d'email blacklisté
blacklist = ["arnaud.dev@gmail.com", "arnaud.taf@gmail.com"]
```
Ensuite, on peut à l'intérieur de notre boucle faire une condition pour savoir si on envoi ou non un email
```py
for email in emails:
    if email in blacklist:
        print("Email {} interdit! envoi impossible".format(email))
    else:
        print("Email envoyé à: ", email)
```
resultat:
```shell
Email envoyé à:  arnaud.fourmault@gmail.com
Email envoyé à:  arnaudf59@hotmail.fr
Email arnaud.dev@gmail.com interdit! envoi impossible
Email arnaud.taf@gmail.com interdit! envoi impossible
```
Il est aussi possible d'utiliser le mot clé ``continue`` finir l'instruction est passé au champs de la liste suivante
```py
for email in emails:
    if email in blacklist:
        print("Email {} interdit! envoi impossible".format(email))
        continue
    
    print("Email envoyé à: ", email)
```
Resultat(Identique à l'autre methode):
```shell
Email envoyé à:  arnaud.fourmault@gmail.com
Email envoyé à:  arnaudf59@hotmail.fr
Email arnaud.dev@gmail.com interdit! envoi impossible
Email arnaud.taf@gmail.com interdit! envoi impossible
```
Il est aussi possible d'utiliser la mot clé ``break`` pour arrêter la boucle 
```py
for email in emails:
    if email in blacklist:
        print("Email {} interdit! envoi impossible".format(email))
        break
    
    print("Email envoyé à: ", email)
```
Resultat
```shell
Email envoyé à:  arnaud.fourmault@gmail.com
Email envoyé à:  arnaudf59@hotmail.fr
Email arnaud.dev@gmail.com interdit! envoi impossible
```
### La boucle while
La boucle ``while`` permet de créer une boucle jusqu'à se que l'on arrive au resultat souhaité

Prenons par exemple un salarié qui à un salaire
```py
salaire = 1500
```
On peux faire une boucle ``while`` sur cette variable
```py
while salaire < 2000:
    print("Votre salaire actuel est de ", salaire, "€")
```
Ici, la boucle while dit : ``Tant que le salaire est inférieur à 2000 faire``

Attention, ici, il s'agit comme on le dit **``boucle infinie``**, une boucle qui ne s'arrête jamais

On decide pour cette boucle, augmenter le salaire à chaque fois que l'on rentre dedans:
```py
while salaire < 2000:
    salaire += 120
    print("Votre salaire actuel est de ", salaire, "€")
```
Dans ce cas là, à chaque fois que l'on entre dans la boucle, on rajoute 120 a la variable salaire, jusqu'à se que l'on depasse la condition.
Resultat:
```shell
Votre salaire actuel est de  1620 €
Votre salaire actuel est de  1740 €
Votre salaire actuel est de  1860 €
Votre salaire actuel est de  1980 €
Votre salaire actuel est de  2100 €
```
---
``Faire les exercices 4 et 5``

---
## Les fonctions
### Pemiere fonction
Pour créer une fonction en python, on utilise le mot clé ``def``
```py
def nomFunction():
```
Dans une fonction, on peut y mettre autant d'instruction que l'on veut
Exemple de function:
```py
def bienvenue():
    print("Bienvenue")
    result = 5 + 6
    print("Le resultat est de :", result)
```
Ensuite pour utiliser la fonction, il faut l'appeler
```py
bienvenue()
```
Resultat:
```shell
Bienvenue
Le resultat est de : 11
```
On peut appeler autant de fois la fonction que l'on veut
```py
bienvenue()
bienvenue()
bienvenue()
```
Resultat (Le resultat s'affiche autant de fois qu'on l'appel):
```shell
Bienvenue
Le resultat est de : 11
Bienvenue
Le resultat est de : 11
Bienvenue
Le resultat est de : 11
```

### Fonction avec argument
Prenons par exemple une fonction qui permets de passer à l'année suivante

Commençons par créer une variable qui contient l'année
```py
annee = 2021
```
Puis notre fonction
```py
def anneeSuivante():
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)
```
Ici, la fonction ne retournera rien, car elle n'a pas accés à la variable ``annee``
Pour cela, il y a plusieurs solutions 
1. premiere solution, inséré la variable dans la fonction
```py
def anneeSuivante():
    annee = 2021
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)
```
Resultat:
```shell
Fin de l'année 2021
Début de l'année 2022
```
2. Methode 2
Pour cela la variable n'est pas dans la fonction, pour l'utiliser dans une function, on utilise le mot clé ``global``
```py
def anneeSuivante():
    global year
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)

year = 2021

anneeSuivante()
```
Resultat:
```shell
Fin de l'année 2021
Début de l'année 2022
```
### Utiliser une fonction dans une function
Une fonction peut aussi envoyer une valeur, permettant d'obtenir cette valeur dans une autre fonction

Pour monter tout ça, on va créer une fonction ``addition``
```py
def addition():
    result = 5 + 5
    return result
```
ici, dans notre fonction, on à une variable qui fait une addition, et on utilise le mot clé **``return``** pour permettre l'envoi de la variable ``result``

On peut récupérer et utiliser la methode pour obtenir ou afficher le resultat
Exemple : 
```py
print("le resultat du calcul est", addition())
```
Resultat
```shell
le resultat du calcul est 10
```
Il est possible d'afficher plusieurs fonction en même temps, imaginons une fonction qui permet d'afficher un message.
```py
def addition():
    result = 5 + 5
    return result

def message():
    return "le resultat du calcul est"

print(message(), addition())
```
Resultat:
```shell
le resultat du calcul est 10
```
### Fonction avec un paramêtre 
Un parametre est un valeur que l'on envoie à la fonction pour pouvoir l'utiliser dedans.
```py
def addition(n):
    return 5 + n
```
Ensuite on peut l'appeler en mettant entre paranthese la valeur de notre paramêtre
```py
print(message(), addition(4))
```
Resultat:
```shell
le resultat du calcul est 9
```
*Il est possible de mettre une valeur par default au cas ou aucun paramêtre n'est envoyé à la function*
```py
def addition(n = 6):
    return 5 + n

print(message(), addition(4))
print(message(), addition())
```
Resultat:
```shell
le resultat du calcul est 9
le resultat du calcul est 11
```
---
Faire l'exercice n°6

---
### La récursivité
C'est le cas ou une fonction peut s'appeler soit même
Pour commencer, créer une fonction ``add()`` qui permet de faire une addition
```py
def add(a):
    a += 1
    print(a)
    
add(12)
```
Resultat:
```shell
13
```
Dans cette fonction, il est possible dans la fonction, il est possible d'appeler la fonction add() dans la fonction add() et incit créer une boucle
```py
def add(a):
    a += 1
    print(a)
    add(a)
    
add(12)
```
Cela créer une boucle infini, pour eviter celà, il faut mettre un condition dedans la fonction
```py
def add(a):
    a += 1
    print(a)
    if a < 20:
        add(a)
    
add(12)
```
Resultat:
```shell
13
14
15
16
17
18
19
20
```
---
Faire l'exercice n°7

---


