# ☼☼ pip install ☼☼
from tkinter import *
from turtle import bgcolor, color
#---------------------------------
#config des 'command'
def estValide() :
    if user.get() == "test" and mdp.get()=="test":
        label_login["text"]="Login correct"
    else:
        label_login["text"]="Login incorrect"

def update_entry():
    global hidden
    if hidden:
        entry_mdp['show'] = ''
        btn['image'] = hide
    else:
        entry_mdp['show'] = '●'
        btn['image'] = view
    hidden = not hidden

#creation de la fenetre
fenetre = Tk()

#configuration de la fenetre
fenetre.title("Connexion")
fenetre.config(bg='#000000')
fenetre.minsize(width=400, height=200)
fenetre.maxsize(width=400, height=200)

user=StringVar()
mdp=StringVar()

label_user = Label(fenetre,text=("Identifiant",) , font=('Courier'),  bg='#000000')
label_user.config(fg='white')
label_mdp = Label(fenetre,text=("Mot de passe"), font=('Courier'), bg='#000000')
label_mdp.config(fg='white')
label_login = Label(fenetre, font="Arial 20 bold", bg='#000000')
label_login.config(fg='white')

hidden = True

hide = PhotoImage(file='Pictures///pythonimg///hidemdp.png')
view = PhotoImage(file='Pictures///pythonimg///viewmdp.png')

btnvalide = Button(fenetre,text="Valider",command=estValide, width=20)
entry_user = Entry(fenetre, textvariable=user)
entry_mdp = Entry(fenetre, textvariable=mdp, show="☻")

btn = Button(
    fenetre,
    image=hide,
    width=90,
    font='Times 15 bold',
    command=update_entry)
btn.pack(side="right",)

#affichage des modifications
label_user.pack()
entry_user.pack()

label_mdp.pack()
entry_mdp.pack()

btnvalide.pack(padx=120, pady=20)
btn.pack(padx=2, pady=5)
label_login.pack()



#affichage de la fenetre
fenetre.mainloop()

#FrTrax
#insta : maelrls
