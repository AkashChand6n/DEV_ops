#!/bin/bash
#29-01-2025

function sum {
    local total=$(( $1 + $2))
    echo "$total"
}

echo "enter numbers"
read num1
echo "enter numbers"
read num2

sum $num1 $num2
