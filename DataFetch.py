from datetime import *

def getDatesFromFile(filepath):
    dates = extractDates(filepath)
    birthdays = []
    for i in dates:
        birthdays.append(extractDayOfYear(i))
    return birthdays

def extractDates(filepath):
    dates = []
    dataFile = open(filepath, 'r')
    for line in dataFile:
        dates.append(str.strip(line))
    return dates


def extractDayOfYear(date, format = '%m/%d/%Y'):
    dateobj = datetime.strptime(date, format).date()
    day_of_year = dateobj.timetuple().tm_yday
    return day_of_year