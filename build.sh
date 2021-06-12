#!/bin/bash

#install requirements
pip3 install -r requirements.txt

#migrate database
python3 manage.py migrate

#more things should be added here