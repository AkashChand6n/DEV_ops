#!/bin/bash
echo "enter your number:"
read -r num #-r is used to read the input as it is
echo "multiplication tabe of $num is:"
i=1
while [ $i -le 10 ] # -le is used to check if the value of i is less than or equal to 10
do
    mul=`expr $num \* $i` #expr is used to evaluate the expression
    echo "$num * $i = $mul"
    i=`expr $i + 1`
done