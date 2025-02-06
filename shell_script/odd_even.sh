echo "enter the number"
read -r n
if [ $((n % 2)) -eq 0 ]; then
    echo "even"
else
    echo "odd"
fi