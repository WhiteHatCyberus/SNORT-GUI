import datetime
import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import psutil
filename=""

with open('.resources/temp/admin.pass', 'r') as file:
    sudo_passwd = file.read()
'''
if not os.path.exists('/etc/snort/ids.conf'):
    os.system('sudo cp ~/Desktop/SNORT-GUI/snort/ids.conf /etc/snort/')

if not os.path.exists('/etc/snort/rules/ids.rules'):
    os.system('sudo cp ~/Desktop/SNORT-GUI/snort/rules/ids.rules /etc/snort/rules/')
'''

foldername = '/etc/snort/logs'


def run_snort(duration_secs, process_lock, sudo_passwd, filename, interface_var):
    if duration_secs>0:
        if filename.endswith('.conf'):
            if interface_var.get():
                with process_lock:
                    datetime_string = datetime.datetime.now().strftime("%d-%m-%y@%H.%M.%S")
                    new_folderpath = f'{foldername}/{datetime_string}'
                    os.system(f'sudo mkdir {new_folderpath}')
                    command = f'sudo -S timeout {duration_secs} snort -A console -A fast -q -c {filename} -i {interface_var.get()} -l {new_folderpath}'
                    snort_process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, preexec_fn=os.setsid)
                    snort_process.stdin.write(sudo_passwd.encode('utf-8') + b'\n')
                    snort_process.stdin.flush()
                    

def stop_snort(window, sudo_password):
    password_window = tk.Tk()
    password_window.title("Password:")

    password_label = tk.Label(password_window, text="Enter the OTP to stop SNORT manually:")
    password_label.pack(padx=20, pady=20)

    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack(padx=20, pady=10)

    def verify_password():
        entered_password = password_entry.get()

        # Run the pkill command only if the entered password is correct
        if entered_password == sudo_password:
            p = subprocess.run(['sudo', '-S', 'pkill', 'snort'])
            password_window.destroy()
            window.destroy()
            messagebox.showinfo('Snort stopped', 'Snort stopped successfully.')
            

        else:
            messagebox.showerror('Incorrect Password', 'Incorrect password entered. Please try again.')
            password_entry.delete(0, tk.END)

    password_button = tk.Button(password_window, text="Stop Snort", command=verify_password)
    password_button.pack(padx=20, pady=10)
    password_window.resizable(False,False)
    password_window.mainloop()


def show_snort_window():
    input_window = tk.Tk()
    input_window.title('Run SNORT')
    input_window.geometry('495x300')

    label = tk.Label(input_window, text='Enter the number of hours to run Snort:')
    label.grid(row=0, column=0, padx=10, pady=15)

    entry = tk.Entry(input_window, width=5)
    entry.grid(row=0, column=1, padx=5, pady=10)

    interface_frame = tk.Frame(input_window)
    interface_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    # Label for network interface dropdown menu
    interface_label = tk.Label(interface_frame, text='Select network interface to listen on:')
    interface_label.grid(row=0, column=0, padx=5, pady=10)

    # Dropdown menu for network interfaces
    global interface_var
    interface_var = tk.StringVar()
    interface_menu = tk.OptionMenu(interface_frame, interface_var, *psutil.net_if_addrs().keys())
    interface_menu.grid(row=0, column=1, padx=5, pady=10)

    # File selection button and label
    file_frame = tk.Frame(input_window)
    file_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    file_label = tk.Label(file_frame, text='')
    file_label.grid(row=2, column=1, padx=5, pady=10)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir='/etc/snort', title='Select File',
                                          filetypes=(('Configuration Files', '*.conf'),))
        if filename:
            file_name = filename.split('/')[-1]  
            file_label.config(text=file_name)
        else:
            messagebox.showerror("Error", "No file selected!")
    file_button = tk.Button(file_frame, text='Select Configuration File', command=select_file)
    file_button.grid(row=2, column=0, padx=10, pady=10)



    def start_snort():
        
        time=entry.get()    #time entered
        try:
        # check if any variable is missing
            if time and interface_var and filename !="":
                try:
                    time = float(time)
                    if time >= 0 and (time.is_integer() or time != int(time)):
                        duration_secs = int(time * 60 * 60)
                        input_window.destroy()
                        # Prompt user for sudo password
                        sudo_password = tk.simpledialog.askstring("Password Initialisation", "Enter your One Time Password:\n(⚠️ Disclaimer: Remember this password\n to stop snort manually)\n", show='*')

                        # Check if password is correct
                        p = subprocess.run(['sudo', '-S', 'true'], input=bytes(sudo_password + '\n', 'utf-8'), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        if p.returncode != 0:
                            messagebox.showerror("Incorrect Password", "The password you entered is incorrect. Please try again.")
                            return

                        # Start snort
                        process_lock = threading.Lock()
                        snort_thread = threading.Thread(target=run_snort, args=(duration_secs, process_lock, sudo_passwd,filename,interface_var))
                        snort_thread.start()

                        status_window = tk.Tk()
                        status_window.title("Snort is Running")

                        status_label = tk.Label(status_window, text="Snort is currently running.")
                        status_label.pack(padx=20, pady=20)

                        status_button = tk.Button(status_window, text="Stop Snort", command=lambda: stop_snort(status_window, sudo_password))
                        status_button.pack(padx=20, pady=10)


                    else:
                        messagebox.showerror("Error", "Enter a valid time")
                except ValueError:
                    messagebox.showerror("Error", "Enter a valid time")
            else:
                messagebox.showerror("Error", "Enter Values") 
        except ValueError:
            messagebox.showerror("Error", "Enter Values")        

    button_active_bg, button_active_fg = '#f00', '#fff'
    start_button = tk.Button(input_window, text="Start Snort",relief='groove', cursor='hand2', activebackground=button_active_bg,
                             activeforeground=button_active_fg,command=start_snort,width=58,height=5)
    start_button.place(x=3,y=200)
    input_window.resizable(False,False)
    input_window.mainloop()

if not os.path.exists(foldername):
    os.system(f'sudo mkdir {foldername}')

i=3
try:
    while i>0:
        sudo_password = tk.simpledialog.askstring("Password", "\nEnter your administrator password:\n", show='*')

        if sudo_password==sudo_passwd:
            i=0
            show_snort_window()
        elif(sudo_password is None):
            exit()
        elif(sudo_password==""):
            messagebox.showerror("Error","Enter password")
        else:
            messagebox.showerror("Error", "ⓘ Incorrect password, try again. (Attempt:"+str(i)+")")
            i=i-1
except tk.TclError:
    exit()
