#!/bin/bash
#working on how to do variable in shell script
#Author name : akashchand6n
#usage : sh <file.sh> or ./<file.sh>
#in double "" we can give variable but not in ''

var1=10
var2="hello"
hostnme=`hostname`
date=`date`
#the following var are not allowed
1val=100
false@linux=false

echo "var1=$var1 "
echo "var2=$var2 "
echo "hostname=$hostnme"
echo "date=$date"
echo "1val=$1val"
echo "false@linux=$false@linux"