"""

TODO: 
- oblique Shock 
- maybe encapsulation:
  separate classes

"""

import tkinter as tk
from tkinter import ttk
import isentropicFlow as isenFlow
import normalShock as ns

LARGE_FONT=("Verdana", 12)

class ContentOverview(tk.Tk):
    
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

        inputFrame = tk.Frame(self, bg='green', width=1200, height=200)
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
        
        self.e_inputValue = tk.Entry(inputFrame, textvariable=txt_inputValue, width=10)
        self.e_inputValue.grid(row=1, column=2)
        self.btn_calc = tk.Button(inputFrame, text="Calculate", fg="red")
        self.btn_calc.bind('<Button-1>', self.calc)
        self.e_inputValue.bind('<Return>', self.calc)
        self.btn_calc.grid(row=1, column=3)
        #====================Results Frame====================  
        label2 = tk.Label(resultsFrame, text="Machnumber =").grid(row=0, column=0, sticky=tk.E)
        label3 = tk.Label(resultsFrame, text="p/p0 =").grid(row=1, column=0, sticky=tk.E)
        label4 = tk.Label(resultsFrame, text="p/p* =").grid(row=2, column=0, sticky=tk.E)

        self.led_2 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_2.grid(row=0, column=1)
        self.led_3 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_3.grid(row=1, column=1)
        self.led_4 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_4.grid(row=2, column=1)

        label5 = tk.Label(resultsFrame, text="Mach angle =")
        label5.grid(row=0, column=2, sticky=tk.E)
        label6 = tk.Label(resultsFrame, text="rho/rho0 =")
        label6.grid(row=1, column=2, sticky=tk.E)
        label7 = tk.Label(resultsFrame, text="rho/rho* =")
        label7.grid(row=2, column=2, sticky=tk.E)

        self.led_5 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_5.grid(row=0, column=3)
        self.led_6 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_6.grid(row=1, column=3)
        self.led_7 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_7.grid(row=2, column=3)

        label8 = tk.Label(resultsFrame, text="P-M angle =")
        label8.grid(row=0, column=4, sticky=tk.E)
        label9 = tk.Label(resultsFrame, text="T/T0 =")
        label9.grid(row=1, column=4, sticky=tk.E)
        label10 = tk.Label(resultsFrame, text="T/T* =")
        label10.grid(row=2, column=4, sticky=tk.E)

        self.led_8 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_8.grid(row=0, column=5)
        self.led_9 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_9.grid(row=1, column=5)
        self.led_10 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_10.grid(row=2, column=5)

        label11 = tk.Label(resultsFrame, text="Ma* =")
        label11.grid(row=0, column=6, sticky=tk.E)
        label12 = tk.Label(resultsFrame, text="...")
        label12.grid(row=1, column=6, sticky=tk.E)
        label13 = tk.Label(resultsFrame, text="A/A* =")
        label13.grid(row=2, column=6, sticky=tk.E)

        self.led_MaStar = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_MaStar.grid(row=0, column=7)
        self.led_11 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_11.grid(row=1, column=7)
        self.led_AdAstar = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.led_AdAstar.grid(row=2, column=7)

    def calc(self, event):
        print("reset and Calc")
        self.reset()

        # get idx in OptionMenu:
        inputType = self.get_idx_fromOptionMenu(self.txt_inputType.get())
        inputValue=float(self.e_inputValue.get())
        gamma=float(self.led_gamma.get())

        Ma = isenFlow.calcMachnumber(inputType, inputValue, gamma)
        pdp0 = isenFlow.calc_pdp0(Ma,gamma)
        MachAngle = isenFlow.calc_MachAngle(Ma)
        rhodrho0 = isenFlow.calc_rhodrho0(Ma, gamma)
        TRatio = isenFlow.calc_TdT0(Ma,gamma)
        PM_angle = isenFlow.calc_PM_Angle(Ma,gamma)
        MaStar = isenFlow.calc_MaStar(Ma, gamma)
        AdAstar = isenFlow.calc_AdAstar(Ma, gamma)
        rho_rhoStar = 1. / AdAstar * (1./MaStar)
        T_Tstar = 1. / (Ma / MaStar)**2
        pdpstar = rho_rhoStar * T_Tstar

        # column=0
        self.led_2.insert(0,"{:.07f}".format(Ma))
        self.led_3.insert(0,"{:.07f}".format(pdp0))
        self.led_4.insert(0,"{:.07f}".format(pdpstar))

        # column=1
        self.led_5.insert(0,"{:.07f}".format(MachAngle))
        self.led_6.insert(0,"{:.07f}".format(rhodrho0))
        self.led_7.insert(0,"{:.07f}".format(rho_rhoStar))

        # column=2
        self.led_8.insert(0,"{:.07f}".format(PM_angle))
        self.led_9.insert(0,"{:.07f}".format(TRatio))
        self.led_10.insert(0,"{:.07f}".format(T_Tstar))

        # column=3
        self.led_MaStar.insert(0,"{:.07f}".format(MaStar))
        self.led_11.insert(0, "...")
        self.led_AdAstar.insert(0,"{:.07f}".format(AdAstar))

    def get_idx_fromOptionMenu(self, search_key):
        for idx, option in self.my_dict1.items():
            if option == search_key:
                # print("idx = {}, search_key= {}".format(idx, option))
                return idx

    def reset(self):
        self.led_2.delete(0,tk.END)
        self.led_3.delete(0,tk.END)
        self.led_4.delete(0,tk.END)
        self.led_5.delete(0,tk.END)
        self.led_6.delete(0,tk.END)
        self.led_7.delete(0,tk.END)
        self.led_8.delete(0,tk.END)
        self.led_9.delete(0,tk.END)
        self.led_10.delete(0,tk.END)
        self.led_AdAstar.delete(0,tk.END)
        self.led_11.delete(0,tk.END)
        self.led_MaStar.delete(0,tk.END)



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Normal Shock Relations", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()

        inputFrame = tk.Frame(self, bg='green', width=1200, height=100)
        inputFrame.pack()

        resultsFrame = tk.Frame(self, bg='blue', width=1200, height=400)
        resultsFrame.pack(fill=tk.BOTH)

        # self.statusbar = tk.Label(self, text="status:", bd=1, relief=tk.SUNKEN)
        # self.statusbar.pack(side=tk.BOTTOM, anchor=tk.SW)

        #====================Variables ====================  
        txt_inputValue = tk.StringVar(value="2.0")
        txt_gamma = tk.StringVar(value="1.4")
        self.my_dict1={0: 'Ma1', 
                  1: 'Ma2', 
                  2: 'p2/p1', 
                  3: 'rho2/rho1',
                  4: 'T2/T1',
                  5: 'p02/p01',
                  6: 'p1/p02'}
        keys=list(self.my_dict1.keys())
        values=self.my_dict1.values()

        self.txt_inputType = tk.StringVar(inputFrame, value=self.my_dict1[0])

        #====================INPUT Line====================  
        self.lbl_name = tk.Label(inputFrame, text="Normal Shock Relations",
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
        
        self.e_inputValue = tk.Entry(inputFrame, textvariable=txt_inputValue, width=10)
        self.e_inputValue.grid(row=1, column=2)
        self.btn_calc = tk.Button(inputFrame, text="Calculate", fg="red")
        self.btn_calc.grid(row=1, column=3)
        self.btn_calc.bind('<Button-1>', self.calc)
        self.e_inputValue.bind('<Return>', self.calc)
        
        #====================Results Frame====================  
        label_Ma1 = tk.Label(resultsFrame, text="Ma1 =")
        label_Ma1.grid(row=0, column=0, sticky=tk.E)
        label_p2dp1 = tk.Label(resultsFrame, text="p2/p1 =")
        label_p2dp1.grid(row=1, column=0, sticky=tk.E)
        self.e_Ma1 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_Ma1.grid(row=0, column=1)
        self.e_p2dp1 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_p2dp1.grid(row=1, column=1)

        label_Ma2 = tk.Label(resultsFrame, text="Ma2 = ")
        label_Ma2.grid(row=0, column=2, sticky=tk.E)
        label_rho2drho1 = tk.Label(resultsFrame, text="rho2/rho1 = ")
        label_rho2drho1.grid(row=1, column=2, sticky=tk.E)
        self.e_Ma2 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_Ma2.grid(row=0, column=3)
        self.e_rho2drho1 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_rho2drho1.grid(row=1, column=3)

        label_p02dp01 = tk.Label(resultsFrame, text="p02/p01 = ")
        label_p02dp01.grid(row=0, column=4, sticky=tk.E)
        label_T2dT1 = tk.Label(resultsFrame, text="T2/T1 = ")
        label_T2dT1.grid(row=1, column=4, sticky=tk.E)
        self.e_p02dp01 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_p02dp01.grid(row=0, column=5)
        self.e_T2dT1 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_T2dT1.grid(row=1, column=5)

        label_p1dp02 = tk.Label(resultsFrame, text="p1/p02 = ")
        label_p1dp02.grid(row=0, column=6, sticky=tk.E)
        self.e_p1dp02 = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_p1dp02.grid(row=0, column=7)

        label_Ma1star = tk.Label(resultsFrame, text="Ma1* = ")
        label_Ma1star.grid(row=0, column=8, sticky=tk.E)
        label_Ma2star = tk.Label(resultsFrame, text="Ma2* = ")
        label_Ma2star.grid(row=1, column=8, sticky=tk.E)
        self.e_Ma1star = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_Ma1star.grid(row=0, column=9)
        self.e_Ma2star = tk.Entry(resultsFrame, text="", justify='right', width=12)
        self.e_Ma2star.grid(row=1, column=9)

    def reset(self):
        self.e_Ma1.delete(0,tk.END)
        self.e_Ma2.delete(0,tk.END)
        self.e_p2dp1.delete(0,tk.END)
        self.e_p02dp01.delete(0,tk.END)
        self.e_p1dp02.delete(0,tk.END)
        self.e_T2dT1.delete(0,tk.END)
        self.e_rho2drho1.delete(0,tk.END)
        self.e_Ma1star.delete(0,tk.END)
        self.e_Ma2star.delete(0,tk.END)

    def calc(self, event):
        print("reset and Calc")
        self.reset()

        inputType = self.get_idx_fromOptionMenu(self.txt_inputType.get())
        inputValue=float(self.e_inputValue.get())
        gamma=float(self.led_gamma.get())

        Ma1 = ns.calcInflowMachnumber(inputType, inputValue, gamma)
        Ma2 = ns.calc_Ma2(Ma1, gamma)
        p2dp1 = ns.calc_p2dp1(Ma1, gamma)
        rho2drho1 = ns.calc_rho2drho1(Ma1, gamma)
        T2dT1 = ns.calc_T2dT1(Ma1, gamma)
        p02dp01 = ns.calc_p02dp01(Ma1, gamma)
        p1dp02 = ns.calc_p1dp02(Ma1, gamma)
        Ma1star = ns.calc_MaStar(Ma1, gamma)
        Ma2star = ns.calc_MaStar(Ma2, gamma)

        # column=0
        self.e_Ma1.insert(0,"{:.07f}".format(Ma1))
        self.e_p2dp1.insert(0,"{:.07f}".format(p2dp1))

        # column=1
        self.e_Ma2.insert(0,"{:.07f}".format(Ma2))
        self.e_rho2drho1.insert(0,"{:.07f}".format(rho2drho1))

        # column=2
        self.e_p02dp01.insert(0,"{:.07f}".format(p02dp01))
        self.e_T2dT1.insert(0,"{:.07f}".format(T2dT1))

        # column=3
        self.e_p1dp02.insert(0,"{:.07f}".format(p1dp02))
        self.e_Ma1star.insert(0,"{:.07f}".format(Ma1star))
        self.e_Ma2star.insert(0,"{:.07f}".format(Ma2star))

    def get_idx_fromOptionMenu(self, search_key):
        for idx, option in self.my_dict1.items():
            if option == search_key:
                return idx


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Oblique Shock Relations", font=LARGE_FONT)
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
    app = ContentOverview()
    app.mainloop()
