#!/bin/bash
sudo apt update
sudo apt install lshw -y
sudo apy install neofetch -y
sudo lshw -short
sudo neofetch

#lshw is a small tool to extract detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or IA-64 systems and on some PowerPC machines (PowerMac G4 is known to work).
#lshw -short