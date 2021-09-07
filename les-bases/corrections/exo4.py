ecoute = 2500

mois = 0

while mois <= 24:
    ecoute *= 1.10
    mois += 1
    
print("Au bout de 24 mois, il y a eu {} ecoute".format(ecoute))