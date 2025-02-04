#!/bin/bash
#based on the time print the message
#29-01-2025

echo " date is `date` " # `date` is a command substitution
if [ `date +%H` -lt 12 ] # -lt is used to check if the time is less than 12
then
    echo "Good Morning"
elif [ `date +%H` -lt 16 ] 
then
    echo "Good Afternoon"
elif [ `date +%H` -lt 20 ]
then
    echo "Good Evening"
else
    echo "Good Night"
fi