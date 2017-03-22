from DataFetch import *
from Simulations import *
import collections


def main():
    # currently prints true if random group of 23 dates
    # from data.txt contains duplicates
    birthdays = getDatesFromFile('data.txt')
    print(simulateBirthdayProblem(birthdays, 23))


if __name__ == '__main__':
    main()