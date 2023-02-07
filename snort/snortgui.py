from tkinter import *
from tkinter import Frame
import PIL
from PIL import *
from PIL import ImageTk
from PIL import Image
snort = Tk()
snort.resizable(width=None, height=None)
#snort.wm_iconbitmap('labris.ico')
#snort.withdraw()
snort.geometry('1370x755+1+1')
#400+100 the position on the screen
#800x400 screen size

#Title of tkinter
snort.title('Intrusion Detection System - Made By WhiteHatCyberus')

# Create an object of tkinter ImageTk

img =Image.open('/home/matty/Desktop/snort/Gui-Snort-Rule-Generator/snort.jpg')
bg = ImageTk.PhotoImage(img)
# Add image
label = Label(snort, image=bg)
label.place(x = 0,y = 20)
button = Button(snort, text="GENERATE RULES", bg="#000", fg="#fff", width=30, height=5, activebackground="#f00", activeforeground="#fff")
button.pack(padx=0,pady=100)
#snort.resizable(False,False)
snort.mainloop()