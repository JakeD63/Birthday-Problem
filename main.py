from DataFetch import getDatesFromFile
from Simulations import *

def main():
    testRun()

def testRun():
    timesToRun = 1000
    groupSize = 23
    populationSample = getDatesFromFile('data.txt')
    randomSample = generateRandomBirthdays(len(populationSample))
    weightedSample = generateWeightedBirthdays(populationSample, len(populationSample))
    results = compareSamples([populationSample, randomSample, weightedSample], timesToRun, groupSize)

    outputComparison(results, ["CSC Population Sample", "Pure Random Sample", "Weighted Random Sample"], timesToRun, groupSize)


if __name__ == '__main__':
    main()