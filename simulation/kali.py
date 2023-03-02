# for kali configuration in internal network, we assign a static ipv4
import os
os.system('sudo ifconfig eth0 192.168.1.3 netmask 255.255.255.0')
