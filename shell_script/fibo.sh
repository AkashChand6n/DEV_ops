#!/bin/bash
read -p "Enter the number of elements : " N
a=0
b=1 
echo "The Fibonacci series is : "

for (( i=0; i<N; i++ ))
do
	echo -n "$a "
	fn=$((a + b))
	a=$b
	b=$fn
done
# The Fibonacci series is : 0 1 1 2 3 5

