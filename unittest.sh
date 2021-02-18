#!/bin/bash
echo "Instantiating virtualenv and running unit tests..."ls
virtualenv -p python3 virtualenv_temp
source virtualenv_temp/bin/activate
echo "Activated Virtualenv."
echo "Installing dependencies..."
pip install "pytest<5"
pip install .
pip install -r requirements_dev.txt
pip install -r requirements.txt
virtualenv_temp/bin/coverage run -m pytest
virtualenv_temp/bin/coverage report -m
echo "Unit tests complete."
echo "Deactivating Virtualenv..."
deactivate
rm -rf ./virtualenv_temp
echo "Virtualenv deactivated."
echo "Local test complete."