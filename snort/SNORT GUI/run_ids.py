import tkinter as tk
import datetime
import os


if not os.path.exists('/etc/snort/ids.conf'):
    os.system('sudo cp ~/Desktop/SNORT-GUI/snort/ids.conf /etc/snort/')

if not os.path.exists('/etc/snort/rules/ids.rules'):
    os.system('sudo cp ~/Desktop/SNORT-GUI/snort/rules/ids.rules /etc/snort/rules/')


foldername='/etc/snort/logs'

def run_snort():
    datetime_string = datetime.datetime.now().strftime("%d-%m-%y@%H.%M.%S")
    new_folderpath='/etc/snort/logs/'+datetime_string
    os.system('sudo mkdir '+new_folderpath)
    os.system('sudo snort -A console -A fast -q -c /etc/snort/ids.conf -i enp0s8 -l '+new_folderpath)


if not os.path.exists(foldername):
    os.system('sudo mkdir '+foldername)
    run_snort()
else:
    run_snort()

