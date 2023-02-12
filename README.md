# Deep Model Intrusion Detection Evaluation of NSL KDD and CIC IDS 2018 datasets and Development of SNORT GUI.
<br>
This is a research project to implement intrusion Detection Systems. With the cumulation of an intrusion detection system and SNORT as a primitive inspiration, We compare the real time efficiency of each method.
<br></br>
<img src="https://user-images.githubusercontent.com/70995581/209061112-3de8e0c7-07bd-4f7d-bb74-0c05727c52ec.PNG"/>

<br>**This is currently in progress so I will be updating this repo.......**</br>
<br>

# SNORT
Snort is a Intrusion Detection System developed by OpenSource Sourcefire and currently maintained by Cisco Talos. For now, Snort 2.9 is single threaded, the new Snort 3 is multi-threaded (ie. it can run multiple processes simultaneously). SNORT has a command line interface and no GUI.<br>
### * WHAT DOES IT DO?
Primarily, SNORT runs by predefined rules set by the administrator, if a rule matches, a alert message is displayed in the SNORT console.
### * WHAT HAVE WE DONE HERE?
To facilitate new users and sys admins to understand the dynamic nature of SNORT, we intend to make a Graphical User Interface 
(GUI) to write rules and execute the IDS in the backend while maintaining User friendliness in the frontend.<br>
*DISCLAIMER: As of now, we have written rules for icmp, ftp, and smtp.*
# The SNORT GUI [v1.0.0]
The snort main program consists of:
* A rule generation tool that makes formulating rules faster.
* Open .rules file
* Provide help centre.
# What is [Intrusion detection system overview report.pdf](https://github.com/WhiteHatCyberus/Deep-Model-Evaluation-Intrusion-Detection-System-using-NSL-KDD-CIC-IDS-2018/blob/main/intrusion%20detection%20system%20overview%20report.pdf) ??
This is primarily for the beginners to understand what an IDS is and how it works, Ive added powerpoint slides of references at the end of the report.
* I discussed what an IDS is, types of IDS, detection methods
* Talked about Firewalls, and compared an IDS versus an Enterprise Firewall
* Furthermore, I talked about the Open Source IDS, SNORT and its 3 operational modes and compared it with other counterparts like Suricata and Bro.
* Finally I did add the literature Survey where I compiled all the papers that helped me take an indepth seminar of the IDS and also gave me an insight to simulate real time attacks on the system.
* Ive added the whole architecture of the working of an IDS and its deep model architecture.
<br> Hope this helps ;)<br>
# Connect with me
* [LinkedIn](https://www.linkedin.com/in/whcyberus/)
* [Twitter](https://twitter.com/MattSleety)
* [Blogs](https://ethicalcyberuspathways.wordpress.com/)
# Credits:
Thank you [Joule Effect](https://github.com/jouleffect),
[ChrisJD20](https://github.com/chrisjd20/Snorpy)
