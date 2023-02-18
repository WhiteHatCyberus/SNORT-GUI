import os
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *
if os.path.exists('.setup.conf'):
    messagebox.showinfo("Your Application is ready","All resources are downloaded and ready to be launched")
    os.system('sudo python3 snortgui.py')
else:
    #tkinter window declaration : Progressbar
    snort = Tk()
    snort.geometry('300x120')
    snort.title('Setup Wizard')

    #########################
    #exit
    def mQuit():
        mexit=messagebox.askokcancel(title='Exit',message='Are you sure?')
        if mexit>0:
            snort.destroy()
            return
    #main
    def run_commands():
        button1.place_forget()
        button.place(x=30,y=80)
        with open('requirements.txt','r') as f:
            commands = f.readlines()

        progress_bar['maximum'] = len(commands)

        for i, command in enumerate(commands):
            command = command.strip()
            button['text']=f'Downloading Components ({i+1}/{len(commands)})'
            os.system(command)
            progress_bar['value']=i+1
            snort.update()
        with open('.setup.conf','w') as f:
            f.write("This is a configuration file to tell the wizard a first time installation")
            
        result=messagebox.askyesno('Installation complete','Yes will start the GUI shortly')
        if result==True:
            snort.destroy()
            os.system("python3 snortgui.py")
        else:
            snort.destroy()


    #progress bar css
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Custom.Horizontal.TProgressbar', foreground='#51C9C2', background='#C7F7F5', thickness=25)
    progress_bar=ttk.Progressbar(snort, orient='horizontal', mode = 'determinate', style='Custom.Horizontal.TProgressbar',length=200)
    progress_bar.pack(pady=40)

    #button css
    button=tk.Button(snort,text='Proceed', command=run_commands)
    button1=tk.Button(snort,text='Cancel', command=mQuit)
    button.place(x=155,y=80)
    button1.place(x=65,y=80)
    
    #messagelabel
    message_label=tk.Label(snort,text='Press Proceed to download resources')
    message_label.place(x=30,y=10)
    snort.mainloop()