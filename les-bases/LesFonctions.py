# Premiere fonction
def bienvenue():
    print("Bienvenue")
    result = 5 + 6
    print("Le resultat est de :", result)
    
    
bienvenue()

# Fonction année suivante
def anneeSuivante():
    global year
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)

year = 2021

anneeSuivante()

# Fonction avec argument
def addition1():
    result = 5 + 5
    return result

def message():
    return "le resultat du calcul est"

def multiplication():
    result = 5 * 5
    return result

def addition(n = 6):
    return 5 + n

print(message(), multiplication())
print(message(), addition(4))
print(message(), addition())

# La récursivité
def add(a):
    a += 1
    print(a)
    if a < 20:
        add(a)
    
add(12)

