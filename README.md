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
``Faire l'exercice n°6``

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
``Faire l'exercice n°7``

---
## Les Objets
Pour créer un objet, il faut d'abord, créer une **``class``**
Expemple de class:
```py
class Player:
```
Dans une class, on va d'abord y mettre des attribut:
```py
class Player:
    
    pseudo = "Arnaud"
    pv = 20
    attaque = 3
```
Après avoir créer la srtucture, il va falloir l'utiliser, pour celà, on va créer une nouvelle variable qui va appeler notre classe
```py
player1 = Player()
```
Ensuite, on peut donc utiliser notre variable
```py
print("Bienvenue au joueur", player1.pseudo)
```
Resultat
```shell
Bienvenue au joueur Arnaud
```
Ici, notre class est static, se qui n'est pas très pratique, car l'on veut créer un moule, il ne faut pas se limiter à une seule valeur par variable, et pour répondre a cette problematique, on va utiliser un ``constructeur``

Le constructeur est une nouvelle fonction

La fonction s'appelle **``__init__``** et c'est la premiere qui va s'ignitialiser quand on va créer une nouvelle instance de l'objet en question

Entre paranthese, il y a un premier parametre qui va se généré automatiquement qui s'appelle ``self``, c'est une sorte de mini bdd dans lequel, on va pouvoir injecter le autre parametre

En plus de ce paramêtre, on peut rajouter d'autre paramêtre et les injecter dans le parametre self
```py
def __init__(self, pseudo, pv, attaque):
    self.pseudo = pseudo
    self.pv = pv
    self.attaque = attaque
```
on peut aussi, rajouter un message qui s'affiche a chaque instance de notre ``Objet``
```py
class Player:
    
    def __init__(self, pseudo, pv, attaque):
        self.pseudo = pseudo
        self.pv = pv
        self.attaque = attaque
        print("Bienvenue au joueur", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
```
On peut ensuite instancié notre objet et voir le resultat
```py
class Player:
    
    def __init__(self, pseudo, pv, attaque):
        self.pseudo = pseudo
        self.pv = pv
        self.attaque = attaque
        print("Bienvenue au joueur", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
    
player1 = Player("Arnaud", 20, 3)
```
Resultat
```shell
Bienvenue au joueur Arnaud / Point de vie : 20 / Attaque :  3
```
### Intérragir avec notre objet
C'est a ce moment que vont entrer en jeu, **les methodes**

Qu'est ce qu'une methode?

C'est une fonction qui est attibué à une **``class``**

Il y a plusieurs types de methode
1. Les getteurs, qui vont permettre de récupérer des informations
```py
def get_pseudo(self):
    return self.pseudo
```
On peut donc maintenant l'appeler
```py 
print("Pseudo:", player1.get_pseudo())
```
Resultat:
```shell
Pseudo: Arnaud
```
2. Les setteurs, qui permet de changer des valeurs
```py
def dommage(self, dommage):
    self.pv -= dommage
    print("Aie... vous venez de subir", dommage, "dégats !")

player1.dommage(4)
print("Pseudo:", player1.get_pseudo(), "PV:", player1.get_pv())
```
Resultat:
```shell 
Aie... vous venez de subir 4 dégats !
Pseudo: Arnaud PV: 16
```
3. On peut aussi créer une methode setteur qui en appelle une autre:
```py
def dommage(self, dommage):
    self.pv -= dommage
    print("Aie... vous venez de subir", dommage, "dégats !")
        
def attaque_player(self, target_player):
    target_player.dommage(self.attaque)

player1 = Player("Arnaud", 20, 3)
player2 = Player("Maud", 20, 1)

print(player1.get_pseudo(), "attaque", player2.get_pseudo())
player1.attaque_player(player2)
print("Bienvenue au joueur", player1.get_pseudo(), "/ Point de vie :", player1.get_pv(), "/ Attaque : ", player1.get_attaque())
print("Bienvenue au joueur", player2.get_pseudo(), "/ Point de vie :", player2.get_pv(), "/ Attaque : ", player2.get_attaque())
```
Resultat:
```shell
Bienvenue au joueur Arnaud / Point de vie : 20 / Attaque :  3
Bienvenue au joueur Maud / Point de vie : 20 / Attaque :  1
Arnaud attaque Maud
Aie... vous venez de subir 3 dégats !
Bienvenue au joueur Arnaud / Point de vie : 20 / Attaque :  3
Bienvenue au joueur Maud / Point de vie : 17 / Attaque :  1
```

