import tkinter as tk

root = tk.Tk()

def calc():
    print("Calculate...")
    print("Machnumber = {}".format(led_1.get()))
    led_2.delete(0,tk.END)
    led_2.insert(0,"{:.04f}".format(float(led_1.get())))

lbl_input = tk.Label(root, text="INPUT:").grid(row=0, column=0)
led_1 = tk.Entry(root, text="2.0")
led_1.grid(row=0, column=1)
btn_calc = tk.Button(root, text="Calculate", fg="red", command=calc)
btn_calc.grid(row=0, column=4)

label2 = tk.Label(root, text="Machnumber =").grid(row=1, column=0)
label3 = tk.Label(root, text="p/p0 =").grid(row=2, column=0)
label4 = tk.Label(root, text="p/p* =").grid(row=3, column=0)

led_2 = tk.Entry(root, text="")
led_2.grid(row=1, column=1)
led_3 = tk.Entry(root, text="").grid(row=2, column=1)
led_4 = tk.Entry(root, text="").grid(row=3, column=1)

label5 = tk.Label(root, text="Mach angle =").grid(row=1, column=2)
label6 = tk.Label(root, text="rho/rho0 =").grid(row=2, column=2)
label7 = tk.Label(root, text="rho/rho* =").grid(row=3, column=2)

led_5 = tk.Entry(root, text="").grid(row=1, column=3)
led_6 = tk.Entry(root, text="").grid(row=2, column=3)
led_7 = tk.Entry(root, text="").grid(row=3, column=3)

label8 = tk.Label(root, text="P-M angle =").grid(row=1, column=4)
label9 = tk.Label(root, text="T/T0 =").grid(row=2, column=4)
label10 = tk.Label(root, text="T/T* =").grid(row=3, column=4)

led_8 = tk.Entry(root, text="").grid(row=1, column=5)
led_9 = tk.Entry(root, text="").grid(row=2, column=5)
led_10 = tk.Entry(root, text="").grid(row=3, column=5)

label9 = tk.Label(root, text="Ma* =").grid(row=1, column=6)
label10 = tk.Label(root, text="...").grid(row=2, column=6)
label11 = tk.Label(root, text="A/A* =").grid(row=3, column=6)

led_9 = tk.Entry(root, text="").grid(row=1, column=7)
led_10 = tk.Entry(root, text="").grid(row=2, column=7)
led_11 = tk.Entry(root, text="").grid(row=3, column=7)
root.mainloop()

