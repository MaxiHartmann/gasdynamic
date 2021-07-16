"""

TODO: 
- OOP-structure 
- reach widgets in each frame from extern functions
- isentropic Flow ...
- normal Shock...
  ....

"""

import tkinter as tk
from tkinter import ttk
from myfunctions import *

LARGE_FONT=("Verdana", 12)

class SeaofBTCapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Gasdynamic Calculator")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


# Example: How to reach tk-widgets from outside of class:
def reset(self):
    self.led_2.delete(0,tk.END)
    self.led_3.delete(0,tk.END)
    self.led_4.delete(0,tk.END)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Isentropic Flow Relations",
                command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Normal Shock Relations",
                command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Oblique Shock Relations",
                command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self, text="Conical Shock Relations",
                command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button5 = ttk.Button(self, text="Fanno Flow",
                command=lambda: controller.show_frame(PageFive))
        button5.pack()

        button6 = ttk.Button(self, text="Rayleigh Flow",
                command=lambda: controller.show_frame(PageSix))
        button6.pack()


class PageOne(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #==================== Frames ====================  
        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP)

        inputFrame = tk.Frame(self, bg='green', width=1200)
        inputFrame.pack(side=tk.TOP, fill=tk.X)

        resultsFrame = tk.Frame(self, bg='blue', width=1200, height=500)
        resultsFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        #====================Variables ====================  
        txt_inputValue = tk.StringVar(value="2.0")
        txt_gamma = tk.StringVar(value="1.4")
        self.my_dict1={0: 'Machnumber', 
                  1: 'T/T0', 
                  2: 'p/p0', 
                  3: 'rho/rho0',
                  4: 'A/A*(sub)',
                  5: 'A/A*(sup)',
                  6: 'Mach angle (deg.)',
                  7: 'P-M angle (deg.)'}
        keys=list(self.my_dict1.keys())
        values=self.my_dict1.values()

        self.txt_inputType = tk.StringVar(inputFrame, value=self.my_dict1[0])

        # TEST:
        self.testButton = tk.Button(self, text="TEST :::", bg='yellow')
                # command=lambda: testFunction(self))
        self.testButton.bind('<Button-1>', self.testFunction)
        self.testButton.pack()
        self.testLabel = tk.Label(self, text="TEST :::", bg='yellow')
        self.testLabel.pack()

        #====================INPUT Line====================  
        self.lbl_name = tk.Label(inputFrame, text="Isentropic Flow Calculator",
                bg='green', font=('arial', 20, 'bold'))
        self.lbl_name.grid(row=0, column=0)
        self.lbl_input = tk.Label(inputFrame, text="INPUT:")
        self.lbl_input.grid(row=1, column=0, sticky=tk.E)
        self.lsbox_1 = tk.OptionMenu(inputFrame, self.txt_inputType, *self.my_dict1.values())
        self.lsbox_1.config(width=16)
        self.lsbox_1.grid(row=1, column=1)
        self.lbl_input = tk.Label(inputFrame, text="gamma = ")
        self.lbl_input.grid(row=0, column=2, sticky=tk.E)
        self.led_gamma = tk.Entry(inputFrame, textvariable=txt_gamma, width=8)
        self.led_gamma.grid(row=0, column=3)
        
        self.led_1 = tk.Entry(inputFrame, textvariable=txt_inputValue, width=10)
        self.led_1.grid(row=1, column=2)
        self.btn_calc = tk.Button(inputFrame, text="Calculate", fg="red")
        self.btn_calc.bind('<Button-1>', self.calc)
        self.btn_calc.grid(row=1, column=3)
        self.btn_reset = tk.Button(inputFrame, text="RESET", fg="red", 
                command=lambda: reset(self))
        self.btn_reset.grid(row=2, column=3)

        #====================Results Frame====================  
        self.label2 = tk.Label(resultsFrame, text="Machnumber =")
        self.label2.grid(row=0, column=0, sticky=tk.E)
        self.label3 = tk.Label(resultsFrame, text="p/p0 =")
        self.label3.grid(row=1, column=0, sticky=tk.E)
        self.label4 = tk.Label(resultsFrame, text="p/p* =")
        self.label4.grid(row=2, column=0, sticky=tk.E)

        self.led_2 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_2.grid(row=0, column=1)
        self.led_3 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_3.grid(row=1, column=1)
        self.led_4 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_4.grid(row=2, column=1)

    #====================Methods ====================  
    def calc(self,event):
        print("reset and Calc")

        # get idx in OptionMenu:
        inputType = self.get_idx_fromOptionMenu(self.txt_inputType.get())
        inputValue=float(self.led_1.get())
        gamma=float(self.led_gamma.get())

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
        self.led_2.insert(0,"{:.07f}".format(Ma))
        self.led_3.insert(0,"{:.07f}".format(pdp0))
        self.led_4.insert(0,"{:.07f}".format(pdpstar))

    def get_idx_fromOptionMenu(self, search_key):
        for idx, option in self.my_dict1.items():
            if option == search_key:
                # print("idx = {}, search_key= {}".format(idx, option))
                return idx

    def testFunction(self, event):
        print("TEST-Function")
        self.testLabel.config(text="xxx")


#================================================================================
#==========      Page Two        ==================================================
#================================================================================

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                command=lambda: controller.show_frame(PageOne))
        button2.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Four!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                command=lambda: controller.show_frame(PageOne))
        button2.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Five!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Six!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()

if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()
