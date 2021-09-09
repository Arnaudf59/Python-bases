from tkinter import *
import string
from random import randint, choice

def generate_password():
    taille_min = 6
    taille_max = 15
    all_caractère = string.ascii_letters + string.punctuation +string.digits
    password = "".join(choice(all_caractère) for x in range(randint(taille_min, taille_max)))
    input_genere.delete(0, END)
    input_genere.insert(0, password)
    

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap(r'C:\dev\projet\Python-bases\les-bases\InterfaceGraphique\logo.ico')
window.config(background="#4065A4")

frame = Frame(window, bg="#4065A4")

# creation d'image
width = 300
height = 300
img = PhotoImage(file=r'C:\dev\projet\Python-bases\les-bases\InterfaceGraphique\password.png').zoom(20).subsample(36)
canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=img)
canvas.grid(row=0, column=0, sticky=W)

frame_droite = Frame(frame, bg="#4065A4")

titre = Label(frame_droite, text="Générer un mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
titre.pack()

input_genere = Entry(frame_droite, font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF')
input_genere.pack()

button_genere = Button(frame_droite, text="Générer", font=("Helvetica", 20), bg='#4065A4', fg='#FFFFFF', command=generate_password)
button_genere.pack(fill=X)

frame_droite.grid(row=0, column = 1, sticky=W)

frame.pack(expand=YES)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()