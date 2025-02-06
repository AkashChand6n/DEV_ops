#!/bin/bash
echo "enter the message you want to print:"
read -r message

print_fun() {
    echo "The message is: $1"
}

print_fun "$message"