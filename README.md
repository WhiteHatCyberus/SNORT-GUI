# SNORT GUI and Deep Model Intrusion Detection Evaluation of NSL KDD and CIC IDS 2018 datasets.

A actively developed blue team application for SNORT. Intended for forensic, incident handling and analysis.

## Table of Contents
1. [Research Architecture](#research-architecture)
2. [SNORT GUI v2](#snort-gui-v2)
    * [Pre-requisite](#pre-requisite)
    * [Download](#download)
    * [Installation](#installation)
3. [Connect with Me](#connect-with-me)
4. [Credits](#credits)

## Research Architecture

![Research Architecture](https://user-images.githubusercontent.com/70995581/229307468-1aa44b4f-0695-4f10-ba31-b71a0360c0ed.png)


> **Warning** This is currently in progress, so I will be updating this repository.

## SNORT GUI v2 

> STATUS: :heavy_check_mark:

The SNORT GUI main program consists of:

- SNORT Rule Generator: Open, Write, Save `.rules` files - **Pre-incident/Preparation**
- Open Configuration Files: Manually Open `.conf` and `.rules` files - **Pre-incident/Preparation**
- Alert Log Analyzer: Analyze SNORT alerts and distinguishing them by protocols and ports for ease of documentation for cyberforensics - **Post-incident/Forenisc Analysis**
- Run SNORT: Runs the SNORT application in **Intrusion Detection System Mode**.
```bash
snort -A console -A fast -q -i <network_interface> -c <configuration_file> -l <log_folderpath>
```
>  :bangbang:  Help: **Currently In Development** covers snort documentation, simulation guides, walkthroughs, snort rule formulation, basic attack and mitigation walkthroughs.

### Pre-requisite

1. A Linux distro (preferably Ubuntu).

### Download

1. Download the latest `snortgui-enterprise-edition.zip` release (tag: v2) available in the "Releases" tab.
2. Alternatively, download via Git, and navigate to "snort/snortgui/" for application files.
> **Note**: If you opt for **method 2**, rename the `resources` folder to `.resources`.

### Installation

For first-time installation, run:

```bash
sudo python3 installer.py
```

   ![Terms and Condition](https://user-images.githubusercontent.com/70995581/219879971-e67a8a21-962b-4f18-ad63-8813ba5f5b6a.png)

   Figure 1.1: Terms and Conditions
   
   ![Installing resources](https://user-images.githubusercontent.com/70995581/223300214-8474d391-d4cb-4bec-9554-4b23e2510923.png)


   Figure 1.2: Installing resources

2. After installation, you can launch the application by running:

```bash
sudo python3 snortgui.py
```

![SNORT GUI main menu](https://user-images.githubusercontent.com/70995581/223300378-1235b879-6d70-4d4c-838a-c57557107662.png)


Figure 2.1: SNORT GUI main menu

![Rule Generator GUI](https://user-images.githubusercontent.com/70995581/223300719-4b603ed9-a5a3-482c-b409-6612a8f9b8e1.png)


Figure 2.2: Rule Generator GUI


![Log Analyzer](https://user-images.githubusercontent.com/70995581/227723225-e67f63cb-6b2d-4ce8-b42d-874ff8fcc381.png)


Figure 2.3: Log Analyzer Tool

3. Run SNORT IDS:

![Run SNORT](https://user-images.githubusercontent.com/70995581/229309507-cb79f013-af93-4245-b6be-2e9d5fd4d5f3.png)<br>

Figure 3.1: Configuring SNORT

![SNORT running](https://user-images.githubusercontent.com/70995581/229309060-e7671380-34dc-4e6c-891a-47423f8250ee.png)<br>

Figure 3.2: Running SNORT

> **Note**: SNORT GUI v1.1 features security patches and bug fixes, additionally running resources via downloading the repository will not work, make sure you download the latest stable release of `snortgui.zip` to run the application hassle free.

## Connect with me

- [LinkedIn](https://www.linkedin.com/in/whcyberus/)
- [Blogs](https://ethicalcyberuspathways.wordpress.com/)
- [Email](mailto:whcyberus@gmail.com)

## Credits

Thank you [Joule Effect](https://github.com/jouleffect) and [ChrisJD20](https://github.com/chrisjd20/Snorpy).
