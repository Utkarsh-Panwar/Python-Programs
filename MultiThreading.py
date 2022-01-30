# -*- coding: utf-8 -*-
import threading
import time
from tkinter import Tk, Button

root = Tk()

def just_wait(seconds):
     
     for x in range(1,100):
         print('\nOutput from ',threading.currentThread().getName(),x)
         time.sleep(seconds)
         if(x==10):
            my_thread2.start()
        
def just_wait2(seconds):
     
     for x in range(1,100):
         print('\nOutput from ',threading.currentThread().getName(),x)  
         time.sleep(seconds)
         if(x==10):
            my_thread3.start()
            
def just_wait3(seconds):
     
     for x in range(1,100):
         print('\nOutput from ',threading.currentThread().getName(),x)  
         time.sleep(seconds)
         if(x==10):
            my_thread._delete()
            
         

def button_callback():
    # Without the thread, the button will stay depressed and the
    # program will respond until the function has returned
    my_thread.start()
    
my_thread = threading.Thread(target=just_wait,args=(1,))
my_thread.setName("Thread-1")
    
my_thread2 = threading.Thread(target=just_wait2, args=(1,))
my_thread2.setName("Thread-2")

my_thread3 = threading.Thread(target=just_wait3, args=(1,))
my_thread3.setName("Thread-3")

button = Button(root, text='Run long thread.', command=button_callback)
button.pack()

# Without them pressing a button that performs
# a long action will pause the entire program and it 
# Will appear as if the program froze - Note about the GIL and only maximizing one cpu

root.mainloop()