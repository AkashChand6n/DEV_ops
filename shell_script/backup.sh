#!/bin/bash
#backup of the file and save in the backup folder
#29-01-2025

function backup {
    echo "enter the file name"
    read -r file
    if [ -f $file ]
    then
        echo "file exists"
        mkdir backup
        cp $file ./backup/$file
        echo "backup of the file is done"
    else
        echo "file does not exist"
    fi
    if [ $? -ne 0 ] # $? is used to check the status of the last executed command
    then
        echo " backup failed $? "
    fi
}

backup