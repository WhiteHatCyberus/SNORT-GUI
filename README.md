# Deep Model Intrusion Detection Evaluation using NSL KDD and CIC IDS 2018 and Monitoring using SNORT GUI
<br>
This is a experimental project to implement intrusion Detection Systems. With the cumulation of an intrusion detection system and SNORT as a primitive inspiration, We compare the real time efficiency of each method.
<br></br>
<img src="https://user-images.githubusercontent.com/70995581/209061112-3de8e0c7-07bd-4f7d-bb74-0c05727c52ec.PNG"/>

<br>**This is currently in progress so I will be updating this repo.......**</br>
<br>
## 1. NSL KDD: The enhanced KDD Cup 99 [Refer](https://www.unb.ca/cic/datasets/nsl.html)
<br>[The KDD Cup 99 dataset](https://www.tensorflow.org/datasets/catalog/kddcup99) contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.
The competition task was to build a network intrusion detector, a predictive model capable of distinguishing between ''bad’’ connections, called intrusions or attacks, and “good” normal connections.
### -> Improvements to the KDD'99 dataset
The NSL-KDD data set has the following advantages over the original KDD data set:

* It does not include redundant records in the train set, so the classifiers will not be biased towards more frequent records.
* There is no duplicate records in the proposed test sets; therefore, the performance of the learners are not biased by the methods which have better detection rates on the frequent records.
* The number of selected records from each difficultylevel group is inversely proportional to the percentage of records in the original KDD data set. As a result, the classification rates of distinct machine learning methods vary in a wider range, which makes it more efficient to have an accurate evaluation of different learning techniques.
* The number of records in the train and test sets are reasonable, which makes it affordable to run the experiments on the complete set without the need to randomly select a small portion. Consequently, evaluation results of different research works will be consistent and comparable.

## 2. CIC IDS 2018: The successor of the CIC IDS 2017 [Refer](https://www.unb.ca/cic/datasets/ids-2018.html)
<br>[CICIDS2017 dataset](https://www.unb.ca/cic/datasets/ids-2017.html) contains benign and the most up-to-date common attacks, which resembles the true real-world data (PCAPs). It also includes the results of the network traffic analysis using CICFlowMeter with labeled flows based on the time stamp, source, and destination IPs, source and destination ports, protocols and attack (CSV files).</br>
<br>In CSE-CIC-IDS2018 dataset, we use the notion of profiles to generate datasets in a systematic manner, which will contain detailed descriptions of intrusions and abstract distribution models for applications, protocols, or lower level network entities. These profiles can be used by agents or human operators to generate events on the network. Due to the abstract nature of the generated profiles, we can apply them to a diverse range of network protocols with different topologies. Profiles can be used together to generate a dataset for specific needs.</br>
* B-profiles: Encapsulate the entity behaviours of users using various machine learning and statistical analysis techniques (such as K-Means, Random Forest, SVM, and J48). The encapsulated features are distributions of packet sizes of a protocol, number of packets per flow, certain patterns in the payload, size of payload, and request time distribution of a protocol. The following protocols will be simulated in our testbed environment: HTTPS, HTTP, SMTP, POP3, IMAP, SSH, and FTP. Based on our initial observations majority of traffic is HTTP and HTTPS.

* M-Profiles: Attempt to describe an attack scenario in an unambiguous manner. In the simplest case, humans can interpret these profiles and subsequently carry them out. Idealistically, autonomous agents along with compilers would be employed to interpret and execute these scenarios.
# The IDS Application ([ids.rb](https://github.com/WhiteHatCyberus/Deep-Model-Evaluation-Intrusion-Detection-System-using-NSL-KDD-CIC-IDS-2018/blob/main/ids.rb))
Initially I developed a primitive intrusion detection system to detect icmp, ftp and port scans using the Ruby Lanaguage , I will be migrating the application to the python language.<br>
# SNORT
Snort is a Intrusion Detection System developed by OpenSource Sourcefire and currently maintained by Cisco Talos. For now, Snort 2.9 is single threaded, the new Snort 3 is multi-threaded (ie. it can run multiple processes simultaneously). SNORT has a command line interace and no GUI.<br>
### * WHAT DOES IT DO?
Primarily, SNORT runs by predefined rules set by the administrator, if a rule matches, a alert message is displayed in the SNORT console.
### * WHAT HAVE WE DONE HERE?
To facilitate new users and sys admins to understand the dynamic nature of SNORT, we intend to make a Graphical User Interface 
(GUI) to write rules and execute the IDS in the backend while maintaining User friendliness in the frontend.<br>
*DISCLAIMER: As of now, we have written rules for icmp, ftp, and smtp.*
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
[MuratBulbul](https://github.com/muratbulbul)
