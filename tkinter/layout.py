from tkinter import *

root = Tk()

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

button1 = Button(root, text="Calculate", fg="red")

label1 = Label(root, text="INPUT:").grid(row=0, column=0)
led_1 = Entry(root, text="INPUT:").grid(row=0, column=1)
button1.grid(row=0, column=4)

label2 = Label(root, text="out 1 =").grid(row=1, column=0)
label3 = Label(root, text="out 2 =").grid(row=2, column=0)
label4 = Label(root, text="out 3 =").grid(row=3, column=0)

led_2 = Entry(root, text="out 1 =").grid(row=1, column=1)
led_3 = Entry(root, text="out 2 =").grid(row=2, column=1)
led_4 = Entry(root, text="out 3 =").grid(row=3, column=1)

label5 = Label(root, text="out 1 =").grid(row=1, column=2)
label6 = Label(root, text="out 2 =").grid(row=2, column=2)
label7 = Label(root, text="out 3 =").grid(row=3, column=2)

led_5 = Entry(root, text="out 1 =").grid(row=1, column=3)
led_6 = Entry(root, text="out 2 =").grid(row=2, column=3)
led_7 = Entry(root, text="out 3 =").grid(row=3, column=3)

label8 = Label(root, text="out 7 =").grid(row=1, column=4)
label9 = Label(root, text="out 8 =").grid(row=2, column=4)
label10 = Label(root, text="out 9 =").grid(row=3, column=4)

led_8 = Entry(root, text="out 1 =").grid(row=1, column=5)
led_9 = Entry(root, text="out 2 =").grid(row=2, column=5)
led_10 = Entry(root, text="out 3 =").grid(row=3, column=5)

label9 = Label(root, text="out 7 =").grid(row=1, column=6)
label10 = Label(root, text="out 8 =").grid(row=2, column=6)
label11 = Label(root, text="out 9 =").grid(row=3, column=6)

led_9 = Entry(root, text="out 1 =").grid(row=1, column=7)
led_10 = Entry(root, text="out 2 =").grid(row=2, column=7)
led_11 = Entry(root, text="out 3 =").grid(row=3, column=7)
root.mainloop()

