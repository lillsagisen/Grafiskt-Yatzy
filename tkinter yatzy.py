import tkinter as tk
import random

#dice=random.randint(1,6)
dices=[]
buttons=[]

def dice_throw():
    antal=1
    while antal==1:
        dice=random.randint(1,6)
        antal=antal+1
        dices.append(dice)
    return dice    

def write_slogan(index):
    msg=tk.Message(root, text="Sparad "+str(dices[index]))
    msg.pack()
    

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

dice_throw()

dice1=tk.Button(frame, text=dices[0], command=lambda: write_slogan(0))
dice1.pack(side=tk.LEFT)

dice=dice_throw()

dice2=tk.Button(frame, text=dices[1], command=lambda: write_slogan(1))
dice2.pack(side=tk.LEFT)

dice=dice_throw()

dice3=tk.Button(frame, text=dices[2], command=lambda: write_slogan(2))
dice3.pack(side=tk.LEFT)

dice=dice_throw()

dice4=tk.Button(frame, text=dices[3], command=lambda: write_slogan(3))
dice4.pack(side=tk.LEFT)

dice=dice_throw()

dice5=tk.Button(frame, text=dices[4], command=lambda: write_slogan(4))
dice5.pack(side=tk.LEFT)

root.mainloop()
