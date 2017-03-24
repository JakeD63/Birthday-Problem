# Birthday-Problem
Simulations of the birthday problem using population data from SDSMT students

## Usage
Run main.py with python3, will print true if the random sample from the population contained duplicates.

## Overview

### main.py
Driver for the program, gets list of birthdays and calls the simulation

### DataFetch.py
Provides functions for reading birthdays in and converting them from a date to a day of the year (1-366)

### Simulations.py
Contains functions for simulating the birthday problem with our data with n selections
Also contains a function to compare two samples n number of times

DEPENDENCIES:
You will need to install numpy in order for some of these functions to work. This can be done with
pip3 install numpy (you may need to sudo this)
