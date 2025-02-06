echo "enter the directory"
read -r dir
if [ -d $dir ]; then
    echo "directory exists"
    zip -r "$dir".zip "$dir" # -r flag is used to recursively zip the directory
else
    echo "directory does not exist"
    exit 1
fi

if [ -f "$dir".zip ]; then
    echo "zip file exists"
else
    echo "zip file does not exist"
    exit 1
fi