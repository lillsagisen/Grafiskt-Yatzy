import tkinter as tk
import random

dice=random.randint(1,6)

def write_slogan():
    print("Sparad", dice)

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame, text=dice, command=write_slogan)
button.pack(side=tk.LEFT)

root.mainloop()
