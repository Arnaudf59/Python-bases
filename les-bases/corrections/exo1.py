def main():
    portemonnaie = int(input("Saisissez l'argent dont vous disposez"))
    print("Vous avez actuellement", portemonnaie, "euros")
    produit = 50
    print("Le Produit vaut", produit, "euros")
    portemonnaie = portemonnaie - produit
    print("Produit acheté !")
    print("Votre porte monnaie contient désormer: " + str(portemonnaie) + " euros")
    
if __name__ == '__main__':
    main()