On peut deplacer notre ``class`` dans un autre fichier, et ensuite l'importer dans le fichier dont on a besoin d'utiliser cette class

Dans le fichier LesObjets.py mettre l'import, qui importe la class ``Player()`` dans le fichier ``Players.py`` qui se trouve dans le dossier ``Class``
```py
from Class.Players import Player
```
---
``Faire l'exercice n°8``

---
## L'héritage
En **programmation orientée objet**, l'héritage est un mécanisme qui permet, lors de la déclaration d'une nouvelle classe, d'y inclure les caractéristiques d'une autre classe.

Prenez par exemple un ville, qui posséde plusieurs rue, dans chaque rue il y a plusieurs construction:

1. Un immeuble qui est carractérisé par une adresse, un nombre d'étage, et un nombre de balcon
2. Ensuite, on a un Supermarché qui posséde une adresse, un nombre d'étage, et un nombre de rayon
3. Et enfin, une banque, qui est caractérisé elle par une adresse, un nombre d'étage, un nom et un nombre de coffre

On peut constater que chaque construction posséde des caractéristique identique comme l'adresse ou le nombre d'étage

Pour eviter la redondance du code, on peut imaginer une super class Batiment qui posséderai de ses attribut, et des class fils qui hériterai de cette class en plus de leurs attribut dédié.

Pour notre exemple, on va reprendre la class Player du cours sur l'objet, et on va créer une nouvelle ***class Guerrier***

On lui rajoute des attribut et des methode propre a cette class
```py
class Guerrier:
    
    def __init__(self, pseudo, pv, attaque):
        self.pseudo = pseudo
        self.pv = pv
        self.attaque = attaque
        #On rajoute un attribut armure pour la class armure
        self.armure = 3
        print("Bienvenue au guerrier", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_pv(self):
        return self.pv
    
    def get_attaque(self):
        return self.attaque
    
    # Une methode get pour récupérer les point d'armure
    def get_armure(self):
        return self.armure
    
    # On modifie la methode dommage pour inséré les point d'armure
    def dommage(self, dommage):
        
        # Si un guerrier a des points d'armure, il en perd 1 et ne subit pas de dégât
        if self.armure > 0:
            self.armure -= 1
            dommage = 0
            
        self.pv -= dommage
        print("Aie... vous venez de subir", dommage, "dégats !")
        
    def attaque_player(self, target_player):
        target_player.dommage(self.attaque)
        
    # On rajoute une methode pour recharger les points d'armure
    def recharge_armure(self):
        self.armure = 3
```
Ensuite, le fichier ``Lheritage``, on peut importer cette class et verifier nos methode
```py
from Class.Player import Player
from Class.Guerrier import Guerrier

player = Player("Arnaud", 20, 5)
warrior = Guerrier("DarkWarrior", 30, 2)
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
warrior.dommage(4)
print("vie:", warrior.get_pv(), "armure:", warrior.get_armure())
```
Resultat:
```shell
Bienvenue au joueur Arnaud / Point de vie : 20 / Attaque :  5
Bienvenue au guerrier DarkWarrior / Point de vie : 30 / Attaque :  2
Aie... vous venez de subir 0 dégats !
vie: 30 armure: 2
Aie... vous venez de subir 0 dégats !
vie: 30 armure: 1
Aie... vous venez de subir 0 dégats !
vie: 30 armure: 0
Aie... vous venez de subir 4 dégats !
vie: 26 armure: 0
```
On remarque bien que le guerrier perds des point d'armure, et lorsqu'elle est à 0, il commence à perdre des point de vie

Pour créer le *class Gierrier*, on a dupliqué la *class Player*.

Quand on parle d'héritage, on va retirer les doublon de la class Guerrier(class enfant) pour éviter la redondance du code et utiliser la class Player(class parent) pour lui transmettre

