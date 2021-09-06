def main():
    # Création d'un variable string
    username = "Arnaud"
    print(username)
    # Création d'une variavle int
    age = 30
    print(age)
    # Création d'une variavle float
    portfeuille = 125.7
    print(portfeuille)
    # Création d'une variavle booleen
    is_happy = True
    print(is_happy)
    print(username, age, portfeuille, is_happy)
    # On peut modifier une variable
    age = 31
    print(age)
    # On peut modifier une variable avec une opération 
    age = age - 1
    print(age)
    print("Salut " + username + ", vous avez " + str(age) + " ans")
    
if __name__ == '__main__':
    main()