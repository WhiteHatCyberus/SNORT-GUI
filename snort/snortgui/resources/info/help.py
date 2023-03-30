import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from PIL import ImageTk, Image
import webbrowser


snort = tk.Tk()
snort.title('Help')
snort.geometry("950x700")


# setting up canvas for bg image
canvas = tk.Canvas(snort, width=900, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

# display bg image
img = Image.open("images/snort1.png")
img = img.resize((950, 700), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

img1 = Image.open("images/snort2.png")
img1 = img1.resize((300, 200), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
def callback(url):
   webbrowser.open_new_tab(url)

def getting_started():
    HELP1 = '''                         Getting Started with Snort

 Snort is the foremost Open Source Intrusion Prevention System (IPS)
 in the world. Snort IPS uses a series of rules that help define malicious
 network activity and usesthose rules to find packets that match against 
 them and generates alerts for users.Snort can be deployed inline to stop 
 these packets, as well.

 Snort has three primary uses: As a packet sniffer like tcpdump, as a 
 packet logger — which is useful for network traffic debugging, or it can
 be used as a full-blown network intrusion prevention system. Snort can be
 downloaded and configured for personal and business use alike.

 Snort GUI is an application interface developed for everyone who has just
 started using snort. Snort GUI simplifies the writing of rules for the IDS
 through an API and able to run on both windows and linux. Snort GUI 
 For more information, the Snort Community website:

                  ''' 
    st = ScrolledText(snort, width=75, height=30)
    st.place(x=300, y=100)
    link="CLICK HERE TO VISIT COMMUNITY WEBSITE"
    text_with_link = f"{HELP1}{link}"
    st.insert(tk.INSERT, text_with_link)
    st.image_create(tk.INSERT, image=img1, padx=180, pady=20)
    st.tag_add("hyperlink", "end-{}c".format(len(link)+2),"19.55")
    st.tag_config("hyperlink", foreground="blue")
    st.tag_bind("hyperlink", "<Enter>", lambda event: st.tag_config("hyperlink", foreground="red"))
    st.tag_bind("hyperlink", "<Leave>", lambda event: st.tag_config("hyperlink", foreground="blue"))
    st.tag_bind("hyperlink", "<Button-1>", lambda event: webbrowser.open("https://www.snort.org/#documents"))
    st.configure(state='disabled')

def doc():
    HELP2 = '''                 Snort Documentation

1. Snort User Manual - Comprehensive guide to Snort usage and configuration.
2. Snort Rule Writing - Guide to creating custom Snort rules.
3. Snort FAQs - Frequently asked questions about Snort.

For more information, refer to the Snort website.

'''

    st = ScrolledText(snort, width=75, height=30)
    st.place(x=300, y=100)
    link1="CLICK HERE TO VISIT DOCUMENTATION"
    text_with_link1 = f"{HELP2}{link1}"
    st.insert(tk.END, text_with_link1)
    st.image_create(tk.END, image=img1,padx=100,pady=20)
   
    st.tag_add("hyperlink", "end-{}c".format(len(link1)+2), "end")
    st.tag_config("hyperlink", foreground="blue", underline=True)
    def on_enter(event):
        st.tag_config("hyperlink", foreground="red", underline=True)

    def on_leave(event):
        st.tag_config("hyperlink", foreground="blue", underline=True)
    def open_link(event):
     webbrowser.open("http://books.gigatux.nl/mirror/snortids/0596006616/snortids-CHP-5.html")
    st.tag_bind("hyperlink", "<Enter>", on_enter)
    st.tag_bind("hyperlink", "<Leave>", on_leave)
    st.tag_bind("hyperlink", "<Button-1>", open_link)
    st.configure(state='disabled')
def use():
    HELP3 = '''Using Snort GUI

1. Launch the Snort GUI application.
2. Configure Snort settings and rules.
3. Start Snort monitoring.
4. View Snort alerts and logs.
5. Troubleshoot common issues.

For more information, refer to the Snort User Manual or the Snort Community website.
fknkkok gkjn
l;smlmmlfm;f
fsnlnkngkjn
jsbfbkfb    kg
gknkngnlkk
fmGRNNNNRGNENN'''

    st = ScrolledText(snort, width=75, height=30)
    st.place(x=300, y=100)
    st.insert(tk.INSERT, HELP3)
    st.image_create(tk.END, image=img1,padx=100,pady=20)
    st.configure(state='disabled')
  
   


# add widgets here
b1 = tk.Button(text='Getting started with snort', command=getting_started)
b1.place(x=70, y=150)
b2 = tk.Button(text='Important Documentation', command=doc)
b2.place(x=70, y=200)
b3 = tk.Button(text='Snort GUI(How to use)', command=use)
b3.place(x=70, y=250)

snort.resizable(False, False)
snort.mainloop()