Pour cela, on va précisser que la *class Guerrier* est ``une specification`` de la *class Player*
```py
class Guerrier(Player):
```
Ensuite, on supprime le code doublons dans le class Guerrier, qui se trouve déjà dans la class Player
```py
from Class.Player import Player

class Guerrier(Player):
    
    def __init__(self, pseudo, pv, attaque):
        self.armure = 3
        print("Bienvenue au guerrier", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
    
    # Une methode get pour récupérer les point d'armure
    def get_armure(self):
        return self.armure
    
    # On modifie la methode dommage pour inséré les point d'armure
    def dommage(self, dommage):
        pass  
        
    # On rajoute une methode pour recharger les points d'armure
    def recharge_armure(self):
        self.armure = 3        
```
On utilise pour le moment le mot clé ``pass`` dans la méthode ``dommage()`` afin de signaler que la méthode pour le moment n'a pas de code mais ne renvoi pas d'erreur

Ensuite, il faut modifier le constructeur pour lui dire les élément qu'il doit récupérer de la *class Player*, pour cela, on utilise le mot clé ``super()`` suivi de la fonction ``__init__`` du constructeur parent suivi des attribut que l'on veut récupérer
```py
def __init__(self, pseudo, pv, attaque):
    super().__init__(pseudo, pv, attaque)
    self.armure = 3
    print("Bienvenue au guerrier", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
```
On peut remplacer le mot clé ``super()`` par le nom de la class Parent 
```py
def __init__(self, pseudo, pv, attaque):
    Player.__init__(pseudo, pv, attaque)
    self.armure = 3
    print("Bienvenue au guerrier", pseudo, "/ Point de vie :", pv, "/ Attaque : ", attaque)
```
Après avoir récupérer c'est attribut, on peut refaire *la methode dommage()* de la *class Guerrier*
```py
def dommage(self, dommage):
    if self.armure > 0:
        self.armure -= 1
        dommage = 0
    # Pour utiliser la methode dommage de la class Player, on utilise une nouvelle fois le methode super()     
    super().dommage(dommage)
```
Il est possible de vérifier si une class est bien l'enfant d'une class parent, pour cela on utilise la methode ``issubclass(classEnfant, classParent)``
```py
if issubclass(classEnfant, classParent):
    print("La classEnfant est bien une spécialisation de la classParent")
```
## Interface graphique
La premiere des choses à faire pour utiliser une interface graphique est d'avoir un support ou on va placer nos différents éléments, comme par exemple une fenêtre.

Pour cela on va utiliser un module qui s'appelle **``tkinter``** 

Pour créer une fenêtre avec **``tkinter``**, il faut d'abord **l'importer**
```py
from tkinter import *
```
Puis, il faut créer une variable qui va contenir l'instance de la fenêtre
```py
# Création d'une fenêtre
window = Tk()
```
Et enfin, il faut l'afficher
```py
# afficher
window.mainloop()
```
Cela nous affiche la fenêtre de base de tkinter

On peut modifier le titre, ou la taille de la fenêtre par exemple
```py
# Titre de la fenêtre
window.title("Interface Graphique")
# Taille de la fenêtre
window.geometry("1080x720")
```
``geometry()`` prend en valeur une chaine, correspondant a la taille en pixel de la fenêtre souhaité

Il est généralement recommander de mettre une taille minimun a cette fenêtre
```py
window.minsize(480, 360)
```
Maintenant, on va modifier la petite icon pour cela, il va falloir ajouter une petite ressource, pour ce faire, il faut prendre l'image de son choix et il va falloir la convertire en **``.ico``**

Site pour convertire : https://convertio.co/fr/png-ico/

On vient ensuite le mettre dans notre projet, et on peut donc la rajouter dans notre application
```py
# Icon de le fenêtre
window.iconbitmap(r'C:\dev\projet\Python-bases\les-bases\InterfaceGraphique\logo.ico')
```
Dernière petite modification, la couleur de fond de notre fenêtre
```py
# Modification du fond de notre fenêtre
window.config(background='#41B77F')
```
### Premier composant (le texte)
Pour insérer du texte, on va commencer par créer une variable qui va **porter** ce composant, puis, on va utiliser le mot clé ``Label`` et lui preciser que ce texte doit être afficher sur la *fenêtre* puis le *contenu* du texte
```py
label = Label(window, text = "Bienvenue sur l'appication")
```
Ensuite, il faut lui dire de l'insérer
```py
label = Label(window, text = "Bienvenue sur l'appication")
label.pack()
```
Le texte qui apparait sur cette fenêtre est de ``taille`` standard, et ne posséde pas le ``background`` de la fenêtre

