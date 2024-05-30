#!/usr/bin/bash


# create virtual env
python -m venv assignment4_venv
# activate env
source ./assignment4_venv/bin/activate
# install requirements
pip install -r requirements.txt
# close the environment
deactivate


