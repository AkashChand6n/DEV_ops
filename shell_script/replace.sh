#!/bin/bash
#Write a script to replace a word in a file with another word.
#29-01-2025

echo "Enter the file name"
read -r file
echo "Enter the word to be replaced"
read -r word
echo "Enter the word to be replaced with"
read -r replace

sed -i "s/$word/$replace/g" "$file" #s/ is used to replace the word
                                    #/g is used to replace all the occurences of the word
echo "The word has been replaced"