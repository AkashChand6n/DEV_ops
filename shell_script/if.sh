#!/bin/bash
read -p "Enter the file name: " file #why we use -p is to prompt the user to enter the file name
if [ -f "$file" ]; # -f is used to check if the file exists or not
then
    echo "File exists"
else
    echo "File does not exist"
fi

if [[ -f $file ]]; # -f is used to check if the file exists or not
then
    echo "File exists"
else
    echo "File does not exist"
fi

#In shell scripting, `[]` and `[[]]` are used for different purposes:

### `[]` (Single Brackets)
#- Used for POSIX-compliant test commands.
#- Can be used for basic conditional expressions.
#- Supports string comparisons, file tests, and arithmetic comparisons.
#- Requires spaces around the brackets and operators.

### `[[]]` (Double Brackets)
#- Used for extended test commands in Bash.
#- Provides more features and flexibility compared to single brackets.
#- Supports pattern matching (e.g., `==`, `!=` with wildcards), logical operators (`&&`, `||`), and regex matching (`=~`).
#- Does not require escaping certain characters like `<`, `>`, `&`, `|`.