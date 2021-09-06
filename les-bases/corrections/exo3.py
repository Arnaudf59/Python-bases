from random import shuffle

phrase = input("Entrer une phrase:")
liste = phrase.split(" ")
print(liste)
shuffle(liste)
print(liste)
if(len(liste) < 10):
    print(liste[0:2])
else:
    print(liste[len(liste) - 3: len(liste)])
