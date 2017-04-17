from DataFetch import getDatesFromFile
from Simulations import *
from sys import stdout
def main():
    testRun()

def testRun():
    timesToRun = 1000
    groupSize = 23
    mean = 0
    populationSample = getDatesFromFile('data.txt')

    randomSample = generateRandomBirthdays(len(populationSample))
    weightedSample = generateWeightedBirthdays(populationSample, len(populationSample))

    results = compareSamples([populationSample, weightedSample, randomSample], timesToRun, groupSize)

    sampleNames = ["CSC Population Sample", "Weighted Random Sample", "Pure Random Sample"]
    outputComparison(results, sampleNames, timesToRun, groupSize)

def getMean():
    timesToRun = 1000
    groupSize = 23
    mean = 0
    populationSample = getDatesFromFile('data.txt')

    randomSample = generateRandomBirthdays(len(populationSample))
    weightedSample = generateWeightedBirthdays(populationSample, len(populationSample))

    #run simulatino 100 times, get mean difference in success rates
    for i in range(0, 100):
        results = compareSamples([weightedSample, randomSample], timesToRun, groupSize)
        mean += results[0] - results[1]
        stdout.write(str((results[0] - results[1])))
        stdout.write(', ')
    stdout.write('\n')
    mean = float(mean) / 100
    print('Mean: ' , mean)

if __name__ == '__main__':
    main()