from tkinter import *

cookie_count = 0


def add_cookie():
    global cookie_count
    cookie_count += 1
    label_counter.config(text=cookie_count)
    
def remove_cookie():
    global cookie_count
    cookie_count -= 1
    label_counter.config(text=cookie_count)
    
def zero_cookie():
    global cookie_count
    cookie_count = 0
    label_counter.config(text=cookie_count)
    
window = Tk()

window.title("Exercie n°10")
window.geometry("720x480")
window.minsize(480, 360)
window.config(background='#41B77F')

label_counter = Label(window, text="0", font=("Courrier", 30), bg="#dee5dc")
label_counter.pack()

frame = Frame(window, bg='#dee5dc')

width = 300
height = 300
image = PhotoImage(file=r'C:\dev\projet\Python-bases\les-bases\corrections\exo10\cookie.png')

button = Button(frame, text="Ajouter", bg='#dee5dc', bd=0, relief=SUNKEN, command=add_cookie)
button.pack()

button2 = Button(frame, text="Retirer", bg='#dee5dc', bd=0, relief=SUNKEN, command=remove_cookie)
button2.pack()

button3 = Button(frame, text="Reinitialiser", bg='#dee5dc', bd=0, relief=SUNKEN, command=zero_cookie)
button3.pack()

frame.pack(expand=YES)

window.mainloop()