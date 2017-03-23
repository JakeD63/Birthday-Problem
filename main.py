from DataFetch import getDatesFromFile
from Simulations import *

def main():
    # currently prints true if random group of 23 dates
    # from data.txt contains duplicates
    sampleSize = 23
    timesToRun = 1000
    populationSample = getDatesFromFile('data.txt')
    populationResult, randomResult = compareSampleWithRandomData(populationSample, timesToRun, sampleSize)
    popPercent = float(populationResult) / timesToRun * 100
    randPercent = float(randomResult) / timesToRun * 100

    print("Simulations Run: " + str(timesToRun) + " Sample Size: " + str(sampleSize))
    print("Population Sample Stats: " + str(popPercent) + "% Success")
    print("Randomly Generated Sample Stats: " + str(randPercent) + "% Success")

if __name__ == '__main__':
    main()