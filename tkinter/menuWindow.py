# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
# import matplotlib.animation as animation
# from matplotlib import style

import tkinter as tk
from tkinter import ttk
from myfunctions import *

LARGE_FONT=("Verdana", 12)
# style.use("dark_background")

# Plotting:
# f = Figure(figsize=(5,5), dpi=100)
# a = f.add_subplot(111)
# # a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
# 
# 
# def animate(i):
#     pullData = open("sampleData.txt", "r").read()
#     dataList = pullData.split('\n')
#     xList = []
#     yList = []
#     for eachLine in dataList:
#         if len(eachLine) > 1:
#             x, y = eachLine.split(',')
#             xList.append(int(x))
#             yList.append(int(y))
# 
#     a.clear()
#     a.plot(xList, yList)

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
        inputFrame = tk.Frame(self, bg='green', width=1200)
        inputFrame.pack(side=tk.TOP, fill=tk.X)
        label = tk.Label(self, text="Isentropic Flow Relations", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        resultsFrame = tk.Frame(self, bg='blue', width=1200, height=500)
        resultsFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        button1 = ttk.Button(self, text="Back to Home",
                command=lambda: controller.show_frame(StartPage))
        button1.pack()

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
        btn_calc = tk.Button(inputFrame, text="Calculate", fg="red", 
                command=calc)
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

# Nice: Live Plotting
# class PageThree(tk.Frame):
# 
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
# 
#         button1 = ttk.Button(self, text="Back to Home",
#                 command=lambda: controller.show_frame(StartPage))
#         button1.pack()
# 
#         canvas = FigureCanvasTkAgg(f, self)
#         canvas.draw()
#         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# 
#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# 
# ani = animation.FuncAnimation(f, animate, interval=1000)

app = SeaofBTCapp()
app.mainloop()
