#!/usr/bin/bash


# create virtual env
python -m venv assignment1_venv

# activate env
source ./assignment1_venv/bin/activate

# install requirements
pip install -r requirements.txt

# Download the spaCy model
python -m spacy download en_core_web_md

# close the environment
deactivate

# Print a message to user saying its done
echo Environment is all set up!




