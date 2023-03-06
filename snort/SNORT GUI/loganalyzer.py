import matplotlib.pyplot as plt
import re
import tkinter as tk
from tkinter import filedialog

filename=filedialog.askopenfilename(initialdir='/etc/snort/logs/', title='Select Alert')
tcp_count = 0
icmp_count = 0
ip_count = 0
udp_count = 0
total_count = 0

with open(filename, 'r') as file:
    for line in file:
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
                    window.title("ICMP Details")
                    window.geometry("600x400")

                    # Create a text box to display the details
                    text_box = tk.Text(window, height=40, width=80)
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
                                if message_tag:
                                    message_tag = message_tag[0]
                                else:
                                    message_tag = ""
                                text_box.insert(tk.END, "Time: {}\nSource IP: {}\nMessage: {}\n\n".format(time_tag, src_ip, message_tag))
                    text_box.config(state="disabled")
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
                        
                        window = tk.Tk()
                        window.title("PORT")
                        window.geometry("600x400")
                        
                        # Get the selected wedge index
                        # Get the selected wedge index
                        if event.inaxes == ax2:
                            for i, wedge in enumerate(wedges2):
                                cont, ind = wedge.contains(event)
                                if cont:
                                    dest_port_number = sorted(dest_port_counts.keys())[i]
                                    break
                        
                        # Create a text box to display the details
                        text_box1 = tk.Text(window, height=40, width=80)
                        text_box1.pack()
                        with open(filename, 'r') as file:
                            for line in file:
                                if "{%s}" % protocol in line and re.findall(r"-> \S+:(\d+)", line)==[dest_port_number]:
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
                                    if message_tag:
                                        message_tag = message_tag[0]
                                    else:
                                        message_tag = ""
                                    text_box1.insert(tk.END, "Time: {}\nSource IP: {}\nProtocol: {}\nPort: {}\nMessage: {}\n\n".format(time_tag, src_ip, protocol, dest_port_number, message_tag))
                        text_box1.config(state="disabled")

                    # Plot the doughnut chart
                    if dest_port_counts:
                        fig2, ax2 = plt.subplots()
                        wedges2, texts2, autotexts2 = ax2.pie(dest_port_counts.values(), labels=dest_port_counts.keys(), wedgeprops={'width': 0.2, 'edgecolor': 'w'}, autopct='%1.1f%%')
                        plt.title("Destination Port Numbers for %s Protocol" % protocol, fontweight="bold", fontsize=16)
                        if protocol == "ICMP":
                            plt.legend(loc="best")
                        fig2.canvas.mpl_connect('motion_notify_event', on_hover_doughnut)
                        fig2.canvas.mpl_connect('button_press_event', lambda event: on_hover_doughnut(event))
                        fig2.canvas.mpl_connect('button_press_event', on_click_doughnut)
                        plt.show()
                    else:
                        print("No destination port numbers found for %s protocol." % protocol)
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

plt.title("Protocol Types", fontweight="bold", fontsize=16)
plt.show()
