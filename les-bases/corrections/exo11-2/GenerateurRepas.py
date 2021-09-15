from tkinter import *
import os
import random

def generate_random_meal_suggestion():
    if os.path.exists("repas.txt"):
        with open("repas.txt", "r+") as file:
            repas_liste =file.readlines()
            repas_choix = random.choice(repas_liste)
            reaps_aleatoire.config(text="Je vous propose aujourd'hui comme repas :" + repas_choix, font=("Helvetica", 20), bg="#4065A4", fg="#FFFFFF")
            file.close()
    else:
        print("Le document n'existe pas ! Attention !")
    
window = Tk()
window.title("Choix du repas")
window.geometry("720x480")
window.config(background="#4065A4")

frame = Frame(window, bg="#4065A4")
titre = Label(frame, text="Générer un mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
titre.pack()

reaps_aleatoire = Label(frame, text="", font=("Helvetica", 20), bg="#4065A4", fg="#FFFFFF")
reaps_aleatoire.pack()

generation_repas_button = Button(frame, text="Je sais pas", font=("Helvetica", 20), bg="#4065A4", fg="#FFFFFF",  command=generate_random_meal_suggestion)
generation_repas_button.pack(fill=X)

frame.pack(expand=YES)

window.mainloop()