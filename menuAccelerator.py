# -*- coding: utf-8 -*-


from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.bind_all("<Control-f>", lambda event: self.menu_file())
        menubar = Menu(self)
        fileMenu = Menu(menubar, tearoff=False)
        fileMenu.add_command(label="File", underline=0, 
                             command=self.menu_file,
                             accelerator="Control+F")
#        fileMenu.add_command(label="File", underline=0, 
#                             command=self.menu_file)
        menubar.add_cascade(label="File",underline=0, menu=fileMenu)
        self.config(menu=menubar)

    def menu_file(self):
        print("Executed")

app=App()
app.mainloop()