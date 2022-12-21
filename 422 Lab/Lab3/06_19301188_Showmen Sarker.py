import numpy as np
file = open('input.txt')
input = file.readlines()

noOfBatsmen,goal = input[0].split()
goal = int(goal)
runs = []
names =[]

for characters in input[1:]:  
    name,run = characters.split()
    names.append(str(name))
    runs.append(int(run))

start_population = 1000
population = np.random.randint(0 , 2,(start_population, int(noOfBatsmen))) 
mutationThreshold = 0.4


def diff(bestFit, goal): 
    minimum = 99999
    for i in range(len(bestFit)):
        diff = abs(goal - bestFit[i])
        if diff < minimum:
            minimum = diff
            index = i
    return index

def crossing(cross1, cross2, crossLength):
    breakPoint = np.random.randint(0, crossLength)
    child = cross1[:breakPoint]
    child = np.append(child, cross2[breakPoint:])
    return child

def mutation(baccha):
    mutationIndex = np.random.randint(0,len(baccha))
    if baccha[mutationIndex] == 0:
        baccha[mutationIndex] = 1
    elif baccha[mutationIndex] == 1:
        baccha[mutationIndex] = 0
    return baccha

def bestSelection(population, bestFit, goal): 
    minimum = 99999
    for i in range(len(bestFit)):
        diff = abs(goal - bestFit[i])
        if diff < minimum:
            minimum = diff
            index = i
    bestFit[index] = 99999
    minimum2 = 99999
    for i in range(len(bestFit)):
        diff = abs(goal - bestFit[i])
        if diff < minimum2:
            minimum2 = diff
            index2 = i
    return population[index], population[index2]

def fitnessFunction(population, noOfBatsmen, runs):
    bestFit = []
    for i in population:
        temp = []
        for f in range(int(noOfBatsmen)):
            temp.append(i[f] * runs[f])
        zero = True
        for items in temp:
            if items != 0:
                zero = False
                break
        if zero:
            bestFit.append(-9999)
        else:
            bestFit.append(sum(temp))
    return bestFit

def GAlgo(population,names, noOfBatsmen, runs, mutationThreshold, goal):
    maxGeneration = 20
    generation = 1
    while True:
        bestFit = fitnessFunction(population, noOfBatsmen, runs)
        finalIndex = diff(bestFit, goal)
        if bestFit[finalIndex] == goal:
            print(names)
            s = ""
            for i in population[finalIndex]:
                s = s + str(i)
            print(s)
            break
        elif generation > maxGeneration:
            print(names)
            print(-1)
            break
        else:
            newGeneration = []
            for i in range(len(population)):
                cross1, cross2 = bestSelection(population, bestFit, goal)
                crossLength = int(len(cross1))
                baccha = crossing(cross1, cross2, crossLength)
                mutationChance = np.random.random()
                if mutationChance > mutationThreshold:
                    baccha = mutation(baccha)
                newGeneration.append(baccha)
            newGeneration = np.array(newGeneration)
            population = np.concatenate((population, newGeneration), axis=0) 
            generation += 1
        print("Generation", generation)

GAlgo(population,names, noOfBatsmen, runs, mutationThreshold, goal)