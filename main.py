from DataFetch import getDatesFromFile
from Simulations import *

def main():
    #compareSamples()
    populationSample = getDatesFromFile('data.txt')

def compareSamples():
    # currently prints true if random group of 23 dates
    # from data.txt contains duplicates
    peopleSelected = 23
    timesToRun = 1000
    populationSample = getDatesFromFile('data.txt')
    populationResult, randomResult = compareSampleWithRandomData(populationSample, timesToRun, peopleSelected)
    popPercent = float(populationResult) / timesToRun * 100
    randPercent = float(randomResult) / timesToRun * 100

    print("Simulations Run: " + str(timesToRun) + " People Selected: " + str(peopleSelected))
    print("Population Sample Stats: " + str(popPercent) + "% Success")
    print("Randomly Generated Sample Stats: " + str(randPercent) + "% Success")


if __name__ == '__main__':
    main()