On va commencer par modifier la font de notre text (taille et police)
```py
Label(window, text = "Bienvenue sur l'appication", font=("Courrier", 40))
```
Ensuite, on va modifier la couleur d'arrière plan et la couleur du texte
```py
label = Label(window, text = "Bienvenue sur l'appication", font=("Courrier", 40), bg='#41B77F', fg='#FFFFFF')
```
On peut aussi positionner le texte en modifiant l'insertion du composant
```py
label.pack(side=POSITION)
```
Exemple de position: **LEFT**,**BOTTOM**,**RIGHT**,**TOP**

On peut aussi le centrer en lui mettant une expension
```py
label.pack(expand=YES)
```
On va créer un sous titre à notre premier composant
```py
#premier composant
label = Label(window, text = "Bienvenue sur l'appication", font=("Courrier", 40), bg='#41B77F', fg='#FFFFFF')
label.pack(expand=YES)

# Ajouter un sous titre
sub_label = Label(window, text = "Comment allez vous?", font=("Courrier", 25), bg='#41B77F', fg='#FFFFFF')
sub_label.pack(expand=YES)
```
Les deux textes sont bien afficher sur notre fenêtre, cependant cette méthode n'est pas vraiment bonne. Il est préférable de créer une ``Frame``

Une ``frame`` est une sorte de boite dans laquelle on va placer nos éléments que l'on placera après dans notre fenêtre

Pour cela avant les deux composant, on va créer notre frame en utilisant le mot clé ``Frame()``, on va lui dire ou elle se situe, et la couleur d'arrière plan
```py
frame = Frame(window, bg='#41B77F')
```
Ensuite, on va modifier nos objets, au lieu d'afficher nos élément dans la fenêtre, on va l'afficher dans notre ``frame``

Puis on va afficher notre *frame* comme pour nos element avec le mots clé ``pack()`` et c'est la *frame* que l'on va etendre pour le positionner au milieu

```py
# frame
frame = Frame(window, bg='#41B77F')

#premier composant
label = Label(frame, text = "Bienvenue sur l'appication", font=("Courrier", 40), bg='#41B77F', fg='#FFFFFF')
label.pack()

# Ajouter un sous titre
sub_label = Label(frame, text = "Comment allez vous?", font=("Courrier", 25), bg='#41B77F', fg='#FFFFFF')
sub_label.pack()

# Afficher notre frame
frame.pack(expand=YES)
```
Les éléments sont bien centrés, mais va frame elle n'est pas visivle, c'est un bloc qui n'est pas afficher

On peut l'afficher en rajoutant de nouveau paramêtre à notre frame, une bordure et un relief pour l'afficher et la faire resortir de la fenêtre
**Bordure en relief**:
```py
frame = Frame(window, bg='#41B77F', bd=1, relief=SUNKEN)
```
**Bordure Classique**:
```py
frame = Frame(window, bg='#41B77F', bd=1, relief=SOLID)
```
### Les boutons
Pour l'exemple on va créer un bouton lien vers une page internet

Pour créer un bouton, c'est le même principe que pour pour créer du texte, mais au lieu d'utiliser le mot clé **``Label``** on va utiliser le mot clé **``Boutton``**
```py
button_github = Button(frame, text="Ouvrir Git Hub", font=("Courrier", 25), fg='#41B77F', bg='#FFFFFF')
button_github.pack()
```
On peut modifier notre bouton, par exemple, on va lui mettre une *marge*, et faire en sorte que le bouton prenne toute la *largeur de la frame en X*
``py
button_github.pack(pady=25, fill=X)
``
On en a fini avec l'aspect design de notre fenêtre, maintenant, on va s'attaquer à l'aspect logique

Comment faire pour intérragir avec notre boutton
### Intérragir avec le boutton (Lien)
Pour commencer, on va d'abbord importer un nouveau module

