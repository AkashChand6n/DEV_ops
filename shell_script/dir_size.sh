#!/bin/bash
echo "enter the directory you want to check:"
read -r dir
du -h "$dir" | cut -f1

echo "====================="

du -sh "$dir" | awk '{print $1}'

echo "====================="

du -h "$dir"

echo "====================="