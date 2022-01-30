# -*- coding: utf-8 -*-


# from tkinter import Tk
# root = Tk()

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# print("Screen width:", screen_width)
# print("Screen height:", screen_height)



# from tkinter import Tk
# root = Tk()

# root.attributes('-fullscreen', True)

# root.mainloop()



# from tkinter import Tk, Message
# root = Tk()

# msg = Message(root, text='Hello, world!')

# # Font is a tuple of (font_family, size_in_points, style_modifier_string)
# msg.config(font=('times', 100, 'italic bold underline'))

# msg.pack()

# root.mainloop()

'''
from tkinter import Tk, Label, Y, RIGHT
root = Tk()

label1 = Label(root, text='Yellow!', background='yellow')
label2 = Label(root, text='Orange?', background='orange')

# Some of the packing options:
# - fill: tells the widget to expand to take up any extra space (X, Y, or BOTH)
# - padx/pady: outter padding
# - ipadx/ipady: inner padding
# - side: which side to stack from. Default is TOP (to bottom)

label1.pack(fill=Y, padx=25,pady=30, ipady=55, side=RIGHT)  # Pack from right to left
label2.pack(fill=Y, padx=25, ipady=15, side=RIGHT)

root.mainloop()
'''

'''
from tkinter import Tk, Label
root = Tk()

# Labels do not have a command option like buttons
# but you can manually attach the click event to a callback
label = Label(root, text='I am a label. Click me.')
label.pack()

def my_callback():
    print('Label was clicked.')

# Bind mouse button 1 click on label
label.bind("<Button-1>", lambda e:my_callback())



root.mainloop()
'''


import threading
import time
from tkinter import Tk, Button

root = Tk()

def just_wait(seconds):
    print('Waiting for ', seconds, ' seconds...')
    time.sleep(seconds)
    print('Done sleeping.')

def button_callback():
    my_thread = threading.Thread(target=just_wait, args=(5,))
    my_thread.start()

button = Button(root, text='Run long thread.', command=button_callback)
button.pack()

#Without them pressing a button that performs
#a long action will pause the entire program and it 
#Will appear as if the program froze - Note about the GIL and only maximizing one cpu

root.mainloop()



# from tkinter import Tk, Toplevel, Button
# root = Tk()

# # Create new top level window. Opens immediately
# second_window = Toplevel()
# second_window.title('Second window')

# # Destroy window
# def destroy_second_window():
#     second_window.destroy()

# close_button = Button(
#     root,
#     text='Close second window',
#     command=destroy_second_window
# )
# close_button.pack()

# root.mainloop()



'''
from tkinter import Tk, Toplevel
root = Tk()

second_window = Toplevel()
second_window.title('Second window')

# Focus on window
second_window.focus_force()

root.mainloop()
'''


'''
from tkinter import Tk, Canvas
root = Tk()

canv = Canvas(root, width=200, height=100)
canv.pack()

# Draw blue line from top left to bottom right with wide dashes
canv.create_line(0, 0, 200, 100, fill='blue')

# Draw green rectangle at (100,50) to (120,55)
canv.create_rectangle(100, 50, 120, 55, fill='green')

# Draw oval(circle) from (20,20) to (40,40)
canv.create_oval(20, 20, 40, 40,fill='red')

root.mainloop()
'''


# from tkinter import *  
# from PIL import ImageTk,Image  
# root = Tk()  
# canvas = Canvas(root, width = 300, height = 300)  
# canvas.pack()  
# img = ImageTk.PhotoImage(Image.open("football.jpg"))  
# canvas.create_image(20, 20, anchor=NW, image=img)  
# root.mainloop()  
