import tkinter as tk

#==================== Frames ====================  
root = tk.Tk()
root.geometry('1200x600+10+10')

inputFrame = tk.Frame(root, bg='green', width=1200, height=100)
inputFrame.pack(side=tk.TOP, fill=tk.X,)

resultsFrame = tk.Frame(root, bg='blue', width=1200, height=500)
resultsFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)

#====================Variables ====================  
txt_val1 = tk.StringVar()
txt_val2 = tk.StringVar()
txt_val3 = tk.StringVar()
txt_val4 = tk.StringVar()
# ...

#====================Methods ====================  
def calc():
    print("Calculate...")
    print("Machnumber = {}".format(led_1.get()))
    led_2.delete(0,tk.END)
    led_2.insert(0,"{:.04f}".format(float(led_1.get())))


#====================INPUT Line====================  
lbl_name = tk.Label(inputFrame, text="Isentropic Flow Calculator",
        bg='green', font=('arial', 20, 'bold'))
lbl_name.grid(row=0, column=0)
lbl_input = tk.Label(inputFrame, text="INPUT:")
lbl_input.grid(row=1, column=0)
led_1 = tk.Entry(inputFrame, text="2.0")
led_1.grid(row=1, column=1)
btn_calc = tk.Button(inputFrame, text="Calculate", fg="red", command=calc)
btn_calc.grid(row=1, column=2)

#====================Results Frame====================  
label2 = tk.Label(resultsFrame, text="Machnumber =").grid(row=0, column=0)
label3 = tk.Label(resultsFrame, text="p/p0 =").grid(row=1, column=0)
label4 = tk.Label(resultsFrame, text="p/p* =").grid(row=2, column=0)

led_2 = tk.Entry(resultsFrame, text="")
led_2.grid(row=0, column=1)
led_3 = tk.Entry(resultsFrame, text="")
led_3.grid(row=1, column=1)
led_4 = tk.Entry(resultsFrame, text="")
led_4.grid(row=2, column=1)

label5 = tk.Label(resultsFrame, text="Mach angle =").grid(row=0, column=2)
label6 = tk.Label(resultsFrame, text="rho/rho0 =").grid(row=1, column=2)
label7 = tk.Label(resultsFrame, text="rho/rho* =").grid(row=2, column=2)

led_5 = tk.Entry(resultsFrame, text="")
led_5.grid(row=0, column=3)
led_6 = tk.Entry(resultsFrame, text="")
led_6.grid(row=1, column=3)
led_7 = tk.Entry(resultsFrame, text="")
led_7.grid(row=2, column=3)

label8 = tk.Label(resultsFrame, text="P-M angle =").grid(row=0, column=4)
label9 = tk.Label(resultsFrame, text="T/T0 =").grid(row=1, column=4)
label10 = tk.Label(resultsFrame, text="T/T* =").grid(row=2, column=4)

led_8 = tk.Entry(resultsFrame, text="")
led_8.grid(row=0, column=5)
led_9 = tk.Entry(resultsFrame, text="")
led_9.grid(row=1, column=5)
led_10 = tk.Entry(resultsFrame, text="")
led_10.grid(row=2, column=5)

label9 = tk.Label(resultsFrame, text="Ma* =").grid(row=0, column=6)
label10 = tk.Label(resultsFrame, text="...").grid(row=1, column=6)
label11 = tk.Label(resultsFrame, text="A/A* =").grid(row=2, column=6)

led_9 = tk.Entry(resultsFrame, text="")
led_9.grid(row=0, column=7)
led_10 = tk.Entry(resultsFrame, text="")
led_10.grid(row=1, column=7)
led_11 = tk.Entry(resultsFrame, text="")
led_11.grid(row=2, column=7)





root.mainloop()

