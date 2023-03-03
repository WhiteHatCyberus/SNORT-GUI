import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def check_reachability():
    target_ip = target_ip_entry.get()
    if target_ip == "":
        messagebox.showerror("Error", "Enter a target IP.")
        return
    # Check if target IP is reachable
    response = subprocess.call(["ping", "-c", "1", "-W", "1", target_ip])
    if response == 0:
        attack_type = attack_var.get()
        messagebox.showinfo("Success", f"Successfully connected to target {target_ip}.")
    else:
        messagebox.showerror("Error", f"Target IP {target_ip} is not reachable. Check your netork connection.")

root = tk.Tk()
root.title("Attack Simulation")
root.geometry("650x200")
root.resizable(False, False)

l1=tk.Label(root)
l1.grid(row=0, column=1)
l2=tk.Label(root)
l2.grid(row=1, column=1)

bg_image = Image.open("kali.jpg")

bg_image= bg_image.resize((650, 200), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Attack Type Label
attack_label = tk.Label(root, text="Attack Type:")
attack_label.grid(row=2, column=0, padx=15, pady=5)

# Attack Type Menu
attack_var = tk.StringVar(value="Select an Attack Type")
attack_menu = tk.OptionMenu(root, attack_var, "Probe", "DoS", "U2R", "R2L")
attack_menu.grid(row=2, column=1, padx=5, pady=5)
attack_label.menu = attack_menu

# Target IP Label and Entry
tk.Label(root, text="Target IP:").place(x=350, y=53)
target_ip_entry = tk.Entry(root)
target_ip_entry.place(x=435, y=53)

# Check Button
check_button = tk.Button(root, text="Check Connection", command=check_reachability)
check_button.place(x=455,y=90)

button_active_bg, button_active_fg = '#f00', '#fff'

print_b = tk.Button(root, text="Exploit",  relief='groove', cursor='hand2', activebackground=button_active_bg, activeforeground=button_active_fg)
print_b.place(x=235, y=90)

#exit
def exit_app():
    if messagebox.askokcancel(title='Exit', message='Are you sure?'):
        root.destroy()



#options- header
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Exit', command=exit_app)
file_menu.add_command(label='About')
menu_bar.add_cascade(label='Options', menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()
