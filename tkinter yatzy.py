import tkinter as tk
import random

antal=0
dices=[]
buttons=[]
point_buttons=[]
saved=[False, False, False, False, False]
points_before_bonus=[]
total_points=[]
one_to_six_label=[]
bonus_points_label=False
variable=-1
#Commands
def dice_throw():
    antal=1
    while antal==1:
        dice=random.randint(1,6)
        antal=antal+1
        dices.append(dice)
    return dice

def restart_throw():
    for i in range (5):
            if saved [i] == True:
                saved[i] = False
                buttons[i].configure(bg="white")
    for i in range (5):
        buttons[i].configure(text="0")
    roll_dice.grid(row=0, column=5)

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
        roll_dice.grid_forget()
        antal=0

#Bonusen ska funka
def check_bonus ():
    global bonus_points_label
    if ones["state"]==tk.DISABLED and twos["state"]==tk.DISABLED and threes["state"]==tk.DISABLED and fours["state"]==tk.DISABLED and fives["state"]==tk.DISABLED and sixes["state"]==tk.DISABLED:
        if sum(points_before_bonus)>= 63:
            bonus_points=50
            bonus=tk.Label(frame, text=bonus_points)
            bonus.grid(row=8, column=1)
            total_points.append(bonus_points)
            bonus_points_label==True
            one_to_six_label.append(bonus)
            
            


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
        one_to_six_label.append(points_label)
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


def antal_dice(ögon):
    # return antal med antal ögon
    antal_dice_antal=0
    for i in dices:
        if i==ögon:
            antal_dice_antal=antal_dice_antal+1
    return antal_dice_antal

def one_pair():
    # för varje 6, 5, 4, ..., 1
    # par i detta?
    # skriv ut och klart
    # inget par, gör något lämpligt
    global antal
    if antal==0:
        for i in reversed(range(7)):
            if antal_dice(i)>1:
                ett_par_points=tk.Label(frame, text=i+i)
                ett_par_points.grid(row=9, column=1)
                total_points.append(i+i)
                ett_par["state"]=tk.DISABLED
                break
            else:
                ett_par_points=tk.Label(frame, text="0")
                ett_par_points.grid(row=9, column=1)
                ett_par["state"]=tk.DISABLED
                
        restart_throw()
        one_to_six_label.append(ett_par_points)

def two_pairs():
    #2 sexor och 2 femmor?.......
    #Poäng till knappen två_par
    global antal
    har_hittat_tvapar = False
    if antal==0:
        for i in reversed(range(7)):
            if antal_dice(i)>1:
                for n in reversed(range(i)):
                    if antal_dice(n)>1:
                        två_par_points=tk.Label(frame, text=i+i+n+n)
                        två_par_points.grid(row=10, column=1)
                        total_points.append(i+i+n+n)
                        två_par["state"]=tk.DISABLED
                        har_hittat_tvapar = True
                        break
                    else:
                        två_par_points=tk.Label(frame, text="0")
                        två_par_points.grid(row=10, column=1)
                        två_par["state"]=tk.DISABLED
            if har_hittat_tvapar:
                break

        restart_throw()
        one_to_six_label.append(två_par_points)


def three_of_one():
    #Räknar om man har tre av samma
    global antal
    if antal==0:
        for i in reversed(range(7)):
            if antal_dice(i)>2:
                tretal_points=tk.Label(frame, text=i+i+i)
                tretal_points.grid(row=11, column=1)
                tretal["state"]=tk.DISABLED
                total_points.append(i+i+i)
                break
            else:
                tretal_points=tk.Label(frame, text="0")
                tretal_points.grid(row=11, column=1)
                tretal["state"]=tk.DISABLED

        restart_throw()
        one_to_six_label.append(tretal_points)


def four_of_one():
    #Räknar om du har fyra av samma
    global antal
    if antal==0:
        for i in reversed(range(7)):
            if antal_dice(i)>3:
                fyrtal_points=tk.Label(frame, text=i+i+i+i)
                fyrtal_points.grid(row=12, column=1)
                fyrtal["state"]=tk.DISABLED
                total_points.append(i+i+i+i)
                break
            else:
                fyrtal_points=tk.Label(frame, text="0")
                fyrtal_points.grid(row=12, column=1)
                fyrtal["state"]=tk.DISABLED

    restart_throw()
    one_to_six_label.append(fyrtal_points)

