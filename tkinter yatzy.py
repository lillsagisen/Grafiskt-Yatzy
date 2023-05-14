import tkinter as tk
import random

antal=0
dices=[]
buttons=[]
point_buttons=[]
saved=[False, False, False, False, False]
points_before_bonus=[]
total_points=[]
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
    if antal<2:
        for i in range (5):
            if saved [i] ==False:
                # kasta denna tärning, visa på knapp
                dice=random.randint(1,6)
                buttons[i].configure(text=dice)
                dices[i]=dice
        antal=antal+1
        print(dices)

    elif antal==2:
        for i in range (5):
            if saved [i] ==False:
                # kasta denna tärning, visa på knapp
                dice=random.randint(1,6)
                buttons[i].configure(text=dice)
                dices[i]=dice
        antal=antal+1
        print(dices)
        roll_dice.grid_forget()
        antal=0

#Bonusen ska funka
def check_bonus ():
    global total_points
    if ones["state"]==tk.DISABLED and twos["state"]==tk.DISABLED and threes["state"]==tk.DISABLED and fours["state"]==tk.DISABLED and fives["state"]==tk.DISABLED and sixes["state"]==tk.DISABLED:
        if sum(points_before_bonus)>= 63:
            bonus_points=50
            bonus=tk.Label(frame, text=bonus_points)
            bonus.grid(row=8, column=1)
            total_points.append(bonus_points)
            


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

    for i in range (5):
        buttons[i].configure(text="0")
        
    point_buttons[index]["state"]=tk.DISABLED
    points_before_bonus.append(points)
    total_points.append(points)
    check_bonus()

def one_pair():
    # 2 sexor? -> 12 poäng
    # 2 femmor?
    # ...
    global antal
    antal_dices=0
    if antal==0:
        for i in dices:
            if i==6:
                antal_dices=antal_dices+1
        if antal_dices>1:
            ett_par_points=tk.Label(frame, text="12")
            ett_par_points.grid(row=9, column=1)
            total_points.append(12)
            ett_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            for i in range (5):
                if saved [i] == True:
                    saved[i] = False
                    buttons[i].configure(bg="white")
            for i in range (5):
                buttons[i].configure(text="0")
            return
        antal_dices=0
        for i in dices:
            if i==5:
                antal_dices=antal_dices+1
        if antal_dices>1:
            ett_par_points=tk.Label(frame, text="10")
            ett_par_points.grid(row=9, column=1)
            total_points.append(10)
            ett_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            for i in range (5):
                if saved [i] == True:
                    saved[i] = False
                    buttons[i].configure(bg="white")
            for i in range (5):
                buttons[i].configure(text="0")
            return
        antal_dices=0
        for i in dices:
            if i==4:
                antal_dices=antal_dices+1
        if antal_dices>1:
            ett_par_points=tk.Label(frame, text="8")
            ett_par_points.grid(row=9, column=1)
            total_points.append(8)
            ett_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            for i in range (5):
                if saved [i] == True:
                    saved[i] = False
                    buttons[i].configure(bg="white")
            for i in range (5):
                buttons[i].configure(text="0")
            return
        antal_dices=0
        for i in dices:
            if i==3:
                antal_dices=antal_dices+1
        if antal_dices>1:
            ett_par_points=tk.Label(frame, text="6")
            ett_par_points.grid(row=9, column=1)
            total_points.append(6)
            ett_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            for i in range (5):
                if saved [i] == True:
                    saved[i] = False
                    buttons[i].configure(bg="white")
            for i in range (5):
                buttons[i].configure(text="0")
            return
        antal_dices=0
        for i in dices:
            if i==2:
                antal_dices=antal_dices+1
        if antal_dices>1:
            ett_par_points=tk.Label(frame, text="4")
            ett_par_points.grid(row=9, column=1)
            total_points.append(4)
            ett_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            for i in range (5):
                if saved [i] == True:
                    saved[i] = False
                    buttons[i].configure(bg="white")
            for i in range (5):
                buttons[i].configure(text="0")
            return
        antal_dices=0
        for i in dices:
            if i==1:
                antal_dices=antal_dices+1
        if antal_dices>1:
            ett_par_points=tk.Label(frame, text="2")
            ett_par_points.grid(row=9, column=1)
            total_points.append(2)
            ett_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            for i in range (5):
                if saved [i] == True:
                    saved[i] = False
                    buttons[i].configure(bg="white")
            for i in range (5):
                buttons[i].configure(text="0")
            return
        ett_par_points=tk.Label(frame, text="0")
        ett_par_points.grid(row=9, column=1)
        ett_par["state"]=tk.DISABLED
        roll_dice.grid(row=0, column=5)
        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")

