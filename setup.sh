#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install Flask and Flask-Cors
pip3 install Flask
pip3 install Flask-Cors

# Install mysql-connector-python
pip install mysql-connector-python


