import tkinter as tk

root = tk.Tk()
root.title("Attack Simulator - Kali Linux")
root.geometry("600x200")
attacks= ["DoS", "Probe", "U2R", "R2L"]
current_attack = tk.StringVar(root)
current_attack.set(attacks[0])

label_attack = tk.Label(root, text="Select an attack: ")
label_attack.grid(row=1, column=1)

menu = tk.OptionMenu(root, current_attack, *attacks)
menu.grid(row=1, column=2)

attack_value = current_attack.get()
ip_value = ""
check_value = False

def update_ip_value(event):
    global ip_value
    ip_value = ip_tbox.get("1.0", tk.END)

label_ip = tk.Label(root, text="IP Address:")
label_ip.grid(row=1, column=3, padx = (150, 0))

ip_tbox = tk.Text(root, height=1, width=25)
ip_tbox.bind("<KeyRelease>", update_ip_value)
ip_tbox.grid(row=1, column=4)

def checker():
    if check_value == False:
        print("Connection not established")
    else:
        print("Connection Established")

check_b = tk.Button(root, text="Check", command=checker)
check_b.grid(row=2,column=4)

def printer():
    attack_value = current_attack.get()
    ip_value = ip_tbox.get("1.0", tk.END)
    print(attack_value)
    print(ip_value)

print_b = tk.Button(root, text="Execute", command=printer)
print_b.grid(row=3, column=3, pady = (100, 0))

root.resizable(False, False)
root.mainloop()