**``webbrowser``**, permet d'ouvrir des page internet de faire tout un tas de choses avec cela
```py
import webbrowser
```
Ensuite, on va créer une function pour ouvrir un navigateur
```py
def open_github():
    webbrowser.open_new("https://github.com/Arnaudf59")
```
Et pour dire a notre bouton d'ouvrir le navigateur, on va rajouter une nouvelle propriété à notre bouton, la propriété ``command``:
```py
button_github = Button(frame, text="Ouvrir Git Hub", font=("Courrier", 25), fg='#41B77F', bg='#FFFFFF', command=open_github)
```
### Intérragir avec le boutton (générateur de mot de passe)
Pour commencer, on va créer un nouveau ficher python, *pass_generator*. On va créer une nouvelle fenêtre dans ce fichier
```py
from tkinter import *

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("logo.ico")
window.config(background="#4065A4")

window.mainloop()
```
On dispose donc de notre fenêtre, à gauche, on va mettre une image pour representer le mecanisme du générateur, alors qu'a droite, on va mettre tous ce qui est titre, bouton ect
#### Création de l'image
D'abord, choisir une image: https://www.flaticon.com/

et de la mettre dans notre projet

Et ensuite, on va créer une premiere section ou l'on va mettre les instructions pour généré un ``canvas``, c'est une zone dans laquelle on va dessiner l'image qui aura une certaine taille et certaine propriété
```py
width = 300
height = 300
img = PhotoImage(file="password.png")
```
On peut personnaliser notre image par exemple en zoomant ou en dezoomant notre image
```py
img = PhotoImage(file="password.png").zoom(35)
```
On peut aussi lui rajouter un parterne
```py
img = PhotoImage(file="password.png").zoom(35).subsample(32)
```
Ensuite, on va créer notre canvas (espace ou on peut dessiner des composaant graphique).
```py
canvas = Canvas(window, width=width, height=height, bg="#4065A4")
```
Grace a ce canvas, on va pourvoir créer notre image dans ce canvas puis l'afficher
```py
canvas.create_image(width/2, height/2, image=img)
canvas.pack(expand=YES)
```
Le canvas et l'image s'affiche dans la fenêtre, le canvas est le bloc qui contient l'image, il estpossible de retirer la bordure en rajoutant les attributs:
```py
canvas = Canvas(window, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
```
Ensuite, nous allons créer nos boite pour pouvoir positionner nos éléments
```py
frame = Frame(window, bg="#4065A4")
```
Ensuite, on va modifier notre canvas pour le mettre dans cette frame
```py
Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
```
puis on affiche notre frame
```py
canvas.pack()
frame.pack(expand=YES)
```
on va aussi rajouter un titre
```py
titre = Label(frame, text="Générer un mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
titre.pack()
```
On va ensuite positionner nos éléments
### Le grillage
Pour pouvoir positionner nos élement, il faut remplacer le mot clé ``pack`` par le mot clé ``grid`` 

**grid** prend 3 options, row (la ligne), column (la colonne) et sticky (pour positionner notre objet (nord, est oest, sud))
```py
canvas.grid(row=0, column=0, sticky=W)
titre.grid(row=0, column = 1, sticky=W)
```
Ensuite on va créer un deuxieme frame pour y mettre nos nouveau élément, c'est une sous frame de la frame principale
```py
frame_droite = Frame(frame, bg="#4065A4")
```
On créer donc une nouvelle frame dans la premiere frame, puis on va y mettre le titre dedans, puis l'afficher dedans. Enfin, on va faire le grid non pas sur le titre, mais sur la deuxieme frame
```py
titre = Label(frame, text="Générer un mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
titre.pack()

frame_droite.grid(row=0, column = 1, sticky=W)
```
On va ensuite pour créer notre champs (``input``) pour pouvoir injecter le mot de passe généré. Pour cela, on va utiliser l'entrée ``Entry`` pour créer un input
```py
input_genere = Entry(frame_droite, font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
input_genere.pack()
```
Puis il nous manque plus que le dernier composant qui est le bouton pour générer le mot de passe
```py
button_genere = Button(frame_droite, text="Générer", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
button_genere.pack(fill=X)
```
Parfait, nous avons donc notre fenêtre et tous les élément dont on a besoin, maintenant, il va falloir créer notre fonction pour générer notre mot de passe
### Fonction de génération de mot de passe
On va tout d'abord importer un nouveau module, le module ``string`` de python ainsi que le module ``random``
```py
import string
from random import randint, choice
```
Puis on va créer notre fonction ainsi que plusieurs variable, la taille min de mot de passe, la taille minimun, ainsi que les caractère à utiliser

