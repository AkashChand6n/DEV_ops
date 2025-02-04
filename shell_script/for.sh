#!/bin/sh

for I in 1 2 3 4 5 #this is used to iterate over the values
do
    echo "$I"
done

echo "******************************************"

for I in {1..5} #this is used to generate a sequence of numbers
do
    echo "$I"
done
echo "******************************************"

for I in $(seq 1 5) #seq is used to generate a sequence of numbers
do
    echo "$I"
done

echo "******************************************"

for (( I=1; I<=5; I++ )) #I++ is used to increment the value of I by 1
do 
    echo "$I"
done

echo "******************************************"

fruits=("apple" "banana" "cherry" "mango") #array is created here
for fruits in "${fruits[@]}"; #array is used here synatx is ${array[@]}
do
    echo "I like $fruits"
done

echo "************************************************** "

fruits=("apple" "banana" "cherry" "mango") #array is created here
for I in "${!fruits[@]}"; #array is used here synatx is ${array[@]}
do
    echo "$I i like ${fruits[$I]}"
done

echo "***************************************************"

fruits=("apple" "banana" "cherry" "mango") #array is created here
for I in "${!fruits[@]}"; #array is used here synatx is ${array[@]}
do  
    if (( $I%2==0 )); then
        echo " i like  ${fruits[$I]}"
    else
        echo " i dont like ${fruits[$I]}"
    fi
done

echo "***************************************************"

#!/bin/bash

fruits=("apple" "banana" "cherry" "mango") #array is created here

for I in "${!fruits[@]}"; #array is used here synatx is ${array[@]}
do  
    if [ $(expr $I % 2) -eq 0 ]; then
        echo "I like ${fruits[$I]}"
    else
        echo "I don't like ${fruits[$I]}"
    fi
done