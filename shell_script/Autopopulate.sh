#!/bin/bash
#autopopulate the script
#29-01-2025

echo "All the arguments in $*" # $* is used to print all the arguments
echo "No of Arguments $#" # $# is used to print the number of arguments
echo "First Argument $1" # $1 is used to print the first argument
echo "expand all the command line on separate words $@" # $@ is used to expand all the command line arguments on separate words
echo "PID of the current  $$" # $$ is used to print the PID of the current process

sleep 400 & # sleep for 400 seconds & is used to run the process in the background
echo "PID of recently added background process $!" # $! is used to print the PID of the recently added background process
echo "File name of the current program $0" # $0 is used to print the file name of the current program