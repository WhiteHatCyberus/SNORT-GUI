import tkinter as tk
import os
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Attack Simulation")
root.resizable(False, False)

# Create the menu bar
menu_bar = tk.Menu(root)
attack_menu = tk.Menu(menu_bar, tearoff=0)
attack_menu.add_command(label="Probe")
attack_menu.add_command(label="DoS")
attack_menu.add_command(label="U2R")
attack_menu.add_command(label="R2L")
menu_bar.add_cascade(label="Select Attack Type", menu=attack_menu)
root.config(menu=menu_bar)

# Create the text field
ip_label = tk.Label(root, text="Enter Target IP:")
ip_label.pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

# Define the function to run the ping command
def run_ping():
    target_ip = ip_entry.get()
    response = os.system("ping -c 4 " + target_ip + " | grep '0% packet loss'")
    if response == 0:
        messagebox.showinfo("Success", "Ping to " + target_ip + " was successful!")
    else:
        messagebox.showerror("Failure", "Ping to " + target_ip + " failed.")

# Create the button to run the ping command
ping_button = tk.Button(root, text="Ping", command=run_ping)
ping_button.pack()

# Run the main loop
root.mainloop()
