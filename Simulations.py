import random

## TODO: return more than just true/false, include the duplicate(s) as well
def simulateBirthdayProblem(birthdays, numToSelect):
    # simulates the birthday problem with passed in list of birthdays
    # and the number of birthdays to select for the simulation
    # NOTE: param birthdays is expected to be converted to day of the year
    #       (ex. 01/01/2017 should be 1)

    # get random numbers to sample
    indices = random.sample(range(0, len(birthdays)), numToSelect)
    # get list of random sample

    sample = []
    for i in indices:
        sample.append(birthdays[i])

    #return true if there are duplicates
    return len(sample) != len(set(sample))


def generateRandomBirthdays(num):
    # returns a list of random birthdays to be used
    # with the simulation
    sample = []
    for i in range(0, num):
        sample.append(random.randint(0, 366))

    return sample

def compareSampleWithRandomData(populationSample, timesToRun, sampleSize):
    # This will run a simulation timesToRun times, comparing two lists of data
    populationSuccess, randomSuccess = 0, 0
    for i in range(0, timesToRun):
        random = generateRandomBirthdays(len(populationSample))
        if simulateBirthdayProblem(populationSample, sampleSize):
            populationSuccess += 1
        if simulateBirthdayProblem(random, sampleSize):
            randomSuccess += 1
    return populationSuccess, randomSuccess

