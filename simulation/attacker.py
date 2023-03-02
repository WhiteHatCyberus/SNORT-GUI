import tkinter as tk
import subprocess
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Attack Simulation")
root.resizable(False, False)

# Create the label for the attack type
attack_label = tk.Label(root, text="Select Attack Type:")
attack_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Create the menu bar for the attack type options
menu_bar = tk.Menu(root)
attack_menu = tk.Menu(menu_bar, tearoff=0)
attack_menu.add_command(label="Probe")
attack_menu.add_command(label="DoS")
attack_menu.add_command(label="U2R")
attack_menu.add_command(label="R2L")
menu_bar.add_cascade(label="Select Attack Type", menu=attack_menu)
root.config(menu=menu_bar)

# Create the label for the target IP
ip_label = tk.Label(root, text="Enter Target IP:")
ip_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Create the text field for the target IP
ip_entry = tk.Entry(root)
ip_entry.grid(row=1, column=1, padx=5, pady=5)

# Define the function to run the ping command
def run_ping():
    target_ip = ip_entry.get()
    ping_process = subprocess.Popen(['ping', '-c', '4', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ping_output, ping_error = ping_process.communicate()
    ping_output_str = ping_output.decode('utf-8')
    if "0% packet loss" in ping_output_str:
        messagebox.showinfo("Success", "Ping to " + target_ip + " was successful!")
    else:
        messagebox.showerror("Failure", "Ping to " + target_ip + " failed.")

# Create the button to run the ping command
ping_button = tk.Button(root, text="Ping", command=run_ping)
ping_button.grid(row=2, column=0, padx=5, pady=5)

# Run the main loop
root.mainloop()
