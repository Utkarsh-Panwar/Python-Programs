# -*- coding: utf-8 -*-

from tkinter import *
 
'''
root = Tk() # Create the root (base) window where all widgets go
w = Label(root, text="Hello, world!") # Create a label with words
w.pack() # Put the label into the window
root.mainloop() # Start the event loop
#Windows go into an “event loop” where they wait for things to happen (buttons pushed, text entered, mouse clicks, etc…) or Windowing operations to be needed (redraw,layout,size etc..). You must tell the root window to enter its event loop or the window won’t be displayed!
'''

'''
root = Tk() 
w = Label(root, text="Hello, world!") 
w.pack() 
myButton = Button(root, text="Exit")
myButton.pack()
root.mainloop() 
'''
 
'''
root = Tk() 
w = Label(root, text="Hello, world!") 
w.pack() 
def buttonClicked():
    print("Button Clicked")
myButton = Button(root, text="Exit",command=buttonClicked)
myButton.pack()
root.mainloop() 
'''

'''
from tkinter import *

root = None
def buttonPushed():
    # Hold onto a global reference for the root window
    global root
    root.destroy() 
def main():
    global root
    root = Tk()  
    w = Label(root, text="Hello, world!") 
    w.pack() 
    myButton = Button(root, text="Exit",command=buttonPushed)
    myButton.pack()
    root.mainloop() 
main()
'''


from tkinter import *

root = None
entryBox = None

def buttonPushed():
    global entryBox
    txt = entryBox.get()
    print("The text is:",txt)
def createTextBox(parent):
    global entryBox
    entryBox = Entry(parent)
    entryBox.pack()
def main():
    global root
    root = Tk() 
    myButton = Button(root, text="Show Text",command=buttonPushed)
    myButton.pack()
    createTextBox(root)
    root.mainloop() 
main()
