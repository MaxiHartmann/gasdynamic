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
pRatio = calc_dpd0(Ma)
rhoRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-1 / (gamma - 1))
rhoRatio = calc_rhodrho0(Ma)
AdAstar = calc_AdAstar(Ma)
MachAngle = calc_MachAngle(Ma)
PM_angle = calc_PM_Angle(Ma)
T_Tstar = 1. / (Ma / MaStar)**2
rho_rhoStar = 1. / AdAstar * (1./MaStar)
p_pstar = rho_rhoStar * T_Tstar

# OUTPUT
# print("Ma       = {:.04f}".format(Ma))
# print("Ma*      = {:.04f}".format(MaStar))
# print("Mach-angle = {:.05f}".format(MachAngle))
# print("PM-angle = {:.05f}".format(PM_angle))
# print("p/pt     = {:.05f}".format(pRatio))
# print("rho/rhot = {:.05f}".format(rhoRatio))
# print("T/Tt     = {:.05f}".format(TRatio))
# 
# print("p/p*     = {:.05f}".format(p_pstar))
# print("rho/rho* = {:.05f}".format(rho_rhoStar))
# print("T/T*     = {:.05f}".format(T_Tstar))
# print("A/A*     = {:.05f}".format(AdAstar))

print("Ma(0, 2.0) = {:.05f}".format(calcMachnumber(0, 2.0)))
print("Ma(1, 0.5) = {:.05f}".format(calcMachnumber(1, 0.5)))
print("Ma(2, 0.5) = {:.05f}".format(calcMachnumber(2, 0.5)))
print("Ma(3, 0.5) = {:.05f}".format(calcMachnumber(3, 0.5)))
print("Ma(4(sub), 1.5) = {:.05f}".format(calcMachnumber(4, 1.5)))
print("Ma(5(sup), 1.5) = {:.05f}".format(calcMachnumber(5, 1.5)))
print("Ma(6, 30) = {:.05f}".format(calcMachnumber(6, 30)))
print("Ma(7, 26.3798) = {:.05f}".format(calcMachnumber(7, 26.3797608)))

#********** GUI ********** 

import tkinter as tk

class App:
    def __init__(self, root):
        root.title("Perfect Gas Calculator")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        lbl_input=tk.Label(root, text="INPUT: ")
        lbl_input.grid(row=0, column=0)

        OptionList = [
                "Machnumber",
                "Taurus",
                "Gemini",
                "Cancer"
                ] 
        variable = tk.StringVar(root)
        variable.set(OptionList[0])
        lsbox_1=tk.OptionMenu(root,variable, *OptionList, command=self.display_selected)
        lsbox_1.grid(row=0, column=1)

        led_INPUT=tk.Entry(root, text="2.0")
        led_INPUT.grid(row=0, column=2)

        btn_calc=tk.Button(root, text="Calculate",command=self.calc)
        btn_calc.grid(row=0, column=3)

    def calc(self):
        print("command")

    def display_selected(self, choice):
        print(choice)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
