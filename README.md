# Maidenhead Locator Functions
These scripts contains useful functions related to the maidenhead locator
used in ham radio operations.
(c) 9V1KG

## Scripts
    1. mhconv.py
    2. locdist.py
    3. maiden.py

## 1. mhconv.py
The script is the main program to convert between 
geographical position and/or the open location code (Google plus code) and
the maidenhead locator (4 to 10 char).

## 2. locdist.py
This script calculates the distance and beam direction (azimuth) between 
two locator positions. Put your own locator in as a constant.

    MY_LOC = "XXddxxddxx"
    
## Installation

Install with its own virtual environment

    git clone https://github.com/9V1KG/maidenhead.git
    cd maidenhead
    # create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate
    python setup.py install

Run conversion and distance calculation

    # run locator conversion
    python -m maidenhead
    # run distance/azimuth calculation
    python maidenhead/locdist.py

    
    
    
    
## 3. maiden.py
Module with class and functions for locator conversions.
    
    latlon2maiden  latitude/longitude to locator
    maiden2latlon  locator to latitude/longitude
    dist_az        locator to distance/azimuth
    dg2dms         latitude/longitude dec to deg,min,sec
    
