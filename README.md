# SNORT GUI and Deep Model Intrusion Detection Evaluation of NSL KDD and CIC IDS 2018 datasets.

This research project implements a Network Intrusion Detection System, comparing the real-time efficiency of each method through the cumulation of an intrusion detection system and SNORT as a primitive inspiration.

## Table of Contents
1. [Research Architecture](#research-architecture)
2. [The SNORT GUI v1.0.0](#the-snort-gui-v100)
    * [Pre-requisite](#pre-requisite)
    * [Download](#download)
    * [Installation](#installation)
3. [Connect with Me](#connect-with-me)
4. [Credits](#credits)

## Research Architecture

![Research Architecture](https://user-images.githubusercontent.com/70995581/209061112-3de8e0c7-07bd-4f7d-bb74-0c05727c52ec.PNG)

> **Warning** This is currently in progress, so I will be updating this repository.

## The SNORT GUI v1.0.0

The SNORT GUI main program consists of:

- A rule generation tool that makes formulating rules faster.
- Open `.rules` file
- Provide help center.

### Pre-requisite

1. A Linux distro (preferably Ubuntu).

### Download

1. Download the latest `snort.tar.gz` release (tag: v1.0) available in the "Releases" tab.
2. Alternatively, download via Git, and access "snort/SNORT GUI/" for application files.

### Installation

For first-time installation, run:

```bash
sudo python3 installerwizard.py
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

![Log Analyzer](https://user-images.githubusercontent.com/70995581/223300847-fb89a2ed-4106-41f7-bf3d-f3d0ce06c2da.png)

Figure 2.3: Log Analyzer Tool

> **Note**: Will be releasing the documentation for the last module `run ids` very soon, primary testing has been completed, but we need to incorporate a flexible system to run snort in any Ubuntu or Linux distro with snort installed, based on network interfaces, configuration file, log file path and mode of detection  to be used.

## Connect with me

- [LinkedIn](https://www.linkedin.com/in/whcyberus/)
- [Blogs](https://ethicalcyberuspathways.wordpress.com/)
- [Email](mailto:whcyberus@gmail.com)

## Credits

Thank you [Joule Effect](https://github.com/jouleffect) and [ChrisJD20](https://github.com/chrisjd20/Snorpy).
