#!/bin/bash

echo "This program requires the following dependencies:"
echo -e "spacy\npandas\ntqdm\nspaCy's en_core_web_md"

echo "Do you want to install them? (y/n):"

#Get response
read -r response


green='\033[0;32m'

#Case statement with what happens when different options are selected
case $response in
[Yy]) 
    echo "Installing..."
    requirements=$(<requirements.txt)

    echo "$requirements"

    # Execute the requirements
    eval "$requirements"

    printf "${green}Installation COMPLETE!"
    exit 0
    ;;
[Nn]) echo "No was pressed. Exiting..."
        exit 0
        ;;
*) echo "o was pressed. Exiting..."
        exit 0
        ;;
esac