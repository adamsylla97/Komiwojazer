import random


def generateCities(amountOfCities):

    print(f"random cities to generate:{amountOfCities}")
    x=0
    tab = []
    while x < amountOfCities :
        tab.append((x, random.randrange(1,100), random.randrange(1,100)))
        x = x+1

    return tab



if __name__ == '__main__':
    #CONFIG
    amountOfCities = 10

    cities = generateCities(amountOfCities)

    for i in range(amountOfCities) :
        print(cities[i])


