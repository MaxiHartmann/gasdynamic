from tkinter import *

root = Tk()

def printName(event):
    print("Chelo my name is Bucky!")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)
button_1.grid(row=0, column=0)

root.mainloop()
