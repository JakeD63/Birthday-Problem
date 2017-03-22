import random

## TODO: return more than just true/false, include the duplicate(s) as well
def simulateBirthdayProblem(birthdays, numToSelect):
    # simulates the birthday problem with passed in list of birthdays
    # and the number of birthdays to select for the simulation
    # NOTE: param birthdays is expected to be converted to day of the year
    #       (ex. 01/01/2017 should be 1)

    #get random numbers to sample
    indices = random.sample(range(0, len(birthdays)), numToSelect)
    #get list of random sample

    sample = []
    for i in indices:
        sample.append(birthdays[i])

    #return true if there are duplicates
    return len(sample) != len(set(sample))