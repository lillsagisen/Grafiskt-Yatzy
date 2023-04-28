import tkinter as tk
import random

antal=0
dices=[]
buttons=[]
point_buttons=[]
saved=[False, False, False, False, False]
points_before_bonus=[]
#Commands
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
    if antal<3:
        for i in range (5):
            if saved [i] ==False:
                # kasta denna tärning, visa på knapp
                dice=random.randint(1,6)
                buttons[i].configure(text=dice)
                dices[i]=dice
        antal=antal+1
        print(dices)
    else:
        roll_dice.grid_forget()
        antal=0

def ones_command(index):
    #POÄNG ETTOR
    #Räknar ut hur många ettor du har och dina poäng.
    global antal
    points=0
    if antal==0:
        for i in dices:
            if i==index+1:
                points=points + index+1
                points_label=tk.Label(frame, text=points)
                points_label.grid(row=index+2, column=1)
                roll_dice.grid(row=0, column=5)
                for i in range (5):
                    if saved [i] == True:
                        saved[i] = False
                        buttons[i].configure(bg="white")
            else:
                points_label=tk.Label(frame, text=points)
                points_label.grid(row=index+2, column=1)
                roll_dice.grid(row=0, column=5)

    for i in range (5):
        buttons[i].configure(text="0")
        
    point_buttons[index]["state"]=tk.DISABLED
    points_before_bonus.append(points)

#Knappar
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

dice_throw()

dice1=tk.Button(frame, text="0", command=lambda: change_color(0))
dice1.grid(row=0, column=0)

buttons.append(dice1)
dice=dice_throw()

dice2=tk.Button(frame, text="0", command=lambda: change_color(1))
dice2.grid(row=0, column=1)

buttons.append(dice2)
dice=dice_throw()

dice3=tk.Button(frame, text="0", command=lambda: change_color(2))
dice3.grid(row=0, column=2)

buttons.append(dice3)
dice=dice_throw()

dice4=tk.Button(frame, text="0", command=lambda: change_color(3))
dice4.grid(row=0, column=3)

buttons.append(dice4)
dice=dice_throw()

dice5=tk.Button(frame, text="0", command=lambda: change_color(4))
dice5.grid(row=0, column=4)

buttons.append(dice5)

roll_dice=tk.Button(frame, text="Slå igen", command=roll_again)
roll_dice.grid(row=0, column=5)
#Poängknapparna
ur_points=tk.Button(frame, text="Dina Poäng")
ur_points.grid(row=1, column=0)

ones=tk.Button(frame, text="Ettor", command=lambda: ones_command(0))
ones.grid(row=2, column=0, sticky=tk.E+tk.W)

point_buttons.append(ones)

twos=tk.Button(frame, text="Tvåor", command=lambda: ones_command(1))
twos.grid(row=3, column=0, sticky=tk.E+tk.W)

point_buttons.append(twos)

threes=tk.Button(frame, text="Treor", command=lambda: ones_command(2))
threes.grid(row=4, column=0, sticky=tk.E+tk.W)

point_buttons.append(threes)

fours=tk.Button(frame, text="Fyror")
fours.grid(row=5, column=0, sticky=tk.E+tk.W)

point_buttons.append(fours)

fives=tk.Button(frame, text="Femmor")
fives.grid(row=6, column=0, sticky=tk.E+tk.W)

point_buttons.append(fives)

sixes=tk.Button(frame, text="Sexor")
sixes.grid(row=7, column=0, sticky=tk.E+tk.W)

point_buttons.append(sixes)

root.mainloop()
