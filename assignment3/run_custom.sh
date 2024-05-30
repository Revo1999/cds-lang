#!/usr/bin/bash

# activate the environment
source assignment3_venv/bin/activate

# Ask the user a question
echo "Name an artist (For example: Black Sabbath)"

# Read the user's response
read flags1

# Ask the user a question
echo "Name a word - must only be one word (for example love)"

# Read the user's response
read flags2

# Ask the user a question
echo "How many words should the model extend your search? (Default is: 3)"

# Read the user's response
read flags3
 
# Add quotes around the responses
fixed_flags1="\"$flags1\""

# run the code
cd src
# Need extra quotes otherwise artist with multiple words will not be parsed
python query_expansion.py -a "$flags1" -w $flags2 -m $flags3
cd ..

# close the environment
deactivate