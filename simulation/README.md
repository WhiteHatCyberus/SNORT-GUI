# Simulation
**Welcome to the main part of this entire project!**
The simulation phase is essential to present the real time analysis and working of our parent application

## Table of Contents
1. [Pre-Requisites](#pre-requisites)
2. [Configuration](#configuration)
3. [Testing](#testing)
4. [The Attacker Interface](#the-attacker-interface)

## Pre-Requisites
What you will need
- Ubuntu (Blue Team, Defender, Server, Target)
- Kali (Red team, Attacker, External user)

## Configuration
Firstly lets configure the virtual machines, for this project I've taken the liberty to use ```Oracle VirtualBox 7```

**To set up the testing environment that is isolated from the host system, do the following:**
1. Go to Oracle Virtualbox 7, select the ```Ubuntu``` Virtual Machine, Click ```Settings```, Go to Network. 
2. Select Network Type as 'Internal Network', Type Name as ```isolatednetwork```.
3. Repeat step 1 for the ```Kali``` Virtual Machine also.
> **Note** Make sure the Internal Network name remains the same for both virtual machines ie. ```isolatednetwork```.
4. Run Kali Linux and Ubuntu simultaneously.
5. In Kali, run ```kali.py```, considering eth0 is the Internal Network Adapter
6. In Ubuntu, run ```ubuntu.py```, considering enp0s3 is the Internal Network Adapter
> **Note** Adapter names should be changed accordingly to system configuration, this can be check by running the ```ifconfig``` command.

## Testing
Now your isolated environment is ready, to check whether the connection is successfully established, use ```ping```.

## The Attacker Interface
![Attacker](https://user-images.githubusercontent.com/70995581/223293146-e2ff573f-7b80-4b3c-83e8-5a362d4a107f.png)

It consists of 4 components:
- `Attack Type`: Since we're drawing comparison with the NSL-KDD and CIC IDS 2018 Datasets, it consists of 'Probe','U2R','R2L', and 'DoS'.
- `Target IP`: Enter the Target system IP
- `Check Connection`: This checks if the attack system is connected to the target.
- `Exploit`: Executes the attack on the target machine.

