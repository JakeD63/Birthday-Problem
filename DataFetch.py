from datetime import datetime

def getDatesFromFile(filepath):
    # returns an array with days of the year
    # using date from filepath's file
    dates = extractDates(filepath)
    birthdays = []
    for i in dates:
        birthdays.append(extractDayOfYear(i))
    return birthdays

def extractDates(filepath):
    # gets date string from file at filepath
    # returns array of strings from file
    dates = []
    dataFile = open(filepath, 'r')
    for line in dataFile:
        dates.append(str.strip(line))
    return dates


def extractDayOfYear(dateString, dateFormat = '%m/%d/%Y'):
    # changes date string to day of the year using date objects
    # params: dateString - date to convert (ex.10/10/2017)
    #         dateFormat - format that dateString is in (default value mm/dd/YY)
    dateobj = datetime.strptime(dateString, dateFormat).date()
    day_of_year = dateobj.timetuple().tm_yday
    return day_of_year