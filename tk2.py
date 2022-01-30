# -*- coding: utf-8 -*-

from tkinter import *

#root = None
#myText = None
#count = 0 
#
#def buttonPushed():
#     global myText
#     global count
#     count += 1
#     myText.set("Stop your clicking, it's already been %d times!" %(count))
#
#def addTextLabel(root):
#     global myText
#     myText = StringVar()
#     myText.set("")
#     myLabel = Label(root, textvariable=myText)
#     myLabel.pack()
#
#def main():
#     global root
#     root = Tk() 
#     myButton = Button(root, text="Show Text",command=buttonPushed)
#     myButton.pack()
#     addTextLabel(root)
#     root.mainloop()
#    
#main()

#--------------------Layout Mangement----------------------------------


#root = None
#count = 0 
#
#def addButton(root, sideToPack):
#    global count
#    name = "Button "+ str(count) +" "+sideToPack
#    button = Button(root, text=name)
#    button.pack(side=sideToPack)
#    count +=1
#    
#def main():
#    global root
#    root = Tk() 
#    for i in range(5):
#        addButton(root, BOTTOM)
#    root.mainloop()
#        
#main()





#root = None
#count = 0 
#
#def addButton(root, sideToPack):
#    global count
#    name = "Button "+ str(count) +" "+sideToPack
#    button = Button(root, text=name)
#    button.pack(side=sideToPack)
#    count +=1
#def main():
#    global root
#    root = Tk() 
#    addButton(root, LEFT) 
#    addButton(root, BOTTOM) 
#    addButton(root, RIGHT) 
#    addButton(root, TOP) 
#    root.mainloop()
#
#main()


#-----------------------Using Frames---------------------------------------------
#Frame are widgets that hold other widgets. (Frames are parents).



root = None
count = 0 

def addButton(root, sideToPack):
    global count
    name = "Button "+ str(count) +" "+sideToPack
    button = Button(root, text=name)
    button.pack(side=sideToPack)
    count +=1
def main():
    global root
    root = Tk() 
    root.configure(background="red")
    frame1 = Frame(root, highlightbackground="green", highlightthickness=5)
    addButton(frame1 , LEFT)
    addButton(frame1 , LEFT)
    addButton(frame1 , LEFT)
    addButton(frame1 , LEFT)
    addButton(frame1 , LEFT)
   
    frame2 = Frame(root, highlightbackground="blue", highlightthickness=5)
    addButton(frame2 , TOP)
    addButton(frame2 , TOP)
    addButton(frame2 , TOP)
    addButton(frame2 , TOP)
    addButton(frame2 , TOP)
    
    frame3 = Frame(root, highlightbackground="brown", highlightthickness=5)
    addButton(frame3 , BOTTOM)
    addButton(frame3 , BOTTOM)
    addButton(frame3 , BOTTOM)
    addButton(frame3 , BOTTOM)
    addButton(frame3 , BOTTOM)
    
    frame1.pack(side=TOP)
    frame2.pack(side=LEFT)
    frame3.pack(side=RIGHT)
    root.mainloop()

main()
