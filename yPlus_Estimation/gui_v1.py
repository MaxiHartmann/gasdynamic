import tkinter as tk
import math as m

class window_1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        input_frame = tk.Frame(self.frame, bd=2, relief=tk.RIDGE)
        output_frame = tk.Frame(self.frame, bd=2, relief=tk.RIDGE)

        # input_1: U_inf
        self.val_1 = tk.StringVar()
        self.lbl_input_1 = tk.Label(input_frame, text='U_inf = ').grid(row=0, column=0, padx=5)
        self.entry_input_1 = tk.Entry(input_frame, textvariable=self.val_1, bg='white', width=10).grid(row=0, column=1, padx=10)
        self.val_1.set('1.0')
        self.lbl_unit_1 = tk.Label(input_frame, text='[m/s]').grid(row=0, column=2, padx=5)

        # input_2: rho_inf
        self.val_2 = tk.StringVar()
        self.lbl_input_2 = tk.Label(input_frame, text='rho_inf = ').grid(row=1, column=0, padx=5)
        self.entry_input_2 = tk.Entry(input_frame, textvariable=self.val_2, bg='white', width=10).grid(row=1, column=1, padx=10)
        self.val_2.set('1.205')
        self.lbl_unit_2 = tk.Label(input_frame, text='[kg/m3]').grid(row=1, column=2, padx=5)

        # input_3: mu_inf
        self.val_3 = tk.StringVar()
        self.lbl_input_3 = tk.Label(input_frame, text='mu_inf = ')
        self.lbl_input_3.grid(row=2, column=0, padx=5)
        self.entry_input_3 = tk.Entry(input_frame, textvariable=self.val_3, bg='white', width=10)
        self.entry_input_3.grid(row=2, column=1, padx=10)
        self.val_3.set('1.82e-5')
        self.lbl_unit_3 = tk.Label(input_frame, text='[kg/ms]').grid(row=2, column=2, padx=5)

        # input_4: Characteristic Length
        self.val_4 = tk.StringVar()
        self.lbl_input_4 = tk.Label(input_frame, text='L_turb = ')
        self.lbl_input_4.grid(row=3, column=0, padx=5)
        self.entry_input_4 = tk.Entry(input_frame, textvariable=self.val_4, bg='white', width=10)
        self.entry_input_4.grid(row=3, column=1, padx=10)
        self.val_4.set('1.0')
        self.lbl_unit_4 = tk.Label(input_frame, text='[m]').grid(row=3, column=2, padx=5)

        # input_5: Desired Y+ value
        self.val_5 = tk.StringVar()
        self.lbl_input_5 = tk.Label(input_frame, text='Y+ = ')
        self.lbl_input_5.grid(row=4, column=0, padx=5)
        self.entry_input_5 = tk.Entry(input_frame, textvariable=self.val_5, bg='white', width=10)
        self.entry_input_5.grid(row=4, column=1, padx=10)
        self.val_5.set('1.0')
        self.lbl_unit_5 = tk.Label(input_frame, text='[-]').grid(row=4, column=2, padx=5)


        title_label_1 = tk.Label(self.frame, text='INPUT-Values:', font='Helvetica 18 bold')
        title_label_1.grid(row=2)
        #input_frame.pack(expand=1, fill=tk.X, pady=10, padx=5)
        input_frame.grid()


        # output_1: Reynolds number 
        self.out_val_1 = tk.StringVar()
        self.lbl_output_1 = tk.Label(output_frame, text='Re = ')
        self.lbl_output_1.grid(row=0, column=0, padx=5)
        self.entry_output_1 = tk.Entry(output_frame, textvariable=self.out_val_1, bg='white', width=10)
        self.entry_output_1.grid(row=0, column=1, padx=10)
        self.out_val_1.set('')
        self.lbl_unit_7 = tk.Label(output_frame, text='[-]')
        self.lbl_unit_7.grid(row=0, column=2, padx=5)

        # output_2: Estimated wall distance
        self.out_val_2 = tk.StringVar()
        self.lbl_output_2 = tk.Label(output_frame, text='y = ')
        self.lbl_output_2.grid(row=1, column=0, padx=5)
        self.entry_output_2 = tk.Entry(output_frame, textvariable=self.out_val_2, bg='white', width=10)
        self.entry_output_2.grid(row=1, column=1, padx=10)
        self.out_val_2.set('')
        self.lbl_unit_7 = tk.Label(output_frame, text='[m]')
        self.lbl_unit_7.grid(row=1, column=2, padx=5)

        title_label_2 = tk.Label(self.frame, text='OUTPUT-Values:', font='Helvetica 18 bold')
        title_label_2.grid(row=2)
        # output_frame.pack(expand=1, fill=tk.X, pady=10, padx=5)
        output_frame.grid()


        # Buttons
        self.button1 = tk.Button(self.frame, text = 'Calculate', width = 25, command = self.calc)
        self.button1.grid(row=3)
        self.button2 = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_window)
        self.button2.grid(row=4)
        self.frame.grid()
    def calc(self):
        u_inf = float(self.val_1.get())
        rho_inf = float(self.val_2.get())
        mu_inf = float(self.val_3.get())
        L = float(self.val_4.get())
        yPlus = float(self.val_5.get())

        Re_L = rho_inf * u_inf * L / mu_inf
        C_f = (2 * m.log(Re_L) - 0.65)**(-2.3)
        tau_w = C_f * rho_inf * u_inf * u_inf
        u_star = m.sqrt(tau_w / rho_inf)
        y = yPlus * mu_inf / (rho_inf * u_star)

        self.out_val_1.set('{:.03e}'.format(Re_L))
        self.out_val_2.set('{:.03e}'.format(y))
    def close_window(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = window_1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
