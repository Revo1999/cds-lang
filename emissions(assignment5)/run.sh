#!/usr/bin/bash

# activate the environment
source assignment5_venv/bin/activate

# run the code
cd src
python prepper.py
cd ..

# close the environment
deactivate