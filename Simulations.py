import random
from numpy.random import choice


def simulateBirthdayProblem(birthdays, groupSize):
    # simulates the birthday problem with passed in list of birthdays
    # and the number of birthdays to select for the simulation
    # NOTE: param birthdays is expected to be converted to day of the year
    #       (ex. 01/01/YYYY should be 1)

    # get random numbers to sample
    indices = random.sample(range(0, len(birthdays)), groupSize)
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
    sections = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 367]
    bins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in population:
        secIndex = 0
        while i > sections[secIndex]:
            secIndex +=1
        bins[secIndex - 1] +=1
    #normalize bins so that they are percentages
    for i in range(0, len(bins)):
        bins[i] /= len(population)
    # use choice to get which section to generate birthdays in each iteration
    # bins are strictly greater than, so if choice returns 240, the range is 240-270
    sample = []
    for i in range(0, num):
        r1 = choice(sections, p=bins)
        # set upper limit, special case for 360-367 since range is not 30 like the others
        if r1 == 360:
            r2 = 367
        else:
            r2 = r1 + 30
        sample.append(random.randint(r1, r2))
    return sample


def compareSamples(samples, timesToRun, groupSize):
    # This will run a simulation timesToRun times
    # comparing samples sent in
    # args: samples    - a list of samples (list of lists)
    #       timesToRun - number of simulations to run
    #       groupSize  - size of groups

    #set up results list with 0 as initial value
    results = []
    for i in range(0, len(samples)):
        results.append(0)

    for i in range(0, timesToRun):
        for s in range(0, len(samples)):
            if(simulateBirthdayProblem(samples[s], groupSize)):
                results[s] += 1

    return results

def outputComparison(sampleResultsList, sampleNameList, timesRun, groupSize):
    # outputs comparison of samples

    if len(sampleResultsList) != len(sampleNameList):
        print("Sample results and names list must be same length")
        return

    template = "{0:25}{1:4}"
    print("Simulation Results")
    print("Number of Simulations Run: " + str(timesRun))
    print("Number of people selected in each simulation: " + str(groupSize) + '\n')
    print(template.format("Sample Name", "Sample Success Rate") + '\n')
    for i in range(0, len(sampleNameList)):
        print(template.format(sampleNameList[i], str("{0:.2f}".format(float(sampleResultsList[i]) / timesRun * 100)) + '%'))
