import math
import random


import numpy

generationTrack = []


def population(populationSz):
    """
    This function will generate population
    of chromosomes as per populationSz
    :type populationSz: int
    """
    l1 = [i for i in range(1, populationSz + 1)]
    random.shuffle(l1)
    return l1

def mypopulation(n,populationSize):
    inp=[]
    total=[]
    for i in range(n):
        if(str(i) not in populationSize):
            inp.append(i)
    k=math.factorial(len(inp))
    
    # if(k==0):
    #     total.append(list(map(int,populationSize)))
    
    if(k>20):
        for i in range(20):
            random.shuffle(inp)
            k=0
            ans=[]
            for j in range(n):
                if(populationSize[j]=='-1'):
                    ans.append(inp[k]+1)
                    k+=1
                else:
                    ans.append(int(populationSize[j])+1)
            total.append(ans)
    else:
        for i in range(k):
            random.shuffle(inp)
            k=0
            ans=[]
            for j in range(n):
                if(populationSize[j]=='-1'):
                    ans.append(inp[k]+1)
                    k+=1
                else:
                    ans.append(int(populationSize[j])+1)
            total.append(ans)
        for i in range(20-k):
            total.append(population(n))
    # if(k==0):
    #     total.pop()
    return total,20
                



def selection(total_population, percentage):
    """
    This method will select top most fit
    candidates or population as per percentage provided
    :param total_population: Total list of chromosome
    :param percentage: Top fit percentage to retain
    :return: sub list to most fit population
    """
    return total_population[:math.ceil(len(total_population) * percentage)]


def fitness(chromosome, sz):
    """
    Returns Fitness of each chromosome
    where 0 means chromosome is fittest
    :param chromosome: list containing chromosome
    :param sz: size of chromosome
    :return: int
    """
    ctr1 = 0
    ctr2 = 0
    f1 = []
    f2 = []
    for i in range(sz):
        f1.append(chromosome[i] - (i + 1))
        f2.append(sz - chromosome[i] - (i + 1))
    list.sort(f1)
    list.sort(f2)
    for i in range(1, sz):
        if f1[i] == f1[i - 1]:
            ctr1 += 1
        if f2[i] == f2[i - 1]:
            ctr2 += 1
    return ctr1 + ctr2


def crossover(p1: list, p2: list) -> tuple:
    """
    Takes in 2 chromosomes and preforms a
    crossover between them
    :param p1: chromosome 1
    :param p2: chromosome 2
    :return: tuple
    """
    sz = len(p1)
    child1 = []
    child2 = []
    for i in range(sz):
        child1.append(-1)
        child2.append(-1)
    pt1 = random.randint(0, sz - 1)
    pt2 = getAnotherPoint(pt1, sz)
    if pt1 > pt2:
        tmp = pt1
        pt1 = pt2
        pt2 = tmp
    for i in range(pt1, pt2):
        child1[i] = p1[i]
        child2[i] = p2[i]
    child1 = fillEmpty(child1, p2)
    child2 = fillEmpty(child2, p1)

    return child1, child2


def getAnotherPoint(pt1, sz):
    """
    Returning a random point different
    from pt1 based on range 0 to sz
    :rtype: int
    """
    pt2 = random.randint(1, sz - 1)
    if pt2 != pt1:
        return pt2
    else:
        return getAnotherPoint(pt1, sz)


def fillEmpty(child, parent):
    """
    This function is a helper for
    crossover as it fills all the empty
    slots in child chromosomes (in our case -1)
    with values of parent which are not present in child
    :param child: list
    :param parent: list
    :return: list
    """
    childSz = len(child)
    sz = len(parent)
    for i in range(childSz):
        for j in range(sz):
            if child[i] == -1 and (parent[j] not in child):
                child[i] = parent[j]
    return child


def mutation(chromosome, factor):
    """
    Changes the chromosome by
    swapping the indexes of element
    if a random number is greater than
    mutation factor
    :param chromosome: list
    :param factor: float
    :return: list
    """
    number = random.uniform(0, 1)
    if number >= factor:
        rand1 = random.randint(0, len(chromosome) - 1)
        rand2 = random.randint(0, len(chromosome) - 1)
        if rand1 != rand2:
            tmp = chromosome[rand1]
            chromosome[rand1] = chromosome[rand2]
            chromosome[rand2] = tmp

    return chromosome


def nQueen(bordSize, totalPop, maxGeneration, totalItr=0, mutationFactor=0.5):
    """
    Main function to provide
    solution to n-queens
    :param mutationFactor: Mutation factor
    :param bordSize: Size of n x n board
    :param totalPop: starting point of populations
    :param maxGeneration: total number of recursions
    :param totalItr: current recursion number
    :return: list
    """
    if totalItr > maxGeneration:
        # //ithe error takayachay
        return "No solution found after generation %d"%totalItr
    totalItr += 1
    fitnessValues = []
    
    # print("totalPop : ",totalPop)
    
    for j in range(len(totalPop)):
        
        fitValue = fitness(totalPop[j], bordSize)
        
        if fitValue == 0:
            print("Got solution in generation " + str(totalItr))
            return totalPop[j], totalItr
        fitnessValues.append(fitValue)
    populationFitness = list(zip(fitnessValues, totalPop))
    
    
    
    populationFitness.sort(key=lambda x: x[0])
    newRange = math.ceil(math.sqrt(len(totalPop)))
    if newRange < 2:
        return "No solution found",1000

    topFitPopulation = []
    for j in range(newRange):
        if len(populationFitness) >= j:
            topFitPopulation.append(populationFitness[j])
    topFitPopulation = list(zip(topFitPopulation[::2], topFitPopulation[1::2]))
    finalPopulation = []
    global generationTrack
    for topPair in topFitPopulation:
        child1, child2 = crossover(topPair[0][1], topPair[1][1])

        generationTrack.append([child1,child2])

        child1 = mutation(child1, mutationFactor)
        child2 = mutation(child2, mutationFactor)
        finalPopulation.append(child1)
        finalPopulation.append(child2)
    return nQueen(bordSize, finalPopulation, maxGeneration, totalItr)


def main(n, populationSize):
    
    totalPopulation = []
    if(len(populationSize)==1):
        populationSize=int(populationSize[0])
        for ielem in range(populationSize):
            totalPopulation.append(population(n))
    else:
        totalPopulation,populationSize=mypopulation(n,populationSize)
    print(totalPopulation)

    # print("totalPopulation : ",totalPopulation)

    itrs = 0    #initial iteration number
    maxIters = 1000 #introduce limit
    solvedQueens,generation = nQueen(n, totalPopulation, maxIters, itrs)
    

    # //jr soln aal tr
    if isinstance(solvedQueens, str):
        print(solvedQueens)
        exit(0)

    # print(solvedQueens)

    solved_2d_array = numpy.zeros((n, n))

    for ielem in range(n):
        solved_2d_array[ielem][solvedQueens[ielem] - 1] = 1
        
    
    global generationTrack
    
    context = {
        'solvedQueens' : solvedQueens,
        'solved_2d_array' : solved_2d_array,
        'generation' : generation,
        'numberQueen' : n,
        'populationSize' : populationSize,
        'generationTrack' : generationTrack
    }
    # print(solved_2d_array)
    # print("Generation Track\n",generationTrack)
    # print(context)
    return context

# main(8,4)