def antal_dice(ögon):
    # return antal med antal ögon
    antal_dice_antal=0
    for i in dices:
        if i==ögon:
            antal_dice_antal=antal_dice_antal+1
    return antal_dice_antal

def two_pairs():
    #2 sexor och 2 femmor?.......
    #Poäng till knappen två_par
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_six>3:
            två_par_points=tk.Label(frame, text="24")
            två_par_points.grid(row=10, column=1)
            total_points.append(24)
            två_par["state"]=tk.DISABLED
            
        elif antal_six>1 and antal_five>1:
            två_par_points=tk.Label(frame, text="22")
            två_par_points.grid(row=10, column=1)
            total_points.append(22)
            två_par["state"]=tk.DISABLED

        elif antal_six>1 and antal_four>1:
            två_par_points=tk.Label(frame, text="20")
            två_par_points.grid(row=10, column=1)
            total_points.append(20)
            två_par["state"]=tk.DISABLED

        elif antal_six>1 and antal_three>1:
            två_par_points=tk.Label(frame, text="18")
            två_par_points.grid(row=10, column=1)
            total_points.append(18)
            två_par["state"]=tk.DISABLED

        elif antal_six>1 and antal_two>1:
            två_par_points=tk.Label(frame, text="16")
            två_par_points.grid(row=10, column=1)
            total_points.append(16)
            två_par["state"]=tk.DISABLED

        elif antal_six>1 and antal_one>1:
            två_par_points=tk.Label(frame, text="14")
            två_par_points.grid(row=10, column=1)
            total_points.append(14)
            två_par["state"]=tk.DISABLED

        elif antal_five>3:
            två_par_points=tk.Label(frame, text="20")
            två_par_points.grid(row=10, column=1)
            total_points.append(20)
            två_par["state"]=tk.DISABLED

        elif antal_five>1 and antal_four>1:
            två_par_points=tk.Label(frame, text="18")
            två_par_points.grid(row=10, column=1)
            total_points.append(18)
            två_par["state"]=tk.DISABLED

        elif antal_five>1 and antal_three>1:
            två_par_points=tk.Label(frame, text="16")
            två_par_points.grid(row=10, column=1)
            total_points.append(16)
            två_par["state"]=tk.DISABLED

        elif antal_five>1 and antal_two>1:
            två_par_points=tk.Label(frame, text="14")
            två_par_points.grid(row=10, column=1)
            total_points.append(14)
            två_par["state"]=tk.DISABLED

        elif antal_five>1 and antal_one>1:
            två_par_points=tk.Label(frame, text="12")
            två_par_points.grid(row=10, column=1)
            total_points.append(12)
            två_par["state"]=tk.DISABLED

        elif antal_four>3:
            två_par_points=tk.Label(frame, text="16")
            två_par_points.grid(row=10, column=1)
            total_points.append(16)
            två_par["state"]=tk.DISABLED

        elif antal_four>1 and antal_three>1:
            två_par_points=tk.Label(frame, text="14")
            två_par_points.grid(row=10, column=1)
            total_points.append(14)
            två_par["state"]=tk.DISABLED

        elif antal_four>1 and antal_two>1:
            två_par_points=tk.Label(frame, text="12")
            två_par_points.grid(row=10, column=1)
            total_points.append(12)
            två_par["state"]=tk.DISABLED


        elif antal_four>1 and antal_one>1:
            två_par_points=tk.Label(frame, text="10")
            två_par_points.grid(row=10, column=1)
            total_points.append(10)
            två_par["state"]=tk.DISABLED

        elif antal_three>3:
            två_par_points=tk.Label(frame, text="12")
            två_par_points.grid(row=10, column=1)
            total_points.append(12)
            två_par["state"]=tk.DISABLED

        elif antal_three>1 and antal_two>1:
            två_par_points=tk.Label(frame, text="10")
            två_par_points.grid(row=10, column=1)
            total_points.append(10)
            två_par["state"]=tk.DISABLED

        elif antal_three>1 and antal_one>1:
            två_par_points=tk.Label(frame, text="8")
            två_par_points.grid(row=10, column=1)
            total_points.append(8)
            två_par["state"]=tk.DISABLED

        elif antal_two>3:
            två_par_points=tk.Label(frame, text="8")
            två_par_points.grid(row=10, column=1)
            total_points.append(8)
            två_par["state"]=tk.DISABLED

        elif antal_two>1 and antal_one>1:
            två_par_points=tk.Label(frame, text="6")
            två_par_points.grid(row=10, column=1)
            total_points.append(6)
            två_par["state"]=tk.DISABLED

        elif antal_one>3:
            två_par_points=tk.Label(frame, text="4")
            två_par_points.grid(row=10, column=1)
            total_points.append(4)
            två_par["state"]=tk.DISABLED

        else:
            två_par_points=tk.Label(frame, text="0")
            två_par_points.grid(row=10, column=1)
            två_par["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)

def three_of_one():
    #Räknar om man har tre av samma
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_six>2:
            tretal_points=tk.Label(frame, text="18")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(18)

        elif antal_five>2:
            tretal_points=tk.Label(frame, text="15")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(15)

        elif antal_four>2:
            tretal_points=tk.Label(frame, text="12")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(12)

        elif antal_three>2:
            tretal_points=tk.Label(frame, text="9")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(9)

        elif antal_two>2:
            tretal_points=tk.Label(frame, text="6")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(6)

        elif antal_one>2:
            tretal_points=tk.Label(frame, text="3")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(3)

        else:
            tretal_points=tk.Label(frame, text="0")
            tretal_points.grid(row=11, column=1)
            tretal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)


