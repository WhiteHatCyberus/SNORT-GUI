import os
import threading
import tkinter as tk
import subprocess
import datetime
import getpass #gets sudo password
import keyring #stores sudo password
import tkinter.messagebox as messagebox

if not os.path.exists('/etc/snort/ids.conf'):
    os.system('sudo cp ~/Desktop/SNORT-GUI/snort/ids.conf /etc/snort/')

if not os.path.exists('/etc/snort/rules/ids.rules'):
    os.system('sudo cp ~/Desktop/SNORT-GUI/snort/rules/ids.rules /etc/snort/rules/')


foldername='/etc/snort/logs'

def run_snort(duration_secs, process_lock):
    with process_lock:
        datetime_string = datetime.datetime.now().strftime("%d-%m-%y@%H.%M.%S")
        new_folderpath = '/etc/snort/logs/' + datetime_string
        os.system('sudo mkdir '+new_folderpath)
        command = f"sudo -S timeout {duration_secs} snort -A console -A fast -q -c /etc/snort/ids.conf -i wlo1 -l {new_folderpath}"
        snort_process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, preexec_fn=os.setsid)
        password = getpass.getpass(stream=None)
        password = password.encode('utf-8')
        snort_process.stdin.write(password)
        snort_process.stdin.write(b"\n")
        snort_process.stdin.flush()

def stop_snort(window):
    sudo_password = keyring.get_password("snort", "sudo_password")
    if sudo_password is None:
        sudo_password = getpass.getpass()
        keyring.set_password("snort", "sudo_password", sudo_password)
    p = subprocess.run(['sudo', '-S', 'pkill', 'snort'], input=f"{sudo_password}\n".encode().decode(), capture_output=True, text=True)
    messagebox.showinfo("Snort stopped", "Snort stopped successfully.")
    window.destroy()

def show_snort_window():
    # Create tkinter window for input
    input_window = tk.Tk()
    input_window.title("Enter Snort Duration")
    input_window.geometry('350x100')
    # Create label and entry widgets
    label = tk.Label(input_window, text="Enter the number of hours to run Snort:")
    label.place(x=10,y=15)

    entry = tk.Entry(input_window,width=5)
    entry.place(x=275,y=15)

    # Define function to start Snort process
    def start_snort():
        duration_hours = float(entry.get())
        duration_secs = int(duration_hours * 60 * 60)

        # Destroy the input window
        input_window.destroy()

        # Create thread lock and start Snort process in a separate thread
        process_lock = threading.Lock()
        snort_thread = threading.Thread(target=run_snort, args=(duration_secs, process_lock))
        snort_thread.start()
        
        # Create new window to display Snort status
        status_window = tk.Tk()
        status_window.title("Snort is Running")

        # Create label and button widgets in status window
        status_label = tk.Label(status_window, text="Snort is currently running.")
        status_label.pack(padx=20, pady=20)

        status_button = tk.Button(status_window, text="Stop Snort", command=lambda: stop_snort(status_window))
        status_button.pack(padx=20, pady=10)

    # Create button to start Snort process
    start_button = tk.Button(input_window, text="Start Snort", command=start_snort)
    start_button.place(x=120, y=50)
    input_window.resizable(False,False)
    input_window.mainloop()

if not os.path.exists(foldername):
    os.system('sudo mkdir '+foldername)
    show_snort_window()
else:
    show_snort_window()
