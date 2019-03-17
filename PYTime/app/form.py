from tkinter import *
from app.controller import AppController

class AppForm:
    def __init__(self):
        self.control = AppController()
        self.form = Tk()
        #
        # Form 
        #
        self.form.title("App")
        self.form.geometry('350x200')
        #
        # Label
        #
        self.lbl = Label(self.form, text="Worked")
        self.lbl.grid(column=0, row=0)
        #
        # Text
        #
        self.txt = Entry(self.form,width=10)
        self.txt.grid(column=1, row=0)
        #
        # Button
        #
        self.btn = Button(self.form, text="Click Me", command=self.btn_onClick)
        self.btn.grid(column=2, row=0)

    def btn_onClick(self):
        self.lbl.configure(text = self.control.calculate())
    
    def show(self):
        self.form.mainloop()