def full_house():
    #Command för att räkna om man har en kåk
    global antal
    har_hittat_kåk=False
    if antal==0:
        for i in reversed(range(7)):
            if antal_dice(i)>2:
                for n in reversed(range(7)):
                    if antal_dice(n)!=antal_dice(i):
                    
                        if antal_dice(n)>1:
                            kåk_points=tk.Label(frame, text=i+i+i+n+n)
                            kåk_points.grid(row=13, column=1)
                            kåk["state"]=tk.DISABLED
                            total_points.append(i+i+i+n+n)
                            har_hittat_kåk=True
                            break
                        
                        else:
                            kåk_points=tk.Label(frame, text="0")
                            kåk_points.grid(row=13, column=1)
                            kåk["state"]=tk.DISABLED
                            
            if har_hittat_kåk:
                break

        restart_throw()
        one_to_six_label.append(kåk_points)

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

        restart_throw()
        one_to_six_label.append(liten_stege_points)


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

        restart_throw()
        one_to_six_label.append(stor_stege_points)


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

        restart_throw()
        one_to_six_label.append(chans_points)


def yatzy_command():
    #Kollar om man har yatzy. 50 poäng
    global antal
    if antal==0:
        for i in reversed(range(7)):
            if antal_dice(i)>4:
                yatzy_points=tk.Label(frame, text="50")
                yatzy_points.grid(row=17, column=1)
                total_points.append(50)
                yatzy["state"]=tk.DISABLED
                break

            else:
                yatzy_points=tk.Label(frame, text="0")
                yatzy_points.grid(row=17, column=1)
                yatzy["state"]=tk.DISABLED
                break

        restart_throw()
        one_to_six_label.append(yatzy_points)

def calculate_points():
    #En knapp för att kunna se hur många poäng du har hela tiden
    points_label.configure(text=sum(total_points))
    one_to_six_label.append(points_label)

def change_variable ():
    global variable
    variable=variable+1
    


def save_command():
    global variable
    global total_points
    global points_before_bonus
    global one_to_six_label
    #Spara dina poäng och starta om
    if ones["state"]==tk.DISABLED and twos["state"]==tk.DISABLED and threes["state"]==tk.DISABLED and fours["state"]==tk.DISABLED and fives["state"]==tk.DISABLED and sixes["state"]==tk.DISABLED and ett_par["state"]==tk.DISABLED and två_par["state"]==tk.DISABLED and tretal["state"]==tk.DISABLED and fyrtal["state"]==tk.DISABLED and kåk["state"]==tk.DISABLED and liten_stege["state"]==tk.DISABLED and stor_stege["state"]==tk.DISABLED and chans["state"]==tk.DISABLED and yatzy["state"]==tk.DISABLED:
        one_to_six_label[0].configure(text="0")
        one_to_six_label[1].configure(text="0")
        one_to_six_label[2].configure(text="0")
        one_to_six_label[3].configure(text="0")
        one_to_six_label[4].configure(text="0")
        one_to_six_label[5].configure(text="0")
        one_to_six_label[6].configure(text="0")
        one_to_six_label[7].configure(text="0")
        one_to_six_label[8].configure(text="0")
        one_to_six_label[9].configure(text="0")
        one_to_six_label[10].configure(text="0")
        one_to_six_label[11].configure(text="0")
        one_to_six_label[12].configure(text="0")
        one_to_six_label[13].configure(text="0")
        one_to_six_label[14].configure(text="0")
        one_to_six_label[15].configure(text="0")
        
    if bonus_points_label==True:
        one_to_six_label[16].configure(text="0")

    ones["state"]=tk.NORMAL
    twos["state"]=tk.NORMAL
    threes["state"]=tk.NORMAL
    fours["state"]=tk.NORMAL
    fives["state"]=tk.NORMAL
    sixes["state"]=tk.NORMAL
    ett_par["state"]=tk.NORMAL
    två_par["state"]=tk.NORMAL
    tretal["state"]=tk.NORMAL
    fyrtal["state"]=tk.NORMAL
    kåk["state"]=tk.NORMAL
    liten_stege["state"]=tk.NORMAL
    stor_stege["state"]=tk.NORMAL
    chans["state"]=tk.NORMAL
    yatzy["state"]=tk.NORMAL

    sparat_spel=tk.Label(frame, text="Sparat spel "+str(sum(total_points))+" poäng")
    sparat_spel.grid(row=variable+1, column=6)
    total_points=[]
    points_before_bonus=[]
    one_to_six_label=[]

    
        

        
        
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

spara=tk.Button(frame, text="Spara", command= lambda:[save_command(), change_variable()])
spara.grid(row=19, column=0, sticky=tk.E+tk.W)

root.mainloop()
