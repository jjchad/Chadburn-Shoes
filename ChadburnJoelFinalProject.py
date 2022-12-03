"""
Author: Joel Chadburn
Program: ChadburnShoes
Date of Last Revision: 12/3/22
The purpose of this program is to allow users to view information about
various shoes from 'Chadburn Shoes.' This program will also allow users to
enter personal information in order to 'place' an order.
"""
from tkinter import * #imports tkinter
from PIL import ImageTk, Image # imports the tools from pillow to allow dynamic backround image resizing.
root = Tk() #creates and opens the main gui window
root.title("Chadburn Shoes") #gives the window/program a name
root.geometry("1200x512") #sets the size of the main window
bg = ImageTk.PhotoImage(file = r"C:\Users\bruin\Desktop\ChadburnJoelFinalProject\ChadburnShoesGraphics\HomePageChadburnShoes2.png") #sets variable to image
homeCanvas = Canvas(root, width = 1200, height = 512) #sets size of the canvas(matches the root.geometry size)
homeCanvas.pack(fill = "both", expand = True) # configures canvas settings
homeCanvas.create_image(0,0, image = bg, anchor = "nw")#puts my desired image onto the canvas
ourStoryButton = Button(root, text = "Our Story", font = ("Helvetica", 30), fg = "white") # Creates 'our story button' with desired style
ourStoryButtonWindow = homeCanvas.create_window(300, 256, anchor="nw", window = ourStoryButton) # Places the Button over the top of the canvas
seeOurShoesButton = Button(root, text = "See Our Shoes", font = ("Helvetica", 30), fg = "white")
seeOurShoesButtonWindow = homeCanvas.create_window(700, 256, anchor="nw", window = seeOurShoesButton)
def resizer(e): #this function allows the program backround to dynamically resize when the window is resized
    global bg1, resized_bg, new_bg
    bg1 = Image.open(r"C:\Users\bruin\Desktop\ChadburnJoelFinalProject\ChadburnShoesGraphics\HomePageChadburnShoes2.png")
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized_bg)
    homeCanvas.create_image(0,0, image = new_bg, anchor = "nw")
    
root.bind('<Configure>', resizer) #passes argument size argument to the resizer function
root.mainloop() #ensures that the mainloop is continuously traversed until the program is closed.

