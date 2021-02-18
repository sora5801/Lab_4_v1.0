import tkinter as tk
import sqlite3
from Client1 import Client



class GUI:
    def __init__(self):
        con = sqlite3.connect('SQLite_Python.db')
        cursorObj = con.cursor()
        con.cursor()
        sel = 'SELECT DISTINCT Country FROM UN'
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()
        temp = list()
        for i in rows:
            temp.append(i[0])
        OptionList = temp
        self.C = Client(5000)
        self.app = tk.Tk()
        self.app.title("UNData")

        self.app.geometry('300x400')

        self.variable = tk.StringVar(self.app)
        self.variable.set(OptionList[0])

        self.opt = tk.OptionMenu(self.app, self.variable, *OptionList, command=self.C.Connect)
        self.opt.config(width=90, font=('Helvetica', 12))
        self.opt.pack(side="top")

        self.labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
        self.labelTest.pack(side="top")

        self.app.mainloop()


