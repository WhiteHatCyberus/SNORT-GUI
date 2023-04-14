import os
os.system('sudo apt install python3-tk -q=3')

import tkinter as tk
from tkinter import messagebox,scrolledtext

# the terms and conditions

import tkinter.simpledialog
i=0
while i!=1:
    # Prompt the user for their sudo password
    sudo_password = tkinter.simpledialog.askstring("Setting up", "\nCreate your SNORT administrator password: \n\n( Note: Once set, admin password cannot be changed and \npassword should be your Linux sudo password to download\npackages and perform administrator operations, incase if\nyou intend to change the password, reinstall the application.)\n", show='*')

    #error handling if window is closed unexpectedly.
    if(sudo_password is None):
                exit()
    elif sudo_password:
        
        os.system('mkdir .resources/temp >/dev/null 2>&1')
        os.system('cp -r .resources/alert . >/dev/null 2>&1')
        i=1

        # Write the password to a text file named "password.txt"
        with open(".resources/temp/admin.pass", "w") as f:
            f.write(sudo_password)

        tc='''
    You are using the SNORT GUI developed by White Hat Cyberus!
    Developed by 4 students from Rajagiri School of Engineering and 
    Technology . This is a Open Source Software, so feel free to 
    check out the code.
    
    Github: https://github.com/WhiteHatCyberus
    
    ⚠ Disclaimer:
    To be used for personal, educational and enterprise purposes. 

    What is SNORT?  
    SNORT is a Open Source Intrusion Detection System / Intrusion 
    Prevention System maintained by Cisco Talos. 

			T&C
		     ---------
		     
    1. Use this software at your own risk.
    2. The authors of this software are not responsible for any 
       damages caused by this software.
    3. This software is provided "as is" without warranty of any 
       kind, express or implied.
    4. By using this software, you agree to these terms and conditions.

    Note: This application will monitor your network in real time and 
    access your administrative directories. For proper functioning, 
    run the application in 'sudo' mode.
    
    ⚠ Manipulating this application for malicious purposes is not 
    entertained.

        '''
        ####################

        snort=tk.Tk()
        snort.geometry('600x420+1+1')
        snort.title('Terms and Conditions')

        ##############################################################################################3333
        #functions
        def agree():
            result=messagebox.askokcancel("Agreement Confirmation","By clicking 'OK', you agree with the t&c")
            if(result==True):
                snort.destroy()
                os.system("python3 .resources/resources.py")
                
        def disagree():
            result=messagebox.askyesno("Disagreement Confirmation","To ensure proper functioning of application, accept the t&c")
            if(result==False):
                snort.destroy()
        #############################################################################################
        #text
        T=scrolledtext.ScrolledText(snort,width=70, height=20)
        T.insert(tk.INSERT,tc)
        T.configure(state="disabled")
        T.pack(pady=20)
        
        #buttons
        agreebtn=tk.Button(snort, text="Agree", command=agree, cursor="hand2",bg="#000", relief="groove", fg="#fff",activebackground="grey72", activeforeground="#fff")
        disagreebtn=tk.Button(snort,text="Disagree", command=disagree, cursor="hand2",bg="#000", relief="groove", fg="#fff",activebackground="grey72", activeforeground="#fff")
        agreebtn.place(x=430,y=380)
        disagreebtn.place(x=500,y=380)
        snort.resizable(False,False)
        snort.mainloop()

    else:
        messagebox.showerror("Failure", "Password field cannot be empty")
