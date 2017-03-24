# Birthday-Problem
Simulations of the birthday problem using population data from SDSMT students

## Usage
Run main.py with python3, prints statistics summary of samples

## Overview

### main.py
Driver for the program, gets list of birthdays and calls the simulation

### DataFetch.py
Provides functions for reading birthdays in and converting them from a date to a day of the year (1-366).
Data input is expected in .txt format, one birthday per line in format dd/mm/YYYY

### Simulations.py
Contains functions for simulating the birthday problem with our data with n selections.
Also contains a function to compare many samples n number of times

## Dependencies
You will need to install numpy in order for some of these functions to work. This can be done with
pip3 install numpy (you may need to sudo this)
