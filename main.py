from DataFetch import getDatesFromFile
from Simulations import *

def main():
    testRun()

def testRun():
    populationSample = getDatesFromFile('data.txt')

    compareSampleWithRandomData(populationSample, 1000, 23)



if __name__ == '__main__':
    main()