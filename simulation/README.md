# SIMULATION
**Welcome to the main part of this entire project!**
The simulation phase is essential to present the real time analysis and working of our parent application

## Table of Contents
1. [Pre-Requisites](#pre-requisites)
2. [Configuration](#configuration)
3. [Testing](#testing)

## PRE-REQUISITES
What you will need
- Ubuntu (Blue Team, Defender, Server, Target)
- Kali (Red team, Attacker, External user)

## CONFIGURATION
> Firstly lets configure the virtual machines, for this project I've taken the liberty to use ```Oracle VirtualBox 7```

**To set up the testing environment that is isolated from the host system, do the following:**
1. Go to Oracle Virtualbox 7, select the ```Ubuntu``` Virtual Machine, Click ```Settings```, Go to Network.
> Select Network Type as ```Internal Network```, Type Name as 'isolatednetwork'.
2. Repeat step 1 for the ```Kali``` Virtual Machine also.
> Note: Make sure the Internal Network name remains the same for both virtual machines ie. ```isolatednetwork```.
3. Run Kali Linux and Ubuntu simultaneously.
4. In Kali, run ```kali.py```, considering eth0 is the Internal Network Adapter
5. In Ubuntu, run ```ubuntu.py```, considering enp0s3 is the Internal Network Adapter
> Adapter names should be changed accordingly to system configuration, this can be check by running the ```ifconfig``` command.

## TESTING
Now your isolated environment is ready, to check whether the connection is successful, use ```ping```.
