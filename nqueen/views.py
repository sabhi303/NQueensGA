from django.shortcuts import redirect, render

# Create your views here.

# importing algorithm
from genetics.algorithm import main, population

import numpy

# altered for the time being

generationTrack = []
totalGenerations = 0
generationCounter = 0
numberQueens = 0
populationSize = 0
gotoParent = False
retVal = {}


def index(request):
    return render(request, 'inputForm.html')

def solution(request):
    
<<<<<<< HEAD
=======


>>>>>>> parent of c51b646 (sys is ready)
    global generationTrack, numberQueens, populationSize, totalGenerations
    global retVal, gotoParent
    print("generationCounter" , generationCounter)
    if(not gotoParent):
        n = int(request.GET.get('n'))
        p = request.GET.get('p')
        print(n,p.split(','))
        gotoParent = False
        retVal = main(n,p.split(','))

    generationTrack = retVal['generationTrack']
    numberQueens = retVal['numberQueen']
    populationSize = retVal['populationSize']
    totalGenerations = retVal['generation']



    context = {
        'arr': retVal['solved_2d_array'],
        'numberQuenns': retVal['numberQueen'],
        'PopulationSize': retVal['populationSize'],
        'Generation': retVal['generation'],
    }
    # print(context)
    return render(request, 'index.html', context)


def showParent(request):
<<<<<<< HEAD
    global generationCounter, totalGenerations
=======
    global generationTrack
    global generationCounter, numberQueens, populationSize, totalGenerations

    generationCounter = generationCounter + 1
    currentGeneration = totalGenerations - generationCounter
>>>>>>> parent of c51b646 (sys is ready)

    generationCounter = generationCounter + 1
    currentGeneration = totalGenerations - generationCounter

    context = common(currentGeneration)

<<<<<<< HEAD
    return render(request, "showParents.html", context)


def showChild(request):

    global generationCounter, totalGenerations

    generationCounter = generationCounter - 1
    currentGeneration = totalGenerations - generationCounter
    
    print("currentGeneration : ",currentGeneration)
    print("generationCounter" , generationCounter)

    # //he mostly pudhe gheto js mdhye
    if(generationCounter <= 1):
        generationCounter = 0   #he 0 ki 1 bghava lagel
        gotoParent = True
        return solution(request)
    
    context = common(currentGeneration)
=======
    solvedQueens = generationTrack[currentGeneration-1][0]
    # print(solvedQueens)
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1

    arr2 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1]
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1

>>>>>>> parent of c51b646 (sys is ready)


    # print(context)

    return render(request, "showParents.html", context)


def common(currentGeneration):

    global generationTrack,gotoParent
<<<<<<< HEAD
    global  numberQueens, populationSize
=======
    global generationCounter, numberQueens, populationSize, totalGenerations

    

    generationCounter = generationCounter - 1
    currentGeneration = totalGenerations - generationCounter
    
    print("currentGeneration : ",currentGeneration)
    print("generationCounter" , generationCounter)
    if(generationCounter <= 1):
        generationCounter = 0   #he 0 ki 1 bghava lagel
        gotoParent = True
        return solution(request)

>>>>>>> parent of c51b646 (sys is ready)

    arr1 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][0]
    for ielem in range(numberQueens):
        arr1[ielem][solvedQueens[ielem] - 1] = 1

    arr2 = numpy.zeros((numberQueens, numberQueens))
    solvedQueens = generationTrack[currentGeneration-1][1]
    for ielem in range(numberQueens):
        arr2[ielem][solvedQueens[ielem] - 1] = 1

<<<<<<< HEAD
=======
    print(generationCounter, numberQueens,
            populationSize, totalGenerations)
    print(generationTrack)
>>>>>>> parent of c51b646 (sys is ready)
    context = {
        'arr1': arr1,
        'arr2': arr2,
        'numberQuenns': numberQueens,
        'PopulationSize': populationSize,
        'currentGeneration': currentGeneration,
    }
    return context