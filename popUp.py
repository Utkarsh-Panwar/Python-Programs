# -*- coding: utf-8 -*-


from tkinter import *


# root = Tk()

# w = Label(root, text="Right-click to display menu", width=40, height=20)
# w.pack()

# # create a menu
# popup = Menu(root, tearoff=0)
# popup.add_command(label="Next") # , command=next) etc...
# popup.add_command(label="Previous")
# popup.add_separator()
# popup.add_command(label="Home")

# def do_popup(event):
#     # display the popup menu
#     try:
#         popup.tk_popup(event.x_root, event.y_root)
#     finally:
#         # make sure to release the grab (Tk 8.0a1 only)
#         popup.grab_release()

# root.bind("<Button-3>", do_popup)

# b = Button(root, text="Quit", command=root.destroy)
# b.pack()

# mainloop()



class PopupMenuDemo( Frame ):
    def __init__( self ):
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Popup Menu Demo" )
      self.master.geometry( "300x200" )

      self.frame1 = Frame( self, bg = "white" )
      self.frame1.pack( expand= YES, fill = BOTH )
      
      self.menu = Menu( self.frame1, tearoff = 0 )

      colors = [ "White", "Blue", "Yellow", "Red", "Pink", "Gray", "Purple"]
      self.selectedColor = StringVar()
      self.selectedColor.set( colors[ 0 ] )
      
      for item in colors:
          self.menu.add_radiobutton( label = item,
            variable = self.selectedColor,
            command = self.changeBackgroundColor )

      self.frame1.bind( "<Button-3>", self.popUpMenu )

    def popUpMenu( self, event ):
      self.menu.post( event.x_root, event.y_root )

    def changeBackgroundColor( self ):
      self.frame1.config( bg = self.selectedColor.get() )
      
def main():
    PopupMenuDemo().mainloop()   

