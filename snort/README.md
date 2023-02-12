# SNORT
Snort is a Intrusion Detection System developed by OpenSource Sourcefire and currently maintained by Cisco Talos. For now, Snort 2.9 is single threaded, the new Snort 3 is multi-threaded (ie. it can run multiple processes simultaneously). SNORT has a command line interface and no GUI.<br>
### WHAT DOES IT DO?
Primarily, SNORT runs by predefined rules set by the administrator, if a rule matches, a alert message is displayed in the SNORT console.
### WHAT HAVE WE DONE HERE?
To facilitate new users and sys admins to understand the dynamic nature of SNORT, we intend to make a Graphical User Interface 
(GUI) to write rules and execute the IDS in the backend while maintaining User friendliness in the frontend.<br>
<br>
*DISCLAIMER: As of now, we have written rules for icmp, ftp, and smtp.*
