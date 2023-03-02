import tkinter as tk
from tkinter import messagebox
import subprocess

def check_reachability():
    target_ip = target_ip_entry.get()
    if target_ip == "":
        messagebox.showerror("Error", "Please enter a target IP.")
        return
    # Check if target IP is reachable
    response = subprocess.call(["ping", "-c", "1", "-W", "1", target_ip])
    if response == 0:
        attack_type = attack_var.get()
        messagebox.showinfo("Success", f"Selected {attack_type} attack on {target_ip}.")
    else:
        messagebox.showerror("Error", f"Target IP {target_ip} is not reachable.")

root = tk.Tk()
root.title("Attack Simulation")
root.geometry("400x250")
root.resizable(False, False)

# Attack Type Label
attack_label = tk.Label(root, text="Attack Type:")
attack_label.grid(row=0, column=0, padx=5, pady=5)

# Attack Type Menu
attack_var = tk.StringVar(value="Select an Attack Type")
attack_menu = tk.OptionMenu(root, attack_var, "Probe", "DoS", "U2R", "R2L")
attack_menu.grid(row=0, column=1, padx=5, pady=5)
attack_label.menu = attack_menu

# Target IP Label and Entry
tk.Label(root, text="Target IP:").grid(row=1, column=0, padx=5, pady=5)
target_ip_entry = tk.Entry(root)
target_ip_entry.grid(row=1, column=1, padx=5, pady=5)

# Check Button
check_button = tk.Button(root, text="Check Reachability", command=check_reachability)
check_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
