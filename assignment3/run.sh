#!/usr/bin/bash

# activate the environment
source assignment3_venv/bin/activate

# run the code
cd src
python query_expansion.py.py
cd ..

# close the environment
deactivate