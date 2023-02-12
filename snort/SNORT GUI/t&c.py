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
snort = Tk()
#Title of tkinter
snort.title('SNORT GUI v1.0.0')
#window size
snort.resizable(width=False, height=False)
snort.geometry('800x700+1+1')
snort.config(bg='#808080')
'''
frame=Frame(snort)
frame.pack(expand=True, fill=BOTH, padx=20,pady=30)
lb=Listbox(frame,font=(12))
lb.pack(expand=True, fill=BOTH,side=LEFT)
sb=Scrollbar(frame,orient=VERTICAL)
sb.pack(fill=Y,side=RIGHT)
lb.configure(yscrollcommand=sb.set)
sb.config(command=lb.yview)
lb.insert(0,'Terms and Conditions')
lb.insert(1,'____________________________________________________________')
'''
#scroll bar
v=Scrollbar(snort, orient='vertical')
v.pack(side=RIGHT, fill='y')
# text boxes
T = Text(snort, width = 64, height=26, background="#ffffff", foreground="#000000", font = ('Sans Serif',13,'italic bold'))
T.tag_configure("heading", justify='center')
T.insert(INSERT, "Terms and Conditions")
T.tag_add("heading","1.0","end")
T.pack()
T.place(x=10,y=10)
T1 = Text(snort, width = 68, height=23, background="#ffffff", foreground="#000000", font = ('Sans Serif',13),yscrollcommand=v.set)
T1.tag_configure("body", justify='left')
T1.insert(INSERT, "\n You are using the SNORT GUI developed by White Hat Cyberus!\n Developed by 4 students from Rajagiri School of Engineering and Technology in\n January, 2023. This is a Open Source Software, so feel free to check out the code.\n https://github.com/WhiteHatCyberus\n \n Disclaimer: \n To be used for personal, educational and enterprise purposes. \n \n What is SNORT? \n SNORT is a Open Source Intrusion Detection System / Intrusion Prevention System \n maintained by Cisco Talos. \n \n Note: This application will monitor your network in real time and access your \n administrative directories. For proper functioning, run the application in 'sudo' \n mode. Manipulating this application for malicious purposes is not entertained.")
#T1.tag_add("body","1.0","end")
v.config(command=T1.yview)
T1.pack()
T1.place(x=20,y=50)

#############################################
#exit
def mQuit():
    mexit=messagebox.askokcancel(title='Exit',message='Are you sure you want to cancel the setup?')
    if mexit>0:
        snort.destroy()
        return
#buttons
button = Button(snort, width=6, height=2,text="Accept", font = fnt.Font(size = 15), cursor="hand2",bg="#000", relief="groove", fg="#fff",activebackground="grey72", activeforeground="#fff")
button.place(x=550, y=600)
button = Button(snort, width=6, height=2,text="Decline", font = fnt.Font(size = 15), cursor="hand2",bg="#000", relief="groove", fg="#fff",activebackground="grey72", activeforeground="#fff", command=mQuit)
button.place(x=670, y=600)
############################################
snort.mainloop()