Pour cela, on va utiliser le module string que l'on vient d'installer
```py
def generate_password():
    taille_min = 6
    taille_max = 15
    all_caractère = string.ascii_letters + string.punctuation + string.digits
```
- **string.ascii_letters** permet de prendre tout l'alphabet
- **string.punctuation** permet de prendre toute les poctuations
- **string.digits** permet de prendre tout les chiffres

Ensuite, on créer notre boucle, pour cela, on va utilser la fonction ``randint()`` pour choisir aléatoirement le nombre de caractère du mot de passe
```py
for x in range(randint(taille_min, taille_max)):
```
Puis on utilise la fonction ``choice`` de random pour choisir aléatoirement un caractère  
```py
for x in range(randint(taille_min, taille_max)):
        choice(all_caractère)
```
Enfin, il faut récuperer notre reponse. Pour cela, en python il est posible de mettre la boucle for dans une variable, de plus on va concaténer chaque caractère pour généré notre mot de passe
```py
password = "".join(choice(all_caractère) for x in range(randint(taille_min, taille_max)))
```
Il ne nous reste plus qu'à afficher le mot de passe dans champs.

Pour cela, on va recupérer notre input créer un peu plus tôt et vider le champs, puis on va remplir le champs avec le mot de passe générer
```py
input_genere.delete(0, END)
    input_genere.insert(0, password)
```
et enfin, il faut appeler cette fonction lorsque l'on clique sur notre bouton, pour cela, on rajoute l'attribut ``command`` à notre bouton
```py
button_genere = Button(frame_droite, text="Générer", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF', command=generate_password)
button_genere.pack(fill=X)
```
## La barre de menu
Pour créer un menu, il faut d'abbord créer un nouvel instance de menu
```ts
menu_bar = Menu(window)
```
Puis on va créer un nouveau sous menu
```py
file_menu = Menu(menu_bar, tearoff=0)
```
l'attribut ``tearoff`` permet de retirer les décorations de liste.
Puis il faut mettre les option disponible dans se sous menu
```py
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
```
Et il nous reste plus qu'à afficher le menu en cascade
```py
menu_bar.add_cascade(label="Fichier", menu=file_menu)
```
Et on dit à notre fenêtre d'utiliser notre menu
```py
window.config(menu=menu_bar)
```
## Les documents
### L'insertion
En python , il est possible d'enregistrer sur l'ordinnateur des données pour les stocker même quand l'application n'est plus en utiliser

Pour créer un nouveau document, on va utiliser la fonction ``open()`` de python, qui va nous demander deux arguments, premièrement le nom du fichier que l'on veux créer ou le nom du fichier avec lequel on veut intérragir et deuxiemement qui va être le mode d'ouverture du fichier
```py
open('NonDuFichier', 'MethodeDouverture')
```
| code | Mode d'ouverture |
|:----------|------:|
|"r"| lecture seule | 
|"w"| écriture seule | 
|"a"| mode d'ajout | 
|"r+"| lecture et écriture | 
|"w+"| lecture et écriture, avec suppression du contenu au préalabl | 
|"a+"| ajout en lecture / écriture à la fin. | 

On constate qu'un nouveau fichier viens de se créer.

Maintenant, on va rejouter du contenu dans ce même fichier. Pour cela il faut récupérer un ce fichier, par exemple dans une variable, qui comporterai l'ouverture et le contenu de ce document
```py
file = open('etudiants.txt', 'w+')
```
Maitenant, il est possible d'utiliser la fonction ``write()`` qui nous permet d'écrire du text
```py
file = open('etudiants.txt', 'w+')
file.write("Arnaud")
file.write("Maud")
file.write("Thomas")
```
Après avoir écrit dans notre document, il faut maintenant le fermer
```py
file.close()
```
Du coup, on obtient 
```py
file = open('etudiants.txt', 'w+')
file.write("Arnaud")
file.write("Maud")
file.write("Thomas")
file.close()
```
Résultat dans le fichier etudiant.txt
```
ArnaudMaudThomas
```
pour rajouter le saut de ligne à la fin d'une insertion, il faut rajouter le ``\n`` à la fin d'une insertion
```py
file.write("Arnaud\n")
```
Resultat dans le fichier etudiant.txt
```
Arnaud
Maud
Thomas
```
Il est possible d'utiliser une autre méthode pour modifier notre ficher

