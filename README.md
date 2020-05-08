# Maidenhead Locator Functions
These scripts contains useful functions related to the maidenhead locator
used in ham radio operations.
(c) 9V1KG

## Scripts
    1. maiden.py
    2. locdist.py

## maiden.py
The script contains the class with functions to calculate the maidenhead locator (4 to 10 char), 
geographical position and/or the open location code (Google plus code).
Run the script and input position, locator or open location code to get the 
result.

To calculate Google plus code the openlocationcode module needs to be installed:

    pip install openlocationcode

## locdist.py
This script calculates the distance and beam direction (azimuth) between 
two locator positions. Put your own locator as constant.

    MY_LOC = "XXddxxddxx"
    
## Installation

Install in a project folder with its own virtual environment

    # make project directory
    mkdir ~/maiden
    cd maiden
    # create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate

Get module from git and run

    git clone https://github.com/9V1KG/maidenhead.git
    cd ~/maiden/maidenhead
    python3 setup.py install
    python3 -m maiden
    
    
    
    
    
