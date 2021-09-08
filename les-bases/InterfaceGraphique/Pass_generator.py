from tkinter import *

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap(r'C:\dev\projet\Python-bases\les-bases\InterfaceGraphique\logo.ico')
window.config(background="#4065A4")

# creation d'image
width = 300
height = 300
img = PhotoImage(file=r'C:\dev\projet\Python-bases\les-bases\InterfaceGraphique\password.png').zoom(20).subsample(36)
canvas = Canvas(window, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=img)
canvas.pack(expand=YES)

window.mainloop()