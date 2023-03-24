import tkinter as tk
import random

antal=0
dices=[]
buttons=[]
saved=[False, False, False, False, False]

def dice_throw():
    antal=1
    while antal==1:
        dice=random.randint(1,6)
        antal=antal+1
        dices.append(dice)
    return dice    

def change_color(index):
    # sparad tärning blir grön
    if saved[index]==False:
        buttons[index].configure(bg="green")
        saved[index]=True
    elif saved[index]==True:
        buttons[index].configure(bg="white")
        saved[index]=False

def roll_again():
    # Slå tärningar igen
    # gå igenom saved med index = 0, 1, ...4
    global antal
    if antal<2:
        for i in range (5):
            if saved [i] ==False:
                # kasta denna tärning, visa på knapp
                dice=random.randint(1,6)
                buttons[i].configure(text=dice)
                dices[i]=dice
        antal=antal+1
        print(dices)
    else:
        roll_dice.pack_forget()
        


root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

dice_throw()

dice1=tk.Button(frame, text=dices[0], command=lambda: change_color(0))
dice1.pack(side=tk.LEFT)

buttons.append(dice1)
dice=dice_throw()

dice2=tk.Button(frame, text=dices[1], command=lambda: change_color(1))
dice2.pack(side=tk.LEFT)

buttons.append(dice2)
dice=dice_throw()

dice3=tk.Button(frame, text=dices[2], command=lambda: change_color(2))
dice3.pack(side=tk.LEFT)

buttons.append(dice3)
dice=dice_throw()

dice4=tk.Button(frame, text=dices[3], command=lambda: change_color(3))
dice4.pack(side=tk.LEFT)

buttons.append(dice4)
dice=dice_throw()

dice5=tk.Button(frame, text=dices[4], command=lambda: change_color(4))
dice5.pack(side=tk.LEFT)

buttons.append(dice5)

roll_dice=tk.Button(frame, text="Slå igen", command=roll_again)
roll_dice.pack(side=tk.LEFT)

root.mainloop()
