# La boucle for
for num_client in range(1,5):
    print("Vous êtes le client n°", num_client)
    
# La boucle for each
emails = ["arnaud.fourmault@gmail.com", "arnaudf59@hotmail.fr", "arnaud.dev@gmail.com", "arnaud.taf@gmail.com"]

# Blacklist
blacklist = ["arnaud.dev@gmail.com", "arnaud.taf@gmail.com"]

for email in emails:
    if email in blacklist:
        print("Email {} interdit! envoi impossible".format(email))
        continue
    
    print("Email envoyé à: ", email)
    
# La boucle while
salaire = 1500

while salaire < 2000:
    salaire += 120
    print("Votre salaire actuel est de ", salaire, "€")
    