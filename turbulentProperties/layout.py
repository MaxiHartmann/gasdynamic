import tkinter as tk
from tkinter import ttk

def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    ttk.Label(frame, text='Freestream velocity: U_inf ').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)
    
    ttk.Label(frame, text='Turbulence kinetic energy ').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    ttk.Label(frame, text='Turbulence dissipation ').grid(column=0, row=2, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=2, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame

def create_main_window():
    

    # root window
    root = tk.Tk()
    root.title('Turbulent Properties')
    root.geometry('400x150')
    root.resizable(0, 0)

    input_frame = create_input_frame(root)
    input_frame.grid(row=0, column=0)
    
    root.mainloop()


if __name__ == "__main__":
    create_main_window()
