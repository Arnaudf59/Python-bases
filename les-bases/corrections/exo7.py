def nb_voyelle_mot(mot):
    compteur = 0
    
    for letter in mot:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            compteur += 1
            
    return compteur
    
mot = input("Saississez un mot: ")
compteur_lettre = nb_voyelle_mot(mot)
print("Il y a", compteur_lettre, "voyelles dans le mot", mot)