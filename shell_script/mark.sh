#!/bin/bash
#Ask for match if any mark is below 35 fail
#If all marks are above 35 pass find the average mark and display first class and distinction
#29-01-2025

set -x
echo "Enter the marks of maths"
read -r maths
echo "Enter the marks of science"
read -r science
echo "Enter the marks of language"
read -r language

function average {
    total=$(( $maths + $science + $language ))
    average=$((total / 3))
    if [ $average -ge 75 ]
    then
        echo "Distinction"
    elif [ $average -ge 60 ]
    then
        echo "First Class"
    fi
}

function pass {
    if [ $maths -lt 35 ] || [ $science -lt 35 ] || [ $language -lt 35 ]
    then
        echo "Fail"
    else
        echo "Pass"
        average $maths $science $language
    fi
}

pass

# average function call removed as it is already called within pass function

# if [ $maths -lt 35 ] || [ $science -lt 35 ] || [ $language -lt 35 ]
# then
#     echo "Fail"
# else
#     echo "Pass"
#     total=$(( $maths + $science + $language ))
#     average=$((total / 3))
#     echo "Average is $average"
#     if [ $average -gt 75 ]
#     then
#         echo "Distinction"
#     elif [ $average -gt 60 ]
#     then
#         echo "First Class"
#     fi
# fi