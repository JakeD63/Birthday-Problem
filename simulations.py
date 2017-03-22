import random
#simulates the birthday problem with passed in days of the year
# and the number of birthdays to select for the simulation
def simulateBirthdayProblem(birthdays, numToSelect):
    #get random numbers
    r = random.sample(range(0, len(birthdays)), numToSelect)
    #get list of random sample
    list = []
    for i in r:
        list.append(birthdays[i])


    #return true if there are duplicates
    return len(list) != len(set(list))