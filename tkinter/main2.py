#!/usr/bin/python3

"""
Machnumber-relation
based on:

http://www.dept.aoe.vt.edu/~devenpor/aoe3114/calc.html

"""

# import numpy as np
from myfunctions import *

# constants: ideal Gas
gamma = 1.4
gasConst = 287.058
Cp = gamma * gasConst / (gamma - 1)

# INPUT
Ma = 2.0
# Ma = float(input("Enter Machnumber: "))

# CALCULATION
MaStar = calc_MaStar(Ma)
TRatio = calc_TdT0(Ma)
pdp0 = calc_pdp0(Ma)
rhodrho0 = (1 + (gamma - 1) / 2 * Ma**2)**(-1 / (gamma - 1))
rhodrho0 = calc_rhodrho0(Ma)
AdAstar = calc_AdAstar(Ma)
MachAngle = calc_MachAngle(Ma)
PM_angle = calc_PM_Angle(Ma)
T_Tstar = 1. / (Ma / MaStar)**2
rho_rhoStar = 1. / AdAstar * (1./MaStar)
p_pstar = rho_rhoStar * T_Tstar

# OUTPUT
print("Ma       = {:.04f}".format(Ma))
print("Ma*      = {:.04f}".format(MaStar))
print("Mach-angle = {:.05f}".format(MachAngle))
print("PM-angle = {:.05f}".format(PM_angle))
print("p/pt     = {:.05f}".format(pdp0))
print("rho/rhot = {:.05f}".format(rhodrho0))
print("T/Tt     = {:.05f}".format(TRatio))

print("p/p*     = {:.05f}".format(p_pstar))
print("rho/rho* = {:.05f}".format(rho_rhoStar))
print("T/T*     = {:.05f}".format(T_Tstar))
print("A/A*     = {:.05f}".format(AdAstar))

print("Ma(0, 2.0) = {:.05f}".format(calcMachnumber(0, 2.0)))
print("Ma(1, 0.55555) = {:.05f}".format(calcMachnumber(1, 0.555555)))
print("Ma(2, 0.12780452) = {:.05f}".format(calcMachnumber(2, 0.12780452)))
print("Ma(3, 0.23004814) = {:.05f}".format(calcMachnumber(3, 0.23004814)))
print("Ma(4(sub), 1.68749999) = {:.05f}".format(calcMachnumber(4, 1.68749999)))
print("Ma(5(sup), 1.68749999) = {:.05f}".format(calcMachnumber(5, 1.68749999)))
print("Ma(6, 30) = {:.05f}".format(calcMachnumber(6, 30)))
print("Ma(7, 26.3798) = {:.05f}".format(calcMachnumber(7, 26.3797608)))


#********** GUI ********** 

import tkinter as tk

#==================== Frames ====================  
root = tk.Tk()
# root.geometry('1200x600+10+10')

inputFrame = tk.Frame(root, bg='green', width=1200, height=100)
inputFrame.pack(side=tk.TOP, fill=tk.X,)

resultsFrame = tk.Frame(root, bg='blue', width=1200, height=500)
resultsFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)

#====================Variables ====================  
txt_inputValue = tk.StringVar(value="2.0")
my_dict1={0: 'Machnumber', 1: 'Colors', 2: 'Games', 3: 'Vehicles'}

# txt_inputType = tk.StringVar(inputFrame, value=inputType[0])
txt_inputType = tk.StringVar(inputFrame, value=my_dict1[0])

txt_Machnumber = tk.StringVar()
txt_MachAngle = tk.StringVar()
txt_PM_Angle = tk.StringVar()
txt_MachStar = tk.StringVar()

txt_pdp0 = tk.StringVar()
txt_rhodrho0 = tk.StringVar()
txt_TdT0 = tk.StringVar()

txt_pdpStar = tk.StringVar()
txt_rhodrhoStar = tk.StringVar()
txt_TdTstar = tk.StringVar()
txt_AdAstar = tk.StringVar()

#====================Methods ====================  
def calc():
    print("reset and Calc")
    reset()
    Ma = float(led_1.get())
    # print("Machnumber = {}".format(Ma))
    led_2.insert(0,"{:.04f}".format(float(led_1.get())))
    # print("InputType = {}".format(lsbox_1.get()))
    #
    MaStar = calc_MaStar(Ma)
    led_MaStar.insert(0,"{:.04f}".format(MaStar))

    TRatio = calc_TdT0(Ma)
    pdp0 = calc_pdp0(Ma)
    led_3.insert(0,"{:.04f}".format(pdp0))


    AdAstar = calc_AdAstar(Ma)
    led_AdAstar.insert(0,"{:.04f}".format(AdAstar))

    rhodrho0 = calc_rhodrho0(Ma)
    MachAngle = calc_MachAngle(Ma)
    PM_angle = calc_PM_Angle(Ma)
    T_Tstar = 1. / (Ma / MaStar)**2
    rho_rhoStar = 1. / AdAstar * (1./MaStar)
    p_pstar = rho_rhoStar * T_Tstar

def reset():
    led_2.delete(0,tk.END)
    led_3.delete(0,tk.END)
    led_AdAstar.delete(0,tk.END)
    led_MaStar.delete(0,tk.END)


def display_selected(choice):
    print(choice)

# def my_show():
#     print(txt_inputType.get())

def my_show(*args):
    for i,j in my_dict1.items():
        if j == txt_inputType.get():
            print(i)

#====================INPUT Line====================  
lbl_name = tk.Label(inputFrame, text="Isentropic Flow Calculator",
        bg='green', font=('arial', 20, 'bold'))
lbl_name.grid(row=0, column=0)
lbl_input = tk.Label(inputFrame, text="INPUT:")
lbl_input.grid(row=1, column=0)
lsbox_1 = tk.OptionMenu(inputFrame, txt_inputType, *my_dict1.values(), command=display_selected)
lsbox_1.grid(row=1, column=1)

led_1 = tk.Entry(inputFrame, textvariable=txt_inputValue)
led_1.grid(row=1, column=2)
btn_calc = tk.Button(inputFrame, text="Calculate", fg="red", command=calc)
btn_calc.grid(row=1, column=3)

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

led_MaStar = tk.Entry(resultsFrame, text="")
led_MaStar.grid(row=0, column=7)
led_11 = tk.Entry(resultsFrame, text="")
led_11.grid(row=1, column=7)
led_AdAstar = tk.Entry(resultsFrame, text="")
led_AdAstar.grid(row=2, column=7)

txt_inputType.trace('w', my_show)
root.mainloop()

