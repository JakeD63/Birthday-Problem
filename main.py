from datetime import *

def main():
    extractDates('data.txt')

def extractDates(filepath):
    dataFile = open(filepath, 'r')


def extractDayOfYear(date, format = '%m/%d/%Y'):
    dateobj = datetime.strptime(date, format).date()
    day_of_year = dateobj.timetuple().tm_yday
    return day_of_year

if __name__ == '__main__':
    main()