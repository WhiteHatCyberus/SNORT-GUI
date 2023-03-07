# for ubuntu configuration in internal network, we assign a static ipv4
import os
os.system('sudo ifconfig enp0s8 192.168.1.2 netmask 255.255.255.0')
