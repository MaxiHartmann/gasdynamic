#!/usr/bin/python3

"""
Machnumber-relation
based on:

http://www.dept.aoe.vt.edu/~devenpor/aoe3114/calc.html

"""

# import numpy as np
from myfunctions import *

# constants: ideal Gas
# gamma = 1.4
# gasConst = 287.058
# Cp = gamma * gasConst / (gamma - 1)

#********** GUI ********** 
import tkinter as tk

#==================== Frames ====================  
root = tk.Tk()
# root.geometry('1200x600+10+10')

inputFrame = tk.Frame(root, bg='green', width=1200)
inputFrame.pack(side=tk.TOP, fill=tk.X)

resultsFrame = tk.Frame(root, bg='blue', width=1200, height=500)
resultsFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)

#====================Variables ====================  
txt_inputValue = tk.StringVar(value="2.0")
txt_gamma = tk.StringVar(value="1.4")
my_dict1={0: 'Machnumber', 
          1: 'T/T0', 
          2: 'p/p0', 
          3: 'rho/rho0',
          4: 'A/A*(sub)',
          5: 'A/A*(sup)',
          6: 'Mach angle (deg.)',
          7: 'P-M angle (deg.)'}
keys=list(my_dict1.keys())
values=my_dict1.values()

txt_inputType = tk.StringVar(inputFrame, value=my_dict1[0])

#====================Methods ====================  
def calc():
    print("reset and Calc")
    reset()

    # get idx in OptionMenu:
    inputType = get_idx_fromOptionMenu(txt_inputType.get())
    inputValue=float(led_1.get())
    gamma=float(led_gamma.get())

    Ma = calcMachnumber(inputType, inputValue, gamma)
    pdp0 = calc_pdp0(Ma,gamma)
    MachAngle = calc_MachAngle(Ma)
    rhodrho0 = calc_rhodrho0(Ma, gamma)
    TRatio = calc_TdT0(Ma,gamma)
    PM_angle = calc_PM_Angle(Ma,gamma)
    MaStar = calc_MaStar(Ma, gamma)
    AdAstar = calc_AdAstar(Ma, gamma)
    rho_rhoStar = 1. / AdAstar * (1./MaStar)
    T_Tstar = 1. / (Ma / MaStar)**2
    pdpstar = rho_rhoStar * T_Tstar

    # column=0
    led_2.insert(0,"{:.07f}".format(Ma))
    led_3.insert(0,"{:.07f}".format(pdp0))
    led_4.insert(0,"{:.07f}".format(pdpstar))

    # column=1
    led_5.insert(0,"{:.07f}".format(MachAngle))
    led_6.insert(0,"{:.07f}".format(rhodrho0))
    led_7.insert(0,"{:.07f}".format(rho_rhoStar))

    # column=2
    led_8.insert(0,"{:.07f}".format(PM_angle))
    led_9.insert(0,"{:.07f}".format(TRatio))
    led_10.insert(0,"{:.07f}".format(T_Tstar))

    # column=3
    led_MaStar.insert(0,"{:.07f}".format(MaStar))
    # led_11.insert(...)
    led_AdAstar.insert(0,"{:.07f}".format(AdAstar))

def get_idx_fromOptionMenu(search_key):
    for idx, option in my_dict1.items():
        if option == search_key:
            # print("idx = {}, search_key= {}".format(idx, option))
            return idx

def reset():
    led_2.delete(0,tk.END)
    led_3.delete(0,tk.END)
    led_4.delete(0,tk.END)
    led_5.delete(0,tk.END)
    led_6.delete(0,tk.END)
    led_7.delete(0,tk.END)
    led_8.delete(0,tk.END)
    led_9.delete(0,tk.END)
    led_10.delete(0,tk.END)
    led_AdAstar.delete(0,tk.END)
    led_MaStar.delete(0,tk.END)

# def my_show(*args):
#     for i,j in my_dict1.items():
#         if j == txt_inputType.get():
#             int_inputType = i
#             # print(int_inputType)

#====================INPUT Line====================  
lbl_name = tk.Label(inputFrame, text="Isentropic Flow Calculator",
        bg='green', font=('arial', 20, 'bold'))
lbl_name.grid(row=0, column=0)
lbl_input = tk.Label(inputFrame, text="INPUT:")
lbl_input.grid(row=1, column=0, sticky=tk.E)
lsbox_1 = tk.OptionMenu(inputFrame, txt_inputType, *my_dict1.values())
lsbox_1.config(width=16)
lsbox_1.grid(row=1, column=1)
lbl_input = tk.Label(inputFrame, text="gamma = ")
lbl_input.grid(row=0, column=2, sticky=tk.E)
led_gamma = tk.Entry(inputFrame, textvariable=txt_gamma, width=8)
led_gamma.grid(row=0, column=3)

led_1 = tk.Entry(inputFrame, textvariable=txt_inputValue, width=10)
led_1.grid(row=1, column=2)
btn_calc = tk.Button(inputFrame, text="Calculate", fg="red", command=calc)
btn_calc.grid(row=1, column=3)

#====================Results Frame====================  
label2 = tk.Label(resultsFrame, text="Machnumber =").grid(row=0, column=0, sticky=tk.E)
label3 = tk.Label(resultsFrame, text="p/p0 =").grid(row=1, column=0, sticky=tk.E)
label4 = tk.Label(resultsFrame, text="p/p* =").grid(row=2, column=0, sticky=tk.E)

led_2 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_2.grid(row=0, column=1)
led_3 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_3.grid(row=1, column=1)
led_4 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_4.grid(row=2, column=1)

label5 = tk.Label(resultsFrame, text="Mach angle =")
label5.grid(row=0, column=2, sticky=tk.E)
label6 = tk.Label(resultsFrame, text="rho/rho0 =")
label6.grid(row=1, column=2, sticky=tk.E)
label7 = tk.Label(resultsFrame, text="rho/rho* =")
label7.grid(row=2, column=2, sticky=tk.E)

led_5 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_5.grid(row=0, column=3)
led_6 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_6.grid(row=1, column=3)
led_7 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_7.grid(row=2, column=3)

label8 = tk.Label(resultsFrame, text="P-M angle =")
label8.grid(row=0, column=4, sticky=tk.E)
label9 = tk.Label(resultsFrame, text="T/T0 =")
label9.grid(row=1, column=4, sticky=tk.E)
label10 = tk.Label(resultsFrame, text="T/T* =")
label10.grid(row=2, column=4, sticky=tk.E)

led_8 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_8.grid(row=0, column=5)
led_9 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_9.grid(row=1, column=5)
led_10 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_10.grid(row=2, column=5)

label11 = tk.Label(resultsFrame, text="Ma* =")
label11.grid(row=0, column=6, sticky=tk.E)
label12 = tk.Label(resultsFrame, text="...")
label12.grid(row=1, column=6, sticky=tk.E)
label13 = tk.Label(resultsFrame, text="A/A* =")
label13.grid(row=2, column=6, sticky=tk.E)

led_MaStar = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_MaStar.grid(row=0, column=7)
led_11 = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_11.grid(row=1, column=7)
led_AdAstar = tk.Entry(resultsFrame, text="", justify='right', width=12)
led_AdAstar.grid(row=2, column=7)

# GUI : Normal Shock Relations
# ...

root.mainloop()

