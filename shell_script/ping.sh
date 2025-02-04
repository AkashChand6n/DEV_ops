#!/bin/bash
echo -e "enter the ip address to ping" #-e is used to enable the interpretation of backslash escapes
read -r ip #-r is used to read the input from the user
until ping $ip #until loop is used to execute the script until the condition is true
#ping is used to check the connectivity of the network
do  
    echo "Host is down"
    sleep 1 #sleep is used to delay the execution of the script
done
echo "host is $ip up"
