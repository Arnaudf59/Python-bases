def main():
    # Récupérer une premiere variable
    note1 = int(input("Entrer la premiere note"))
    # Récupérer une premiere variable
    note2 = int(input("Entrer la seconde note"))
    # Récupérer une premiere variable
    note3 = int(input("Entrer la dernière note"))
    # Calcul de la moyenne
    result = (note1 + note2 + note3) /3
    print("La moyenne est de:" + str(result))
    
if __name__ == '__main__':
    main()