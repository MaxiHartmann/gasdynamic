from tkinter import *


root = Tk()

photo = PhotoImage(file="penguin.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()
