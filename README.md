# Python-bases

## Installation
Installer python sur le site ``www.python.org``

Installer les extension visual studion python

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