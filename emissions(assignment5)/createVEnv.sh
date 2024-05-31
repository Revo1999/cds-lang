#!/usr/bin/bash


# create virtual env
python -m venv assignment5_venv
# activate env
source ./assignment5_venv/bin/activate
# install requirements
pip install -r requirements.txt
# close the environment
deactivate


