#!/bin/bash
echo "enter the number"
read -r n
if [ $((n % 2)) == 0 ]; then
    echo "even"
else
    echo "odd"
fi