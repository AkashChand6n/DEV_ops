#!/bin/bash
#working on how to do variable in shell script
#Author name : akashchand6n
#usage : sh <file.sh> or ./<file.sh>
#in double "" we can give variable but not in ''

var1=10
var2="hello"

echo "$var1 this is variable "
echo "**********************"
echo "$var2 this is a string "

echo '$var1 is it time to have lunch' #we cannot add var here
echo " todays date is `date` " #we added `` to have date inside the echo