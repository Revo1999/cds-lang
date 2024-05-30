#!/usr/bin/bash

# activate the environment
source assignment1_venv/bin/activate

# run the code
cd src
python spacy_extract.py
cd ..

# close the environment
deactivate