Pour cela, on va utiliser le mot-clé **``with``** qui en python permet le contexte de ce que l'on a après, *dans notre cas, le document*, puis le mot clé ``as`` pour definier comment on va appeler ce context
```py
with open('etudiants.txt', 'w+') as file:
    file.write("Arnaud\n")
    file.write("Maud\n")
    file.write("Thomas\n")
    file.close()
```
Résultat dans le fichier etudiants.txt
```
Arnaud
Maud
Thomas
```
Pour éviter de devoir entrer un par un les entrées, il est possible de créer une boucle pour pouvoir insérer des noms à la pelle
```py
etudiants_liste = ["Arnaud", "Maud", "Thomas", "Floran", "Yannick", "Manu", "Juliette"]

with open('etudiants.txt', 'w+') as file:
    for etudiant in etudiants_liste:
        file.write(etudiant + "\n")
    file.close()
```
Resultat dans le fichier ``etudiant.txt``
```
Arnaud
Maud
Thomas
Floran
Yannick
Manu
Juliette
```
### La lecture 

Maintenant que l'on a vu la modification, l'on va voir maintenant un seconde context, la lecture de fichier. Pour cela, on va créer un nouveau fichier repas, et l'on créer un petit module pour choisir aléatoirement le rapas que l'on va manger.
```py
repas_liste = ["kebab", "mcdo", "japonais", "chinois", "thai", "poulet frites", "crepes", "omelette", "kfc", "tacos"]

with open('repas.txt', 'w+') as file:
    for repas in repas_liste:
        file.write(repas + "\n")
    file.close()
```
pour le lire , on va faire comme tout à l'heure, on va utiliser la function ``open()`` avec l'argument ``r+`` pour la lecture
```py
with open("repas.txt", "r+") as file:
    print(file.readline())
    file.close()
```
Pour éviter une erreur dans le choix du fichier suite à un erreur de saisi, il est possible de faire un controle pour être sur que le fichier choisi est existe bien. pour cela, on va importer le module ``os``
```py
import os
if os.path.exists("repas.txt"):
    with open("repas.txt", "r+") as file:
        print(file.readline())
        file.close()
else:
    print("Le document n'existe pas ! Attention !")
```
Ensuite, on va modifiernotre code pour afficher aleatoirement un repas dans la liste

Pour cela on va réutiliser le module ``random`` pour choisir aléatoirement un repas dans notre liste
```py
import os
import random

if os.path.exists("repas.txt"):
    with open("repas.txt", "r+") as file:
        repas_liste =file.readlines()
        repas_choix = random.choice(repas_liste)
        print("Je vous propose aujourd'hui comme repas :", repas_choix)
        file.close()
else:
    print("Le document n'existe pas ! Attention !")
```
Resultat 1 :
```shell
Je vous propose aujourd'hui comme repas : tacos
```
Resultat 2 :
```shell
Je vous propose aujourd'hui comme repas : kfc
```

### Déplacer ou dupliquer un fichier
Pour cela, on va prendre comme exemple, le déplacement d'une image dans le dossier img

Pour cela, on va commencer à importer deux modules, tout d'abords, le module ``os`` vu un peu plus haut et le module ``shutil`` qui permet notament le deplacement de fichier ou la copie de fichier
```ty
import os
import shutil
```
Puis, on va lui indiquer une source, et un enddroit ou le copier, puis on utilise le module ``shutil`` pour copier
```py
source = "password.png"
target = "img/password.png"

shutil.copy(source, target)
```
Pour le couper/coller, il faut aussi faire le copier/coller puis le supprimer le fichier d'origine
```py
shutil.copy(source, target)
os.remove(source)
```







