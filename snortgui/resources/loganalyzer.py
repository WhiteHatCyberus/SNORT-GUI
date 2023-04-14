import matplotlib.pyplot as plt
import re
import tkinter as tk
import tkinter
from tkinter import filedialog, messagebox

#security

with open('.resources/temp/admin.pass', 'r') as file:
    sudo_passwd = file.read()

i=3
try:
    while i>0:
        sudo_password = tkinter.simpledialog.askstring("Password", "\nEnter your administrator password:\n", show='*')

        if sudo_password==sudo_passwd:
            i=0 
            # open the file
            filename = filedialog.askopenfilename(initialdir='/etc/snort/logs/', title='Select Alert')
            if not filename:
                messagebox.showerror("Error", "Alert File not selected")
            else:
                with open(filename, 'r') as file:
                    # read the contents of the file
                    file_contents = file.read()

                    # check if the file is empty
                    if not file_contents:
                        # if the file is empty, display an error message
                        root = tk.Tk()
                        root.withdraw()
                        messagebox.showerror("Error", "No Alerts detected!")
                        exit()
                    else:
                        # if the file is not empty, iterate through each line
                        tcp_count = 0
                        icmp_count = 0
                        ip_count = 0
                        udp_count = 0
                        total_count = 0
                        for line in file_contents.split('\n'):
                            total_count += 1
                            if "{TCP}" in line:
                                tcp_count += 1
                            if "{ICMP}" in line:
                                icmp_count += 1
                            if "{IP}" in line:
                                ip_count += 1
                            if "{UDP}" in line:
                                udp_count += 1

                labels = []
                counts = []
                colors = []

                if tcp_count > 0:
                    labels.append("TCP")
                    counts.append(tcp_count)
                    colors.append('tab:blue')
                if icmp_count > 0:
                    labels.append("ICMP")
                    counts.append(icmp_count)
                    colors.append('tab:orange')
                if ip_count > 0:
                    labels.append("IP")
                    counts.append(ip_count)
                    colors.append('tab:green')
                if udp_count > 0:
                    labels.append("UDP")
                    counts.append(udp_count)
                    colors.append('tab:red')

                fig1, ax1 = plt.subplots()
                wedges, texts, autotexts = ax1.pie(counts, labels=labels, colors=colors, wedgeprops={'width': 0.2, 'edgecolor': 'w'}, autopct='%1.1f%%')
                plt.setp(autotexts, size=12)

                def explode_pie_chart(i):
                    new_alphas = [0.5] * len(wedges)
                    new_alphas[i] = 1.0
                    for j, wedge in enumerate(wedges):
                        wedge.set_alpha(new_alphas[j])
                    plt.draw()

                def on_click(event):
                    # Get the selected wedge index
                    if event.inaxes == ax1:
                        for i, wedge in enumerate(wedges):
                            cont, ind = wedge.contains(event)
                            if cont:
                                protocol = labels[i]
                                if protocol == "ICMP":              
                                
                                    # Create a new tkinter window
                                    window = tk.Tk()
                                    window.title("EVENT BREAKDOWN FOR ICMP ALERTS")
                                    window.geometry("600x400")

                                    scrollbar = tk.Scrollbar(window)
                                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                                    # Create a text box to display the details
                                    text_box = tk.Text(window, height=40, width=80, yscrollcommand=scrollbar.set)
                                    text_box.pack(side=tk.LEFT, fill=tk.BOTH)
                                    text_box.pack()

                                    # Get the time tags, source IPs, and message tags for ICMP packets
                                    with open(filename, 'r') as file:
                                        for line in file:
                                            if "{ICMP}" in line:
                                                time_tag = re.findall(r"\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+", line)
                                                if time_tag:
                                                    time_tag = time_tag[0]
                                                else:
                                                    time_tag = ""
                                                src_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                                                if src_ip:
                                                    src_ip = src_ip[0]
                                                else:
                                                    src_ip = ""
                                                message_tag = re.findall(r"\[\*\*\] (.*) \[\*\*\]", line)
                                                priority=re.findall(r"\[Priority: (\d)\]",line)
                                                if priority:
                                                    priority=priority[0]
                                                else:
                                                    priority="N/A"
                                                if message_tag:
                                                    message_tag = message_tag[0]
                                                else:
                                                    message_tag = ""
                                                text_box.insert(tk.END, "Time: {}\nSource IP: {}\nMessage: {}\nPriority: {}\n\n".format(time_tag, src_ip, message_tag,priority))
                                    text_box.config(state="disabled")
                                    scrollbar.config(command=text_box.yview)
                                else:
                                    # Generate doughnut chart for destination port numbers
                                    dest_port_counts = {}
                                    with open(filename, 'r') as file:
                                        for line in file:
                                            if "{%s}" % protocol in line:
                                                # Extract the destination port number
                                                dest_port_number = re.findall(r"-> \S+:(\d+)", line)
                                                if dest_port_number:
                                                    dest_port_number = dest_port_number[0]
                                                    if dest_port_number in dest_port_counts:
                                                        dest_port_counts[dest_port_number] += 1
                                                    else:
                                                        dest_port_counts[dest_port_number] = 1
                                    
                                    def on_hover_doughnut(event):
                                        if event.inaxes == ax2:
                                            for i, wedge in enumerate(wedges2):
                                                cont, ind = wedge.contains(event)
                                                if cont:
                                                    new_alphas = [0.5] * len(wedges2)
                                                    new_alphas[i] = 1.0
                                                    for j, w in enumerate(wedges2):
                                                        w.set_alpha(new_alphas[j])
                                                    plt.draw()
                                                    break
                                                else:
                                                    for wedge in wedges2:
                                                        wedge.set_alpha(0.3)
                                        else:
                                            for wedge in wedges2:
                                                wedge.set_alpha(1)
                                            plt.draw()

                                    def on_click_doughnut(event):
                                        
                                        
                                        # Get the selected wedge index
                                        if event.inaxes == ax2:
                                            for i, wedge in enumerate(wedges2):
                                                cont, ind = wedge.contains(event)
                                                if cont:
                                                    dest_port_number = list(dest_port_counts.keys())[i]
                                                    break
                                        
                                        window = tk.Tk()
                                        window.title("EVENT BREAKDOWN FOR {} PORT {}".format(protocol,dest_port_number))
                                        window.geometry("600x400")

                                        # Create the scrollbar widget
                                        scrollbar = tk.Scrollbar(window)
                                        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                                        # Create a text box to display the details
                                        text_box1 = tk.Text(window, height=40, width=80, yscrollcommand=scrollbar.set)
                                        text_box1.pack(side=tk.LEFT, fill=tk.BOTH)
                                        with open(filename, 'r') as file:
                                            for line in file:
                                                if "{%s}" % protocol in line and re.findall(r"-> \S+:(\d+)", line)==[dest_port_number]:
                                                    time_tag = re.findall(r"\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+", line)
                                                    if time_tag:
                                                        time_tag = time_tag[0]
                                                    else:
                                                        time_tag = ""
                                                    src_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                                                    priority=re.findall(r"\[Priority: (\d)\]",line)
                                                    if priority:
                                                        priority=priority[0]
                                                    else:
                                                        priority="N/A"
                                                    if src_ip:
                                                        src_ip = src_ip[0]
                                                    else:
                                                        src_ip = ""
                                                    message_tag = re.findall(r"\[\*\*\] (.*) \[\*\*\]", line)
                                                    if message_tag:
                                                        message_tag = message_tag[0]
                                                    else:
                                                        message_tag = ""
                                                    text_box1.insert(tk.END, "Time: {}\nSource IP: {}\nProtocol: {}\nPort: {}\nMessage: {}\nPriority: {}\n\n".format(time_tag, src_ip, protocol, dest_port_number, message_tag,priority))
                                        text_box1.config(state="disabled")
                                        scrollbar.config(command=text_box1.yview)

                                    # Plot the doughnut chart
                                    if dest_port_counts:
                                        fig2, ax2 = plt.subplots()
                                        counts2 = list(dest_port_counts.values())
                                        labels2 = list(dest_port_counts.keys())
                                        wedges2, texts2, autotexts2 = ax2.pie(counts2, wedgeprops={'width': 0.2, 'edgecolor': 'w'}, autopct='%1.1f%%')
                                        ax2.legend(wedges2, labels2, title=protocol+" PORTS EXPLOITED", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
                                        plt.setp(autotexts2, size=12)

                                        # Add hover and click events to the doughnut chart
                                        cid_hover = fig2.canvas.mpl_connect('motion_notify_event', on_hover_doughnut)
                                        cid_click = fig2.canvas.mpl_connect('button_press_event', on_click_doughnut)
                                        fig2.set_size_inches(12,8)
                                        # Show the doughnut chart
                                        plt.show()

                                    else:
                                        messagebox.showerror("Error", f"No destination port numbers found for {protocol} protocol.")
                                break

                def on_hover(event):
                    if event.inaxes == ax1:
                        for i, wedge in enumerate(wedges):
                            cont, ind = wedge.contains(event)
                            if cont:
                                explode_pie_chart(i)
                                break
                            else:
                                wedge.set_alpha(0.3)
                    else:
                        for wedge in wedges:
                            wedge.set_center((0, 0))
                            wedge.set_alpha(1)
                        plt.draw()

                fig1.canvas.mpl_connect('motion_notify_event', on_hover)
                fig1.canvas.mpl_connect('button_press_event', lambda event: on_hover(event))
                fig1.canvas.mpl_connect('button_press_event', on_click)

                plt.title("Exploited Protocols", fontweight="bold", fontsize=16)
                plt.show()
        elif(sudo_password is None):
            exit()
        elif(sudo_password==""):
            messagebox.showerror("Error","Enter password")
        else:
            messagebox.showerror("Error", "ⓘ Incorrect password, try again. (Attempt:"+str(i)+")")
            i=i-1
except tk.TclError:
    exit()