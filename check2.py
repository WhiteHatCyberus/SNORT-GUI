import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

# create the main window
root = tk.Tk()
root.title('Intrusion Detection System - Made By WhiteHatCyberus')
root.geometry('1200x650+1+1')
root.resizable(False, False)

# create a canvas to display the background image
canvas = tk.Canvas(root, width=1200, height=650)
canvas.pack(fill=tk.BOTH, expand=True)

# load and display the background image
img = Image.open('snort.jpg')
img = img.resize((1200, 650), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

# define the functions for the buttons
def generate_rules():
    os.system('python3 rule_generator.py')

def open_files():
    filename = filedialog.askopenfilename(initialdir='/etc/snort/rules/', title='Select File',
                                          filetypes=(('SNORT Rules', '*.rules'), ('config', '*.conf')))
    if filename:
        subprocess.run(['sudo', 'gedit', filename])

def run_ids():
    os.system('python3 ids.py')

def exit_app():
    if messagebox.askokcancel(title='Exit', message='Are you sure?'):
        root.destroy()

# create the buttons
button_width, button_height = 20, 2
button_font = ('TkDefaultFont', 15)
button_bg, button_fg = '#000', '#fff'
button_active_bg, button_active_fg = '#f00', '#fff'

generate_button = tk.Button(root, width=button_width, height=button_height, text='GENERATE RULES', font=button_font,
                            bg=button_bg, fg=button_fg, relief='groove', cursor='hand2', activebackground=button_active_bg,
                            activeforeground=button_active_fg, command=generate_rules)
generate_button.place(x=45, y=150)

open_button = tk.Button(root, width=button_width, height=button_height, text='OPEN FILES', font=button_font,
                        bg=button_bg, fg=button_fg, relief='groove', cursor='hand2', activebackground=button_active_bg,
                        activeforeground=button_active_fg, command=open_files)
open_button.place(x=45, y=300)

run_button = tk.Button(root, width=button_width, height=button_height, text='RUN IDS', font=button_font,
                       bg=button_bg, fg=button_fg, relief='groove', cursor='hand2', activebackground=button_active_bg,
                       activeforeground=button_active_fg, command=run_ids)
run_button.place(x=45, y=450)

# create the menu bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Exit', command=exit_app)
file_menu.add_command(label='About')
menu_bar.add_cascade(label='Files', menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
