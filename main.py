from dataFetch import *
from simulations import *
import collections

#currently prints true if random group of 23 dates
#from data.txt contains duplicates
def main():
    birthdays = getDatesFromFile('data.txt')
    print(simulateBirthdayProblem(birthdays, 23))


if __name__ == '__main__':
    main()