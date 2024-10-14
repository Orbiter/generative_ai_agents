#!/bin/bash
# Simple chat client which calls the chat.py script

# Check if at least one argument is given
if [ $# -lt 1 ]; then
    echo "Please provide at least one argument"
    exit 1
fi

# Get the number of arguments
num_args=$#

# Extract all arguments except the last one
args_without_last="${@:1:$(($num_args - 1))}"

# Extract the last argument
last_arg="${!num_args}"

# Call the python script with the arguments and pass the last argument via stdin
echo "$last_arg" | python3 chat.py $args_without_last

# Exit with the return code of the python script
exit $?
