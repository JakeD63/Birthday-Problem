from DataFetch import getDatesFromFile
from Simulations import *

def main():
    # currently prints true if random group of 23 dates
    # from data.txt contains duplicates
    sampleSize = 23
    birthdays = generateRandomBirthdays(sampleSize)
    print(simulateBirthdayProblem(birthdays, sampleSize))


if __name__ == '__main__':
    main()