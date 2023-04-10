import os,subprocess
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

with open('.resources/temp/admin.pass', 'r') as file:
    sudo_passwd = file.read()
    
i=3
try:
    while i>0:
        sudo_password = tk.simpledialog.askstring("Password", "\nEnter your administrator password:\n", show='*')

        if sudo_password==sudo_passwd:
            i=0
            snort=tk.Tk()

            snort.geometry('1200x650+1+1')

            filename="/etc/snort/rules/Untitled.rules"
            
            command='sudo -S touch '+filename
            process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, preexec_fn=os.setsid)
            process.stdin.write(sudo_password.encode('utf-8') + b'\n')
            process.stdin.flush()
            mylabel4=Label()
            
            #Title of tkinter
            snort.title('SNORT Rule Generator')


            # Frames
            frame = Frame(snort,height = 50, width = 100,padx=10,pady=10)
            frame.pack(fill=X, expand=False)
            frame2 = Frame(snort,height = 50, width = 100,padx=10,bg='white')
            frame2.pack(fill=BOTH, expand=False)

            frame3 = Frame(snort,height = 50, width = 900,padx=10,pady=1)
            frame3.pack(fill=X, expand=False)

            frame5 = Frame(snort,height = 50, width = 900,padx=27,relief='ridge')
            frame5.pack(fill=X, expand=False)

            frame6 = Frame(snort,height = 50, width = 900,padx=27,relief='ridge')
            frame6.pack(fill=X, expand=False)

            frame7 = Frame(snort,height = 50, width = 900,padx=10,bg='white',relief='sunken',bd=2)
            frame7.pack(fill=X, expand=False)

            frame8 = Frame(snort,height = 50, width = 900,padx=10,relief='ridge')
            frame8.pack(fill=X, expand=False)

            frame4 = Frame(snort,height = 250, width = 900,bd=3,padx=10,relief='ridge',bg='#81DAF5')
            frame4.pack(fill=BOTH, expand=True)


            #Variables
            mystr=StringVar()
            mystr2=StringVar()
            messagex=StringVar()
            sidx=StringVar()

            ################################################################################3333

            #Functions

            def mNew():
                global filename 
                if filename=="/etc/snort/rules/Untitled.rules":
                    response=messagebox.askyesnocancel("Creating new workspace","Do you want to save the current workspace?")
                    if response is True:
                        mSaveas()
                        filename="/etc/snort/rules/Untitled.rules"
                    elif response is False:
                        if os.path.exists(filename):
                            command='sudo -S rm '+filename
                            process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, preexec_fn=os.setsid)
                            process.stdin.write(sudo_password.encode('utf-8') + b'\n')
                            process.stdin.flush()
                        else:
                            myopen=""
                            filename = myopen
                            mylabel4.config(text=filename)
                            mylabel4.pack()
                myopen=""
                filename = myopen
                mylabel4.config(text=filename)
                mylabel4.pack()
                filename="/etc/snort/rules/Untitled.rules"

            def mAbout():
                messagebox.showinfo(title='About',message='SNORT Rule Generator')
                return

            def mOpen():
                myopen=filedialog.askopenfilename(initialdir='/etc/snort/rules/', title='Select .rules')
                
                if myopen:
                    global filename
                    filename = myopen
                    mylabel4.config(text=filename)
                    mylabel4.pack()

            def mQuit():
                mexit=messagebox.askokcancel(title='Exit',message='Are you sure?')
                if mexit>0:
                    snort.destroy()
                    return
                
            def mSaveas():
                myopen = filedialog.asksaveasfilename(initialdir='/etc/snort/rules', defaultextension='.rules')
                if myopen:
                    global filename
                    command = 'sudo -S mv '+filename+' '+myopen
                    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, preexec_fn=os.setsid)
                    process.stdin.write(sudo_password.encode('utf-8') + b'\n')
                    process.stdin.flush()
                    filename = myopen
                    mylabel4.config(text=filename)
                    mylabel4.pack()

            ##########################################################################################	
            # Rule Header Area
            actions=Label(frame,text='Actions',fg='black',font=('Verdana', 8)).grid(row=1,column=0,sticky=W)
            protocol=Label(frame,text=' Protocol',fg='black',font=('Verdana', 8)).grid(row=1,column=1,sticky=W)
            snetwork=Label(frame,text=' Source Network',fg='black',font=('Verdana', 8)).grid(row=1,column=2,sticky=W)
            srcport=Label(frame,text=' Source Port',fg='black',font=('Verdana', 8)).grid(row=1,column=3,sticky=W)
            #ara=Label(frame,text='Direction',fg='black',font=('Verdana', 8)).grid(row=1,column=4,sticky=W)
            dnetwork=Label(frame,text=' Destination Network',fg='black',font=('Verdana', 8)).grid(row=1,column=5,sticky=W)
            dstport=Label(frame,text=' Destination Port',fg='black',font=('Verdana', 8)).grid(row=1,column=6,sticky=W)
            classtype=Label(frame,text=' Class Type',fg='black',font=('Verdana', 8)).grid(row=1,column=7,sticky=W)



            ###########################################################################################
            #Actions Options
            mylist=['ALERT','MAILALERT','DROP','REJECT','PASS','LOG']
            var=StringVar()
            var.set("Select")
            mymenu=OptionMenu(frame,var,*mylist)
            mymenu.grid(row=2,column=0)
            #mymenu.pack()
            mymenu.config(font=('calibri',(10)),bg='#54ECF7',width=9,cursor="hand2")
            mymenu['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")

            #Protocol Options
            mylist2=['TCP','UDP','IP','ICMP']
            var2=StringVar()
            var2.set("Select")
            mymenu2=OptionMenu(frame,var2,*mylist2)
            mymenu2.grid(row=2,column=1)
            #mymenu.pack()
            mymenu2.config(font=('calibri',(10)),bg='#54ECF7',width=6,cursor="hand2")
            mymenu2['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")

            # Source Networks Options
            mylist3=['$EXTERNAL_NET','$HOME_NET','$HTTP_SERVER','$DNS_SERVER','$MAIL_SERVER','any']
            var3=StringVar()
            var3.set("Select")
            mymenu3=OptionMenu(frame,var3,*mylist3)
            mymenu3.grid(row=2,column=2)
            #mymenu.pack()
            mymenu3.config(font=('calibri',(10)),bg='#54ECF7',width=11,cursor="hand2")
            mymenu3['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")

            # Source Port Options
            mylist4=['21','22','23','25','53','80','110','143','443','587','any']
            var4=StringVar()
            var4.set("Select")
            mymenu4=OptionMenu(frame,var4,*mylist4)
            mymenu4.grid(row=2,column=3)
            #mymenu.pack()
            mymenu4.config(font=('calibri',(10)),bg='#54ECF7',width=6,cursor="hand2")
            mymenu4['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")


            # Destination Network Options
            mylist5=['$EXTERNAL_NET','$HOME_NET','$HTTP_SERVER','$DNS_SERVER','$MAIL_SERVER','any']
            var5=StringVar()
            var5.set("Select")
            mymenu5=OptionMenu(frame,var5,*mylist5)
            mymenu5.grid(row=2,column=5)
            #mymenu.pack()
            mymenu5.config(font=('calibri',(10)),bg='#54ECF7',width=11,cursor="hand2")
            mymenu5['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")

            # Destination Port Options
            mylist6=['21','22','23','25','53','80','110','143','443','587','any']
            var6=StringVar()
            var6.set("Select")
            mymenu6=OptionMenu(frame,var6,*mylist6)
            mymenu6.grid(row=2,column=6)
            #mymenu.pack()
            mymenu6.config(font=('calibri',(10)),bg='#54ECF7',width=6,cursor="hand2")
            mymenu6['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")

            #ClassTypes
            mylist8=['attempted-admin','attempted-user','inappropriate-content','policy-violation','shellcode-detect','trojan-activity','web-application-attack','attempted-dos','attempted-recon','denial-of-service','misc-attack','web-application-activity','misc-activity','network-scan']
            var8=StringVar()
            var8.set("Select")
            mymenu8=OptionMenu(frame,var8,*mylist8)
            mymenu8.grid(row=2,column=7)
            #mymenu.pack()
            mymenu8.config(font=('calibri',(10)),bg='#54ECF7',width=17,cursor="hand2")
            mymenu8['menu'].config(font=('calibri',(10)),bg='#54ECF7',cursor="hand2")

            #Direction Options
            mylist7=['->','<>']
            var7=StringVar()
            var7.set("->")
            mymenu7=OptionMenu(frame,var7,*mylist7)
            mymenu7.grid(row=2,column=4)
            mymenu7.config(font=('calibri',(10)),bg='white',width=4,cursor="hand2")
            mymenu7['menu'].config(font=('calibri',(10)),bg='white',cursor="hand2")


            ####Message
            messagetext=Label(frame2,text='Message Text',fg='black',font=('Verdana', 8),bg='white').grid(row=0,column=0,sticky=W)
            message=Entry(frame2,textvariable=messagex,width = 111,bd=3,justify=LEFT,selectforeground='black').grid(row=1,column=0)

            sidx.set("1000000")
            sidtext=Label(frame2,text='Snort ID',fg='black',font=('Verdana', 8),bg='white').grid(row=0,column=2,sticky=W)
            eesid=Entry(frame2,textvariable=sidx,width = 18,bd=3,justify=LEFT,selectforeground='black').grid(row=1,column=2)


            priotext=Label(frame2,text='Priority',fg='black',font=('Verdana', 8),bg='white').grid(row=0,column=3,sticky=W)
            #Direction Options
            var9=StringVar()
            pri=Entry(frame2,textvariable=var9,width = 12,bd=3,justify=RIGHT,selectforeground='black').grid(row=1,column=3,sticky=W)

            ######Content
            CheckVar1 = IntVar()
            CheckVar2 = IntVar()
            CheckVar = IntVar()
            Payloadd = IntVar()
            Payloadd=0
            def runSelectedItems():
                global Payloadd
                Payloadd=1
                if CheckVar2.get() == 1:
                    CheckVar2.set(0)
                if CheckVar.get() == 1:
                    CheckVar.set(0)
                    
            def runSelectedItems2():
                global Payloadd
                Payloadd=2
                if CheckVar1.get() == 1:
                    CheckVar1.set(0)
                if CheckVar.get() == 1:
                    CheckVar.set(0)
                    
            def runSelectedItems3():
                global Payloadd
                Payloadd=3
                if CheckVar1.get() == 1:
                    CheckVar1.set(0)
                if CheckVar2.get() == 1:
                    CheckVar2.set(0) 

            content=Label(frame3,text='Payload:',fg='black',font=('Verdana', 8, 'bold')).grid(row=0,column=0,sticky=W)
            C1 = Checkbutton(frame3, text = "Content", variable = CheckVar1, \
                            onvalue = 1, offvalue = 0, height=2, \
                            width = 10, command=runSelectedItems,cursor="hand2")
            C2 = Checkbutton(frame3, text = "PCRE", variable = CheckVar2, \
                            onvalue = 1, offvalue = 0, height=2, \
                            width = 10,command=runSelectedItems2,cursor="hand2")

            C3 = Checkbutton(frame3, text = "Uricontent", variable = CheckVar, \
                            onvalue = 1, offvalue = 0, height=2, \
                            width = 10,command=runSelectedItems3,cursor="hand2")
                            
            C1.grid(row=1,column=0,sticky=W)
            C2.grid(row=1,column=1,sticky=W)
            C3.grid(row=1,column=2,sticky=W)


            ######Payload Entry
            textpoyload1=StringVar()
            textpoyload2=StringVar()
            poyload1=Entry(frame5,textvariable=textpoyload1,width = 108,bd=2,justify=LEFT,selectforeground='black').grid(row=0,column=0,sticky=W)
            def over(event):
                event.widget.config(bg='gray')
                return
                
            def leave(event):
                event.widget.config(bg='#54ECF7')
                return
                
            def myLinks():
                textpoyload1.set("")
                
            clearbutton=Button(frame5,text='Clear',fg='black',bg='#54ECF7',borderwidth=1,pady=1,width = 6,cursor="hand2",command=myLinks,relief=GROOVE,activebackground='#54ECF7',justify=LEFT)
            clearbutton.bind("<Enter>",over)
            clearbutton.bind("<Leave>",leave)
            clearbutton.grid(row=0,column=1)


            ##Poyload Options

            Ext1 = IntVar()
            Ext2 = IntVar()

            CE1 = Checkbutton(frame6, text = "Case Sensitive", variable = Ext1, \
                            onvalue = 1, offvalue = 0, height=2, \
                            width = 10,cursor="hand2")
            CE2 = Checkbutton(frame6, text = "Raw Bytes", variable = Ext2, \
                            onvalue = 1, offvalue = 0, height=2, \
                            width = 10,cursor="hand2")
                            
            CE1.grid(row=0,column=0,sticky=W)
            CE2.grid(row=0,column=1,sticky=W)

            offsett=StringVar()
            depthh=StringVar()
            distancee=StringVar()



            poffset=Label(frame6,text='Offset(in byte)',fg='black',font=('Verdana', 8)).grid(row=1,column=0,sticky=W)
            payoffset=Entry(frame6,textvariable=offsett,width = 10,bd=2,justify=LEFT,selectforeground='black').grid(row=2,column=0,sticky=W)

            pdepth=Label(frame6,text='Depth(in byte)',fg='black',font=('Verdana', 8)).grid(row=1,column=1,sticky=W)
            paydepth=Entry(frame6,textvariable=depthh,width = 10,bd=2,justify=LEFT,selectforeground='black').grid(row=2,column=1,sticky=W)

            pdistance=Label(frame6,text='Distance',fg='black',font=('Verdana', 8)).grid(row=1,column=2,sticky=W)
            paydistance=Entry(frame6,textvariable=distancee,width = 10,bd=2,justify=LEFT,selectforeground='black').grid(row=2,column=2,sticky=W)

            bos=Label(frame6,text='  ',fg='black',font=('Verdana', 8),pady=10).grid(row=3,column=0,sticky=W)
            ####Extra Options

            bos=Label(frame6,text='        ',fg='black',font=('Verdana', 8),pady=10).grid(row=1,column=3,sticky=W)

            threslabel=Label(frame6,text='Thresholds ->',fg='black',font=('Verdana', 8)).grid(row=1,column=4,sticky=E)
            threslabel2=Label(frame6,text='Type:',fg='black',font=('Verdana', 8)).grid(row=2,column=4,sticky=W)

            mylist12=['limit','threshold','both']
            var12=StringVar()
            var12.set("Select")
            mymenu12=OptionMenu(frame6,var12,*mylist12)
            mymenu12.grid(row=2,column=5)
            mymenu12.config(font=('calibri',(10)),bg='white',width=6,cursor="hand2")
            mymenu12['menu'].config(font=('calibri',(10)),bg='white',cursor="hand2")

            trackk=StringVar()
            countt=IntVar()
            secondss=IntVar()

            tracklabel=Label(frame6,text='Track',fg='black',font=('Verdana', 8)).grid(row=2,column=6,sticky=E)

            mylist13=['by_src','by_dst']
            var13=StringVar()
            var13.set("Select")
            mymenu13=OptionMenu(frame6,var13,*mylist13)
            mymenu13.grid(row=2,column=7)
            mymenu13.config(font=('calibri',(10)),bg='white',width=4,cursor="hand2")
            mymenu13['menu'].config(font=('calibri',(10)),bg='white',cursor="hand2")

            cont=StringVar()
            cont.set("0")
            sec=StringVar()
            sec.set("0")

            countlabel=Label(frame6,text='Count',fg='black',font=('Verdana', 8)).grid(row=2,column=8,sticky=E)
            countt=Entry(frame6,textvariable=cont,width = 8,bd=2,justify=LEFT,selectforeground='black').grid(row=2,column=9,sticky=W)

            secondslabel=Label(frame6,text='Second(s)',fg='black',font=('Verdana', 8)).grid(row=2,column=10,sticky=E)
            secondss=Entry(frame6,textvariable=sec,width = 8,bd=2,justify=LEFT,selectforeground='black').grid(row=2,column=11,sticky=W)


            ##Flow Options
            flowxxx=Label(frame7,text='Session Options:',fg='black',font=('Verdana', 8, 'bold'),pady=10,bg='white').grid(row=0,column=0,sticky=W)
            flow=StringVar()
            flow="flow:"

            flow1 = IntVar()
            flow2 = IntVar()
            flow3 = IntVar()
            flow4 = IntVar()
            flow5 = IntVar()
            flow6 = IntVar()
            flow7 = IntVar()
            flow8 = IntVar()


            FL1 = Checkbutton(frame7, text = "Established", variable = flow1,onvalue = 1, offvalue = 0, height=1, cursor="hand2",bg='white')
            FL2 = Checkbutton(frame7, text = "To Client", variable = flow2,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')
            FL3 = Checkbutton(frame7, text = "From Client", variable = flow3,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')
            FL4 = Checkbutton(frame7, text = "No Stream", variable = flow4,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')
            FL5 = Checkbutton(frame7, text = "Stateless", variable = flow5,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')
            FL6 = Checkbutton(frame7, text = "To Server", variable = flow6,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')
            FL7 = Checkbutton(frame7, text = "From Server", variable = flow7,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')
            FL8 = Checkbutton(frame7, text = "Only Stream", variable = flow8,onvalue = 1, offvalue = 0, height=1,cursor="hand2",bg='white')				 

            FL1.grid(row=1,column=0)
            FL2.grid(row=1,column=1)
            FL3.grid(row=1,column=2)
            FL4.grid(row=1,column=3)
            FL5.grid(row=1,column=4)
            FL6.grid(row=1,column=5)
            FL7.grid(row=1,column=6)
            FL8.grid(row=1,column=7)
            bos=Label(frame7,text='  ',fg='black',font=('Verdana', 8),pady=2,bg='white').grid(row=2,column=0,sticky=W)

            ###References
            ref11=StringVar()
            ref22=StringVar()

            ref1lab=Label(frame8,text='Reference',fg='black',font=('Verdana', 8)).grid(row=0,column=0,sticky=W)
            reftype1=Label(frame8,text='Type',fg='black',font=('Verdana', 8)).grid(row=0,column=1,sticky=W)
            ref1=Entry(frame8,textvariable=ref11,width = 50,bd=2,justify=LEFT,selectforeground='black').grid(row=1,column=0,sticky=W)

            #Type1
            mylist10=['bugtraq','cve','nessus','arachnids','mcafee','url']
            var10=StringVar()
            var10.set("Select")
            mymenu10=OptionMenu(frame8,var10,*mylist10)
            mymenu10.grid(row=1,column=1)
            mymenu10.config(font=('calibri',(10)),bg='white',width=6,cursor="hand2")
            mymenu10['menu'].config(font=('calibri',(10)),bg='white',cursor="hand2")

            ref1lab2=Label(frame8,text='Reference',fg='black',font=('Verdana', 8)).grid(row=2,column=0,sticky=W)
            reftype2=Label(frame8,text='Type',fg='black',font=('Verdana', 8)).grid(row=2,column=1,sticky=W)
            ref2=Entry(frame8,textvariable=ref22,width = 50,bd=2,justify=LEFT,selectforeground='black').grid(row=3,column=0,sticky=W)

            #Type2
            mylist11=['bugtraq','cve','nessus','arachnids','mcafee','url']
            var11=StringVar()
            var11.set("Select")
            mymenu11=OptionMenu(frame8,var11,*mylist11)
            mymenu11.grid(row=3,column=1)
            mymenu11.config(font=('calibri',(10)),bg='white',width=6,cursor="hand2")
            mymenu11['menu'].config(font=('calibri',(10)),bg='white',cursor="hand2")

            ####Buttons
            def over(event):
                event.widget.config(bg='gray')
                return
                
            def leave(event):
                event.widget.config(bg='#F7BE81')
                return
            def Copyrule():
                snort.clipboard_clear()
                snort.clipboard_append(myrule)
            def Resetall():
                snort.destroy()
            Ruleheader=StringVar()
            Rulebody=StringVar()
            Rulebody="bos"
            Ruleend=StringVar()
            Rulelimit=StringVar()
            Reference1=StringVar()
            Reference2=StringVar()
            def Rulecreate():
                #Header of the rule
                if var.get() == "Select" or var2.get() == "Select" or var3.get() == "Select" or var4.get() == "Select" or var5.get() == "Select" or var6.get() == "Select":
                    messagebox.showwarning("Error","Header Rule Missed")
                else:
                    global Ruleheader
                    global Rulebody
                    global Ruleend
                    #clearbuttonx['state'] = 'enabled'
                    clearbuttonx.configure(state=NORMAL)
                    clearbuttony.configure(state=NORMAL)
                    Ruleheader= var.get().lower()+" "+var2.get().lower()+" "+var3.get()+" "+var4.get()+" "+var7.get()+" "+var5.get()+" "+var6.get()+" "+"( "
                    ##Message
                    if(messagex.get()): 
                        Ruleheader+="msg:"+'"'+messagex.get()+'"'+"; "
                    ##Sid and Prioty
                    ##Classtype
                    if(sidx.get()):
                        Ruleend="sid:"+sidx.get()+"; "    
                    if(var8.get() != "Select"):
                        Ruleend+="classtype:"+var8.get()+"; "
                    if(var9.get() != ""):
                        Ruleend+="priority:"+var9.get()+"; "    
                    ##Content(Payload)
                    global Payloadd
                    global flow
                    global myrule
                    if (Payloadd != 0):
                        if(Payloadd == 1):
                            Rulebody="content:"+'"'+textpoyload1.get()+'"'+"; "
                        if(Payloadd == 2):
                            Rulebody="pcre:"+'"'+textpoyload1.get()+'"'+"; "
                        if(Payloadd == 3):
                            Rulebody="uricontent:"+'"'+textpoyload1.get()+'"'+"; "
                        if(Ext1.get()):
                            Rulebody+="nocase; "
                        if(Ext2.get()):
                            Rulebody+="rawbytes; "
                        if(offsett.get()):
                            Rulebody+="offset:"+offsett.get()+"; "
                        if(depthh.get()):
                            Rulebody+="depth:"+depthh.get()+"; "
                        if(distancee.get()):
                            Rulebody+="distance:"+distancee.get()+"; "
                    ##Threshold
                    if(var12.get != "Select" and var13.get() != "Select"):
                        Ruleend+="threshold:type "+var12.get()+", track "+var13.get()+", count "+cont.get()+", seconds "+sec.get()+"; "
                    ##References
                    if(var10.get != "Select" or var11.get() != "Select"):
                        if(ref22.get()):
                            Ruleend+="reference:"+var11.get()+","+ref22.get()+"; "
                        if(ref11.get()):
                            Ruleend+="reference:"+var10.get()+","+ref11.get()+"; "
                    if (flow1.get() == 1) or (flow2.get() == 1) or (flow3.get() == 1) or (flow4.get() == 1) or (flow5.get() == 1) or (flow6.get() == 1) or (flow7.get() == 1) or (flow8.get() == 1):
                        if(flow1.get() == 1):
                            flow+="established,"
                        if(flow2.get() == 1):
                            flow+="to_client,"
                        if(flow3.get() == 1):
                            flow+="from_client,"
                        if(flow4.get() == 1):
                            flow+="no_stream,"
                        if(flow5.get() == 1):
                            flow+="stateless,"
                        if(flow6.get() == 1):
                            flow+="to_server,"
                        if(flow7.get() == 1):
                            flow+="from_server,"
                        if(flow8.get() == 1):
                            flow+="only_stream,"
                        flow+=";"
                        flow=flow.replace(",;", "; ")
                        Ruleheader+=flow
                        flow="flow:"
                    if(Rulebody != "bos"):
                        myrule=Ruleheader+Rulebody+Ruleend+")"
                        
                        rules=Label(frame4,text=myrule,font=('Verdana', 8),bg='#81DAF5',padx=5,wraplength=900)
                        rules.grid(row=1,column=0,sticky=W)
                        Rulebody="bos"
                    else:
                        myrule=Ruleheader+Ruleend+")"
                        rules=Label(frame4,text=myrule,font=('Verdana', 8),bg='#81DAF5',padx=5,wraplength=900)
                        rules.grid(row=1,column=0,sticky=W)


                    if filename:
                        with open(filename, 'a') as file:
                            # write the string to the file
                            file.write(myrule + '\n')



                            
                    

            bos=Label(frame8,text='                ',fg='black',font=('Verdana', 8),pady=2).grid(row=2,column=2,sticky=W)
                
            clearbutton=Button(frame8,text='Generate Rule',fg='black',bg='#F7BE81',borderwidth=1,padx=15,width = 15,cursor="hand2",command=Rulecreate,relief=GROOVE,activebackground='#54ECF7',justify=LEFT)
            clearbutton.bind("<Enter>",over)
            clearbutton.bind("<Leave>",leave)
            clearbutton.grid(row=2,column=3)

            clearbuttonx=Button(frame8,text='Close',fg='black',bg='#F7BE81',borderwidth=1,padx=15,width = 10,cursor="hand2",command=Resetall,relief=GROOVE,activebackground='#54ECF7',justify=LEFT,state=DISABLED)
            clearbuttonx.bind("<Enter>",over)
            clearbuttonx.bind("<Leave>",leave)
            clearbuttonx.grid(row=2,column=5)

            clearbuttony=Button(frame8,text='Copy',fg='black',bg='#F7BE81',borderwidth=1,padx=15,width = 10,cursor="hand2",command=Copyrule,relief=GROOVE,activebackground='#54ECF7',justify=LEFT,state=DISABLED)
            clearbuttony.bind("<Enter>",over)
            clearbuttony.bind("<Leave>",leave)
            clearbuttony.grid(row=2,column=4)
            ###Output
            myrule=StringVar()
            myrule=""
            rule=Label(frame4,text='Snort Rule:',fg='black',font=('Verdana', 8, 'bold'),bg='#81DAF5').grid(row=0,column=0,sticky=W)

            ########################################################################################
            #Menus
            menubar=Menu(frame)

            #File
            filemenu=Menu(menubar,tearoff=0)
            filemenu.add_command(label="New Workspace", command=mNew)
            filemenu.add_command(label="Open Workspace",command=mOpen)
            filemenu.add_command(label="Save as", command=mSaveas)
            filemenu.add_command(label="Exit", command=mQuit)
            menubar.add_cascade(label="Options",menu=filemenu)

            snort.config(menu=menubar)

            snort.resizable(False,False)

            snort.mainloop()

        elif(sudo_password is None):
            exit()
        elif(sudo_password==""):
            messagebox.showerror("Error","Enter password")
        else:
            i=i-1
            messagebox.showerror("Error", "ⓘ Incorrect password, try again. (Attempts Left:"+str(i)+")")
            
except tk.TclError:
    exit()