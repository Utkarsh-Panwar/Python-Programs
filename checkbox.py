# -*- coding: utf-8 -*-
#import tkinter as tk
#
#root = tk.Tk()
#
#kar = tk.IntVar()
#cb = tk.Checkbutton(root, text="the lights are on", variable=kar)
#cb.pack()
#
#def showstate():
#     if kar.get():
#         print("the lights are on")
#         print(kar.get())
#        
#     else:
#         print("the lights are off")
#         print(kar.get())
#
#button = tk.Button(root, text="show state", command=showstate)
#button.pack()
#
#root.mainloop()


'''
from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.destroy).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
master.mainloop()
'''


# from tkinter import *
    
# x = Tk()
# y=Listbox(x)
# y.pack()
# def glst():
#     #print(y.get(ACTIVE))
#     #y.insert(2,"Hello")
#     #y.delete(2)
#     #y.delete(0,END)
#     x.configure(background=y.get(ACTIVE))
#     y.configure(background=y.get(ACTIVE))
    
# b=Button(x,text="get",command=glst)
# b.pack()
# y.insert(END, "Listbox")

# for names in ["Adil", "John", "Eric", "Edward","red"]:
#     y.insert(END, names)

#     if names=="Adil":
#         y.insert(END,"Erica")
                         
# mainloop()



# from tkinter import *

# window = Tk()
# window.title("Welcome to Techguru")
# selected = IntVar()
# rad1 = Radiobutton(window,text='First', value=1, variable=selected)
# rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
# rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
# def clicked():
#     print(selected.get())
# btn = Button(window, text="Click Me", command=clicked)
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)
# btn.grid(column=3, row=0)
# window.mainloop()




from tkinter import *
    
x = Tk()
y=Listbox(x)
y.grid(row=0,column=0)
z=Listbox(x)
z.grid(row=0,column=1)
def glst():
    if y.get(ACTIVE)=="Cars":
        z.delete(0,END)
        for values in ["Bugati-Vyron", "Mers-SClass", "BMW-Z","Audi-R8"]:
            z.insert(END, values)
    elif y.get(ACTIVE)=="Bikes":
        z.delete(0,END)
        for values in ["Ninja H2R", "Ducati-Panigalle", "Suzuki-BKing","Honda FireBlade"]:
            z.insert(END, values)
    elif y.get(ACTIVE)=="Fighter Jets":
        z.delete(0,END)
        for values in ["Sukhoi 30MKI", "F22 Raptor", "Euro Fighter","Rafel"]:
            z.insert(END, values)
        
    
    
b=Button(x,text="fill",command=glst)
b.grid(column=0,row=1)


for values in ["Cars", "Bikes", "Fighter Jets"]:
    y.insert(END, values)

    
                         
mainloop()
