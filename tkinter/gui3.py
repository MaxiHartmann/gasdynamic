from tkinter import *


OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

root = Tk()

def calculate(event):
    print("TODO: Calculation")

root.geometry('100x200')

variable = StringVar(root)
variable.set(OptionList[0])

opt = OptionMenu(root, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

button_1 = Button(root, text="Calculate")
button_1.bind("<Button-1>", calculate)
button_1.grid(row=0, column=0)

label_1 = Label(root, text="INPUT:")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)


root.mainloop()