def four_of_one():
    #Räknar om du har fyra av samma
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_six>3:
            fyrtal_points=tk.Label(frame, text="18")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(18)

        elif antal_five>3:
            fyrtal_points=tk.Label(frame, text="15")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(15)

        elif antal_four>3:
            fyrtal_points=tk.Label(frame, text="12")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(12)

        elif antal_three>3:
            fyrtal_points=tk.Label(frame, text="9")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(9)

        elif antal_two>3:
            fyrtal_points=tk.Label(frame, text="6")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(6)

        elif antal_one>3:
            fyrtal_points=tk.Label(frame, text="3")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(3)

        else:
            fyrtal_points=tk.Label(frame, text="0")
            fyrtal_points.grid(row=12, column=1)
            fyrtal["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)


def full_house():
    #Command för att räkna om man har en kåk
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_six==3 and antal_five==2:
            kåk_points=tk.Label(frame, text="28")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(28)

        elif antal_six==3 and antal_four==2:
            kåk_points=tk.Label(frame, text="26")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(26)

        elif antal_six==3 and antal_three==2:
            kåk_points=tk.Label(frame, text="24")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(24)

        elif antal_six==3 and antal_two==2:
            kåk_points=tk.Label(frame, text="22")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(22)

        elif antal_six==3 and antal_one==2:
            kåk_points=tk.Label(frame, text="20")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(20)

        elif antal_five==3 and antal_six==2:
            kåk_points=tk.Label(frame, text="27")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(27)

        elif antal_five==3 and antal_four==2:
            kåk_points=tk.Label(frame, text="23")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(23)

        elif antal_five==3 and antal_three==2:
            kåk_points=tk.Label(frame, text="21")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(21)

        elif antal_five==3 and antal_two==2:
            kåk_points=tk.Label(frame, text="19")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(19)

        elif antal_five==3 and antal_one==2:
            kåk_points=tk.Label(frame, text="17")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(17)

        elif antal_four==3 and antal_six==2:
            kåk_points=tk.Label(frame, text="24")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(24)

        elif antal_four==3 and antal_five==2:
            kåk_points=tk.Label(frame, text="22")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(22)

        elif antal_four==3 and antal_three==2:
            kåk_points=tk.Label(frame, text="18")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(18)

        elif antal_four==3 and antal_two==2:
            kåk_points=tk.Label(frame, text="16")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(16)

        elif antal_four==3 and antal_one==2:
            kåk_points=tk.Label(frame, text="14")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(14)

        elif antal_three==3 and antal_six==2:
            kåk_points=tk.Label(frame, text="21")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(21)

        elif antal_three==3 and antal_five==2:
            kåk_points=tk.Label(frame, text="19")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(19)

        elif antal_three==3 and antal_four==2:
            kåk_points=tk.Label(frame, text="17")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(17)

        elif antal_three==3 and antal_two==2:
            kåk_points=tk.Label(frame, text="13")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(13)

        elif antal_three==3 and antal_one==2:
            kåk_points=tk.Label(frame, text="11")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(11)

        elif antal_two==3 and antal_six==2:
            kåk_points=tk.Label(frame, text="18")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(18)

        elif antal_two==3 and antal_five==2:
            kåk_points=tk.Label(frame, text="16")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(16)

        elif antal_two==3 and antal_four==2:
            kåk_points=tk.Label(frame, text="14")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(14)

        elif antal_two==3 and antal_three==2:
            kåk_points=tk.Label(frame, text="12")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(12)

        elif antal_two==3 and antal_one==2:
            kåk_points=tk.Label(frame, text="8")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(8)

        elif antal_one==3 and antal_six==2:
            kåk_points=tk.Label(frame, text="15")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(15)

        elif antal_one==3 and antal_five==2:
            kåk_points=tk.Label(frame, text="13")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(13)

        elif antal_one==3 and antal_four==2:
            kåk_points=tk.Label(frame, text="11")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(11)

        elif antal_one==3 and antal_three==2:
            kåk_points=tk.Label(frame, text="9")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(9)

        elif antal_one==3 and antal_two==2:
            kåk_points=tk.Label(frame, text="7")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(7)

        else:
            kåk_points=tk.Label(frame, text="0")
            kåk_points.grid(row=13, column=1)
            kåk["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)


def small_straight():
    #Kollar om du har en liten stege
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_one==1 and antal_two==1 and antal_three==1 and antal_four==1 and antal_five==1:
            liten_stege_points=tk.Label(frame, text="15")
            liten_stege_points.grid(row=14, column=1)
            liten_stege["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(15)

        else:
            liten_stege_points=tk.Label(frame, text="0")
            liten_stege_points.grid(row=14, column=1)
            liten_stege["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)


def big_straight():
    #Kollar omman har en stor stege
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_two==1 and antal_three==1 and antal_four==1 and antal_five==1 and antal_six==1:
            stor_stege_points=tk.Label(frame, text="20")
            stor_stege_points.grid(row=15, column=1)
            stor_stege["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)
            total_points.append(20)

        else:
            stor_stege_points=tk.Label(frame, text="0")
            stor_stege_points.grid(row=15, column=1)
            stor_stege["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)


def chans_command():
    #Räknar poäng till knappen chans
    global antal
    points=0
    if antal==0:
        for i in dices:
            points=points+i
            total_points.append(points)
            chans_points=tk.Label(frame, text=points)
            chans_points.grid(row=16, column=1)
            chans["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        else:
            chans_points=tk.Label(frame, text="0")
            chans_points.grid(row=16, column=1)
            chans["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)


def yatzy_command():
    #Kollar om man har yatzy. 50 poäng
    global antal
    antal_one=antal_dice(1)
    antal_two=antal_dice(2)
    antal_three=antal_dice(3)
    antal_four=antal_dice(4)
    antal_five=antal_dice(5)
    antal_six=antal_dice(6)
    if antal==0:
        if antal_six==5 or antal_five==5 or antal_four==5 or antal_three==5 or antal_two==5 or antal_one==5:
            yatzy_points=tk.Label(frame, text="50")
            yatzy_points.grid(row=17, column=1)
            total_points.append(50)
            yatzy["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        else:
            yatzy_points=tk.Label(frame, text="0")
            yatzy_points.grid(row=17, column=1)
            yatzy["state"]=tk.DISABLED
            roll_dice.grid(row=0, column=5)

        for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
        for i in range (5):
            buttons[i].configure(text="0")
        roll_dice.grid(row=0, column=5)

def calculate_points():
    #En knapp för att kunna se hur många poäng du har hela tiden
    points_label.configure(text=sum(total_points))
    
                

        
#Knappar
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

dice_throw()

dice1=tk.Button(frame, text="0", command=lambda: change_color(0))
dice1.grid(row=0, column=0, sticky=tk.E)

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

roll_dice=tk.Button(frame, text="Slå", command=roll_again)
roll_dice.grid(row=0, column=5)
#Poängknapparna
ur_points=tk.Label(frame, text="Dina Poäng")
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

fours=tk.Button(frame, text="Fyror", command=lambda: ones_command(3))
fours.grid(row=5, column=0, sticky=tk.E+tk.W)

point_buttons.append(fours)

fives=tk.Button(frame, text="Femmor", command=lambda: ones_command(4))
fives.grid(row=6, column=0, sticky=tk.E+tk.W)

point_buttons.append(fives)

sixes=tk.Button(frame, text="Sexor", command=lambda: ones_command(5))
sixes.grid(row=7, column=0, sticky=tk.E+tk.W)

point_buttons.append(sixes)

bonus_label=tk.Label(frame, text="Bonus")
bonus_label.grid(row=8, column=0, sticky=tk.E+tk.W)

ett_par=tk.Button(frame, text="Ett par", command=one_pair)
ett_par.grid(row=9, column=0, sticky=tk.E+tk.W)

två_par=tk.Button(frame, text="Två par", command=two_pairs)
två_par.grid(row=10, column=0, sticky=tk.E+tk.W)

tretal=tk.Button(frame, text="Tretal", command=three_of_one)
tretal.grid(row=11, column=0, sticky=tk.E+tk.W)

fyrtal=tk.Button(frame, text="Fyrtal", command=four_of_one)
fyrtal.grid(row=12, column=0, sticky=tk.E+tk.W)

kåk=tk.Button(frame, text="Kåk", command=full_house)
kåk.grid(row=13, column=0, sticky=tk.E+tk.W)

liten_stege=tk.Button(frame, text="Liten stege", command=small_straight)
liten_stege.grid(row=14, column=0, sticky=tk.E+tk.W)

stor_stege=tk.Button(frame, text="Stor stege", command=big_straight)
stor_stege.grid(row=15, column=0, sticky=tk.E+tk.W)

chans=tk.Button(frame, text="Chans", command=chans_command)
chans.grid(row=16, column=0, sticky=tk.E+tk.W)

yatzy=tk.Button(frame, text="Yatzy", command=yatzy_command)
yatzy.grid(row=17, column=0, sticky=tk.E+tk.W)

points=tk.Button(frame, text="Räkna dina poäng", command=calculate_points)
points.grid(row=18, column=0, sticky=tk.E+tk.W)

points_label=tk.Label(frame, text="0")
points_label.grid(row=18, column=1)

root.mainloop()
