#!/bin/bash
#set is used to set the date and time
#29-01-2025

set -x #-x is used to print the command before executing it
set`date` #set is used to set the date and time
echo "Today is $1"
echo "Month is $2"
echo "Date is $3"
echo "Year is $4"

echo "Time is $5"
echo "AM/PM or ? $6"
