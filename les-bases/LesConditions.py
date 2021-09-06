#Exemple condition 1
# Variables
portemonnaie = int(input("De combien d'argent disposez-vous?"))
prix_produit = 900

# Vérification que le prix de l'ordinateur est inférieur à 1000€
if prix_produit <= portemonnaie:
    print("Vous achetez ce produit")
    # Première version
    # portemonnaie = portemonnaie - prix_produit
    # Deuxieme version
    portemonnaie -= prix_produit
    print("Vous disposez désormé de: {}€".format(portemonnaie))
else:
    print("Vous ne pouvez pas acheter ce produit")
    
text = ("L'achat est possible", "L'achat est impossible")[prix_produit <= portemonnaie]
print(text)

#Exemple condition 2
# Systeme de verification de mot de passe

# Variable
password = input("Entrer votre mot de passe:")
password_length = len(password)
print(password_length)

# Vérifier si le mot de passe est supérieur à 8 caracteres
if password_length <= 8:
    print("Mot de passe trop court")
elif password_length > 8 and password_length <= 12:
    print("Mot de passe moyen")
else:
    print("Mot de passe parfait")