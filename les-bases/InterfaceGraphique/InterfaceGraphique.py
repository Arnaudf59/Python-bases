from tkinter import *
import webbrowser

def open_github():
    webbrowser.open_new("https://github.com/Arnaudf59")

# Création d'une fenêtre
window = Tk()

# Personnalisation de la fenêtre
# Titre de la fenêtre
window.title("Interface Graphique")
# Taille de la fenêtre
window.geometry("720x480")
#Taille minimun de la fenêtre
window.minsize(480, 360)
# Modification du fond de notre fenêtre
window.config(background='#41B77F')
# Icon de le fenêtre
window.iconbitmap(r'C:\dev\projet\Python-bases\les-bases\InterfaceGraphique\logo.ico')


# frame
frame = Frame(window, bg='#41B77F')

#premier composant
label = Label(frame, text = "Bienvenue sur l'appication", font=("Courrier", 40), bg='#41B77F', fg='#FFFFFF')
label.pack()

# Ajouter un sous titre
sub_label = Label(frame, text = "Comment allez vous?", font=("Courrier", 25), bg='#41B77F', fg='#FFFFFF')
sub_label.pack()

# Ajouter un premier bouton
button_github = Button(frame, text="Ouvrir Git Hub", font=("Courrier", 25), fg='#41B77F', bg='#FFFFFF', command=open_github)
button_github.pack(pady=25, fill=X)

# Afficher notre frame
frame.pack(expand=YES)

# afficher
window.mainloop()