# Variable
age = int(input("Quel age avez vous?"))

# Condition
if age < 18:
    prix_total = 7
else:
    prix_total = 12
    
pop_corn = input("Voulez vous du popcoorn ? (oui, non)")

if pop_corn == "oui":
    prix_total += 5

print("Vous devez réglé la somme de: {}€".format(prix_total))