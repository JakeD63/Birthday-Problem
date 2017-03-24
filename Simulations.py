import random
from numpy.random import choice


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

def generateWeightedBirthdays(population, num = 200):
    # returns a list of birthdays that have been generated randomly
    # based on a passed in list. This works by segmenting the passed in
    # data into 12 sections (1/month), and assigning each section a probability

    # generate sections (all will be 30 days except the last, 366 possible days)
    sections = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 367]
    bins = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in population:
        secIndex = 0
        while i > sections[secIndex]:
            secIndex +=1
        bins[secIndex] +=1
    #normalize bins so that they are percentages
    for i in range(0, len(bins)):
        bins[i] /= len(population)
    
    #use choice to get which section to generate birthdays in each iteration
    print(choice(sections, p=bins))




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

