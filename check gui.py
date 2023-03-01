import os
import subprocess
from tkinter import *
from tkinter import font, ttk, messagebox, filedialog
from PIL import Image, ImageTk

# Create the main window
snort = Tk()
snort.title('Intrusion Detection System - Made By WhiteHatCyberus')
snort.geometry('1200x650+1+1')
snort.resizable(False, False)
'''
# Create the canvas and add an image
canvas = Canvas(snort, width=1200, height=650)
canvas.pack(fill=BOTH, expand=True)

image = Image.open('snort.jpg')
resized = image.resize((1200, 650), Image.ANTIALIAS)
image2 = ImageTk.PhotoImage(resized)
canvas.create_image(0, 0, image=image2, anchor='nw')

# Resize the image when the window is resized
def resize_image(e):
   global image, resized, image2
   image = Image.open('snort.jpg')
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

snort.bind("<Configure>", resize_image)
'''
# Define functions
def generate_rules():
    os.system("python3 rule_generator.py")

def open_files():
    filename = filedialog.askopenfilename(initialdir="/etc/snort/rules/", title="Select File",
                                          filetypes=(("SNORT Rules", "*.rules"), ("config", "*.conf")))
    if filename:
        subprocess.run(["sudo", "gedit", filename])

def run_ids():
    # Add code here to run IDS
    pass

def quit_app():
    if messagebox.askokcancel(title='Exit', message='Are you sure?'):
        snort.destroy()

# Create buttons
button_font = font.Font(size=15)
button_color = "#000"
button_active_color = "#f00"
button_text_color = "#fff"
button_relief = "groove"

generate_button = Button(snort, width=20, height=2, text="GENERATE RULES", font=button_font,
                         cursor="hand2", bg=button_color, relief=button_relief,
                         fg=button_text_color, activebackground=button_active_color,
                         activeforeground=button_text_color, command=generate_rules)
generate_button.place(x=45, y=150)

open_button = Button(snort, width=20, height=2, text="OPEN FILES", font=button_font,
                     cursor="hand2", bg=button_color, relief=button_relief,
                     fg=button_text_color, activebackground=button_active_color,
                     activeforeground=button_text_color, command=open_files)
open_button.place(x=45, y=300)

run_button = Button(snort, width=20, height=2, text="RUN IDS", font=button_font,
                    cursor="hand2", bg=button_color, relief=button_relief,
                    fg=button_text_color, activebackground=button_active_color,
                    activeforeground=button_text_color, command=run_ids)
run_button.place(x=45, y=450)

# Create menu
menubar = Menu(snort)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=quit_app)
filemenu.add_command(label="About")

menubar.add_cascade(label="Files", menu=filemenu)
snort.config(menu=menubar)

snort.mainloop()
