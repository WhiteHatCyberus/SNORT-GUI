# SNORT
Snort is a Intrusion Detection System developed by OpenSource Sourcefire and currently maintained by Cisco Talos. For now, Snort 2.9 is single threaded, the new Snort 3 is multi-threaded (ie. it can run multiple processes simultaneously). SNORT has a command line interface and no GUI.<br>

### WHAT DOES IT DO?
Primarily, SNORT runs by predefined rules set by the administrator, if a rule matches, a alert message is displayed in the SNORT console.
### WHAT HAVE WE DONE HERE?
To facilitate new users and sys admins to understand the dynamic nature of SNORT, we intend to make a Graphical User Interface 
(GUI) to write rules and execute the IDS in the backend while maintaining User friendliness in the frontend.<br>

# SNORT Documentation:
Primarily snort contains a .conf (configuration file) that indexes to a set of rule files. learn documentation [here](http://books.gigatux.nl/mirror/snortids/0596006616/snortids-CHP-5.html)

## Default installation of snort 
SNORT is embedded within the Ubuntu directory, hence it can be installed via the terminal (Ctrl+Alt+T):
```bash
sudo apt install snort -y
```
if manually prompted to enter the network interface snort has to listen to, the information can be obtained by a function called 'ifconfig'
```bash
apt install net-tools -y                  // this installs ifconfig in the system
ifconfig
```
<img width="374" alt="ifconfig" src="https://user-images.githubusercontent.com/70995581/220833040-55b49909-4241-41ac-a80c-2ff7041a963f.png"></br>
> **Note** here enp0s3, enp0s8 and lo are network interfaces

