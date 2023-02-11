import os
from tkinter import *
from tkinter import Frame
import PIL
from PIL import *
from PIL import ImageTk
from PIL import Image
import tkinter.font as fnt
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import subprocess
snort = Tk()
#Title of tkinter
snort.title('Intrusion Detection System - Made By WhiteHatCyberus')
snort.resizable(width=None, height=None)
#snort.wm_iconbitmap('labris.ico')
#snort.withdraw()
snort.geometry('1200x650+1+1')
# Open the Image File

bg = ImageTk.PhotoImage(file="/home/matty/Desktop/snort/snort.jpg")

# Create a Canvas
canvas = Canvas(snort, width=1200, height=650)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open('/home/matty/Desktop/snort/snort.jpg')
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
snort.bind("<Configure>", resize_image)
canvas.place(x=0, y=0)
################################################################################################
#functions
def function1():
    
    os.system("python3 rule_generator.py")

#exit
def mQuit():
    mexit=messagebox.askokcancel(title='Exit',message='Are you sure?')
    if mexit>0:
        snort.destroy()
        return
#OpenFiles
def FOpen():
    snort.filename=filedialog.askopenfilename(initialdir="/etc/snort/rules/",title="Select File",filetypes=(("SNORT Rules","*.rules"),("config","*.conf")))
    subprocess.run(["sudo","gedit",snort.filename])
#################################################################################################
#buttons
button = Button(snort, width=20, height=2,text="GENERATE RULES", font = fnt.Font(size = 15), cursor="hand2",bg="#000", relief="groove", fg="#fff",command=function1,activebackground="#f00", activeforeground="#fff")
button.place(x=45, y=150)
button = Button(snort, width=20, height=2, text="OPEN FILES", font = fnt.Font(size = 15), cursor="hand2",bg="#000", relief="groove", fg="#fff",command=FOpen,activebackground="#f00", activeforeground="#fff")
button.place(x=45, y=300)
button = Button(snort, width=20, height=2, text="RUN IDS", font = fnt.Font(size = 15), cursor="hand2",bg="#000", relief="groove", fg="#fff",command=function1,activebackground="#f00", activeforeground="#fff")
button.place(x=45, y=450)

#button.pack(padx=0,pady=150)
frame = Frame(snort,height = 50, width = 100)
#################################################################################
#Menus
menubar=Menu(frame)

#Menu
filemenu=Menu(menubar,tearoff=0)

#filemenu.add_command(label="Colour", command=mColor)
filemenu.add_command(label="Exit",command=mQuit)
filemenu.add_command(label="About")
menubar.add_cascade(label="Files",menu=filemenu)


snort.config(menu=menubar)
snort.resizable(False, False)
snort.mainloop()
