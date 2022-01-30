# -*- coding: utf-8 -*-

from tkinter import *



class Frame1( Frame ):
    def __init__( self ):
        Frame.__init__(self)
        self.pack()
        self.master.title("UTKARSH")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, 
                          sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = Frame2()
class Frame2(Frame):     
    def __init__(self):
        new =Frame.__init__(self)
        new = Toplevel(self)
        new.title("Utkarsh New Window")
        new.button = Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    Frame1().mainloop()

main()
