import tkinter as tk
from tkinter import ttk, scrolledtext

snort=tk.Tk()
snort.title('ABOUT')
snort.geometry('775x200')
tc='''        SNORT-GUI is a Open Source Application developed by WhiteHatCyberus for intrusion 
        detection systems and cyber-forensic analysis.

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.15.1 GRE (Build 15125) 
   """"    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014-2019 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.10.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

'''

T=scrolledtext.ScrolledText(snort,width=95, height=10)
T.insert(tk.INSERT,tc)
T.configure(state="disabled")
T.pack(padx=10, pady=10)
snort.resizable(False, False)
snort.mainloop()
