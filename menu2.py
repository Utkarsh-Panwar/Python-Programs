# -*- coding: utf-8 -*-


from tkinter import *
def do_something():
    print("Doing something")
    
root = Tk()
# create a menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

#Insert sub-menu here
submenu = Menu(menu) # create a new menu
filemenu.add_cascade(label="New",menu=submenu) # attach it to a parent menu
submenu.add_command(label="Text File", command=do_something)
submenu.add_command(label="Graphics File", command=do_something)

#carry on with the filemenu
filemenu.add_separator()
filemenu.add_command(label="Exit", command=do_something)

mainloop()