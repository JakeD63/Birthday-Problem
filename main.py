from DataFetch import getDatesFromFile
from Simulations import *

def main():
    testRun()

def testRun():
    timesToRun = 1000
    peopleSelected = 23
    populationSample = getDatesFromFile('data.txt')

    populationSuccess, randomSuccess = compareSampleWithRandomData(populationSample, timesToRun, 23)
    outputComparison([populationSuccess, randomSuccess], ["CSC Population Sample", "Pure Random Sample"], timesToRun, peopleSelected)



if __name__ == '__main__':
    main()