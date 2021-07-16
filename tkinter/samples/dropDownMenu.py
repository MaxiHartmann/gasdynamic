import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

app = tk.Tk()

app.geometry('600x400')
# app.resizable(width=False, height=False)

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=45, font=('Helvetica', 12))
opt.grid(row=0, column=0)

app.mainloop()
