from tkinter import *


def doNothing():
    print("ok ok I won't")
def doNothing2():
    print("ok ok I won't. New...")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing2)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing2)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
