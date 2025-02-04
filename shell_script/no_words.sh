#!/bin/bash
#Write a script to count the number of words in a given string.
#29-01-2025

echo "Enter the string"
read -r string
wordcount=$( wc -w <<< "$string"  ) 
# wordcount=$( echo "$string" | wc -w) #wc -w is used to count the number of words
echo "The number of words in the string is $wordcount"