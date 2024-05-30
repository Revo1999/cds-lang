#!/usr/bin/bash


# create virtual env
python -m venv assignment3_venv
# activate env
source ./assignment3_venv/bin/activate
# install requirements
pip install -r requirements.txt
# close the environment
deactivate


