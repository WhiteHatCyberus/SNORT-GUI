import os
import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import ImageTk, Image
import psutil


with open('.resources/temp/admin.pass', 'r') as file:
    sudo_passwd = file.read()

i=3
try:
    while i>0:
        sudo_password = simpledialog.askstring("Password", "\nEnter your administrator password:\n", show='*')

        if sudo_password==sudo_passwd:
            try:
                i=0
                # create the main window
                snort = tk.Tk()
                snort.title('Simulation Environment Configuration')
                snort.geometry('900x650+1+1')
                snort.resizable(False, False)        

                # create a canvas to display the background image
                canvas1 = tk.Canvas(snort, width=900, height=650)
                canvas1.pack(fill=tk.BOTH, expand=True)

                # load and display the background image
                img1 = Image.open('.resources/info/images/sim_art.png')
                img1 = img1.resize((875, 500), Image.ANTIALIAS)
                img1 = ImageTk.PhotoImage(img1)
                canvas1.create_image(10, 20, image=img1, anchor=tk.NW)

                label = tk.Label(canvas1, text='Configurable Network Interface:')
                label.grid(row=0, column=0, padx=10, pady=550)

                def run_sim():
                    if interface_var.get()=='':
                        messagebox.showerror('Error', 'Please select a network interface!')
                    else:
                        cmd='sudo -S ifconfig '+ interface_var.get()+ ' 192.168.1.0 netmask 255.255.255.0'
                        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, preexec_fn=os.setsid)
                        process.stdin.write(sudo_password.encode('utf-8') + b'\n')
                        process.stdin.flush()
                        messagebox.showinfo("Configuration Success", "Your system is ready for simulation (your ip:192.168.1.0)")
                        exit()
                interface_var = tk.StringVar()
                interface_menu = tk.OptionMenu(canvas1, interface_var, *psutil.net_if_addrs().keys())
                interface_menu.grid(row=0, column=1, padx=5, pady=550)

                initalise_button=tk.Button(canvas1, text='Initialise SNORT Environment', width=25, height=1, bg='blue', fg='white', command=run_sim)
                initalise_button.grid(row=0, column=2, padx=250, pady=550)

                snort.mainloop()
            except tk.TclError:
                break
        elif(sudo_password is None):
            exit()
        elif(sudo_password==""):
            messagebox.showerror("Error","Enter password")
        else:
            i=i-1
            messagebox.showerror("Error", "ⓘ Incorrect password, try again. (Attempts Left:"+str(i)+")")
            
except tk.TclError:
    exit()
