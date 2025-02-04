#!/bin/bash
#regular expression
#29-01-2025

numstring="1234567890abc"
if [[ $numstring =~ ^1 ]]; #[[]] is used to match the regular expression and [] is used to match the character
#=~ ^ is used to match the regular expression
then
    echo "$numstring Start with 1"
fi

if [[ $numstring =~ ^[1.7] ]]; #[1.7] is used to match the character 1 and 7
then
    echo "$numstring Start with 1 and have 7 inbetween"
fi

if [[ $numstring =~ 0$ ]]; #0$ is used to match the character 0 at the end
then
    echo "$numstring End with 0"
fi

if [[ $numstring =~ [a-z] ]]; #[a-z] is used to match the small letter
then
    echo "$numstring have small letter"
fi